from mitmproxy import http
import os
import re

class Blocker:

    def __init__(self):
        self.fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blocklist.txt')
        self.redirect_url = 'https://www.google.com/search?q=inspiring+quotes+for+entrepreneurs&tbm=isch'

        assert self.fp, 'Blocklist file not found'
        self._process_blocklist()

    def _process_blocklist(self):
        with open(self.fp, 'r') as f:
            self.redirects = [line.strip() for line in f.readlines()]
    
    def request(self, flow: http.HTTPFlow):
        if re.match(r'^(www\.)?' + '(' + '|'.join(self.redirects) + ')', flow.request.host, re.MULTILINE):
            flow.request.url = self.redirect_url

addons = [
    Blocker()
]
