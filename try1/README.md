# hophacks18-memeproject
log 9/15 
building workflow


import urllib, cStringIO

file = cStringIO.StringIO(urllib.urlopen(URL).read())
img = Image.open(file)
