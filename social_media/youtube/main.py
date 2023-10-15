import sys
sys.path.append('/home/espacio/projects/zen')

from social_media.main import Blocker, Config

config = Config(
    match_mapping={'}]},"title":{"runs":[{"text":"{word}","navigationEndpoint":{"clickTrackingParams":"': '/home/espacio/projects/zen/social_media/youtube/channels.txt'},
    method=('literal', 'replace_content_url'),
    url='https://www.youtube.com/watch?v=',
    replace_url='https://www.google.com/search?q=inspiring+quotes+for+entrepreneurs&tbm=isch'
)

blocker = Blocker(config)

addons = [
    blocker
]

# html_c = open('test.html', 'r').read()
# def debug(search_term, content):
#     pass
# print(debug('T-Series', html_c))

# print(html_c.find('}]},"title":{"runs":[{"text":"T-Series","navigationEndpoint":{"clickTrackingParams":"'))
