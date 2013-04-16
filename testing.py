import urllib

print "Please input full url link of subreddit including http://"
URL = raw_input("> ")

html_str = urllib.urlopen(URL).read()

filetest = str(html_str)

segment = filetest[filetest.find("header-img"):filetest.find("\" width")]

imageurl = segment[segment.find("src=\"")+5:len(segment)]

urllib.urlretrieve(imageurl, "alien.png")