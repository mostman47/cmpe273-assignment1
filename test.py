import urllib2
import json
from sys import argv

script,link = argv

print link

link = link.split('/') 
repo = link[-1]
user = link[-2]

a = urllib2.urlopen("https://api.github.com/repos/%s/%s/contents" % (user,repo)).read()
# print a
a = json.loads(a) 
# print a
for j in a:
    print j['name']