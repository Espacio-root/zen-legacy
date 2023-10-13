from mitmproxy import http
import re
import os

class Blocker:

    def __init__(self):
        self.fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blocklist.txt')
        self.redirect_url = 'https://www.google.com/search?q=inspiring+quotes+for+entrepreneurs&tbm=isch'

        assert self.fp, 'Blocklist file not found'
        self._process_blocklist()

    def _process_blocklist(self):
        with open(self.fp, 'r') as f:
            self.redirects = [f'www.{line.strip()}' for line in f.readlines()]
    
    def request(self, flow: http.HTTPFlow):
        if flow.request.host in self.redirects:
            flow.request.url = self.redirect_url

addons = [
    Blocker()
]
