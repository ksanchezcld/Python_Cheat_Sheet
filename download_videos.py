# apple.py - leverage Python to help me learn better
# Assembly... and vice versa LOL
import urllib, urllister
usock = urllib.urlopen("http://www.securitytube.net/groups?operation=view&groupId=5")
parser = urllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()
lines_seen = set()
for url in parser.urls:
if "video" in url:
if url not in lines_seen:
lines_seen.add(url)
url = "http://www.securitytube.net" + url
usock = urllib.urlopen(url)
html = usock.read()
first = html.find("'file=http://videos.securitytube.net")
last = html.find(".mp4")
vidurl = html[first+6:last+4]	
print vidurl
urllib.urlretrieve(vidurl, vidurl[31:])

#<embed type="application/x-shockwave-flash" src="http://miliw0rm.securitytube.net/player.swf" width="640" height="480" style="undefined" id="player" name="player" quality="high" allowfullscreen="true" allowscriptaccess="always" flashvars="file=http://videos.securitytube.net/Buffer Overflow Primer Part 1 (Smashing the Stack).mp4">