import sys
sys.path.append('/home/espacio/projects/zen')

from social_media.main import Blocker, Config
from lxml import html

config = Config(
    xpath_mapping={'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a': '/home/espacio/projects/zen/social_media/youtube/channels.txt'},
    method=('literal', 'replace_url'),
    url='https://www.youtube.com/watch?v=',
    replace_url='https://www.google.com/search?q=inspiring+quotes+for+entrepreneurs&tbm=isch'
)

blocker = Blocker(config)

addons = [
    blocker
]

html_c = open('test.html', 'r').read()
# xpath = list(config.xpath_mapping.keys())[0]
xpath = r'/html/body/ytd-app/div[1]/ytd-page-manager'
content = html.fromstring(html_c)
x = content.xpath(xpath)
print(x)

