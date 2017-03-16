import urllib2
from sys import argv
from flask import Response
from flask import Flask
import yaml
import json
import sys
# from github import Github

script, link = argv

print link

link = link.split('/')
repo = link[-1]
user = link[-2]


app = Flask(__name__)

def getYmlContent(environment):
    try:
        request = urllib2.Request(
            "https://api.github.com/repos/%s/%s/contents/%s-config.yml" % (user, repo, environment))
        request.add_header('Accept', 'application/vnd.github.VERSION.raw')
        return urllib2.urlopen(request).read()
    except:
        return "File not found!"


def generateJSON(raw):
    try:
        return Response(json.dumps(yaml.load(raw), sort_keys=True, indent=2), mimetype='application/json')
    except:
        return "Error"

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"


@app.route("/v1/<environment>-config.yml")
def configYml(environment):
    return  getYmlContent(environment)


@app.route("/v1/<environment>-config.json")
def configJson(environment):
    return generateJSON(getYmlContent(environment))



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
