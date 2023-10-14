from mitmproxy import http
from lxml import html
from dataclasses import dataclass
import re
import os

@dataclass
class Config:
    xpath_mapping: dict
    method: tuple
    url: str
    replace_url: str
    
    def __post_init__(self):
        valid_methods = ('literal', 'regex')
        valid_actions = ('replace_url', 'replace_content_url')
        
        if not (
            isinstance(self.method, tuple) and
            len(self.method) == 2 and
            self.method[0] in valid_methods and
            self.method[1] in valid_actions
        ):
            raise ValueError("Invalid method configuration")

class BlockerConfig:

    def __init__(self, config):
        self.c = config
        self.xpaths = self.c.xpath_mapping.keys()
        self.filepaths = self.c.xpath_mapping.values()
        assert any([os.path.exists(fp) for fp in self.filepaths]), 'Blocklist file not found'

    def _get_xpath(self, flow):
        res = []
        with open('test.html', 'w') as fp:
            fp.write(flow.response.content.decode('utf-8'))
        content = html.fromstring(flow.response.content)
        for xpath in self.xpaths:
            x = content.xpath(xpath)
            print(x)
            if x:
                res.append(x[0])
        return res

    def _get_blocklist(self):
        return [[line.strip() for line in open(fp, 'r').readlines()] for fp in self.filepaths]

    def block_literal(self, flow):
        return any([word in xpath for block, xpath in zip(self._get_xpath(flow), self._get_blocklist()) for word in block])

    def block_regex(self, flow):
        return any([re.match(regex, xpath) for block, xpath in zip(self._get_xpath(flow), self._get_blocklist()) for regex in block])

    def replace_url(self, flow):
        flow.request.url = self.c.replace_url
        return flow

    def replace_content_url(self, flow):
        flow.response.content = flow.response.content.replace(self.c.url, self.c.replace_url)
        return flow

class Blocker(BlockerConfig):

    def __init__(self, config):
        super().__init__(config)
        self.method = config.method

    def response(self, flow: http.HTTPFlow):
        if not flow.response.headers.get('content-type', '').startswith('text/html'):
            return
        if not flow.response.status_code == 200:
            return
        if not flow.request.url.startswith(self.c.url):
            return
        to_block = getattr(self, f'block_{self.method[0]}')(flow)
        if to_block:
            flow = getattr(self, self.method[1])(flow)

