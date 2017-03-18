from sys import argv
from flask import Response
from flask import Flask
import yaml
import json
from github import Github

script, link = argv

print link

link = link.split('/')
repo = link[-1]
user = link[-2]


app = Flask(__name__)


def getYmlContent(environment):
    try:
        git = Github().get_user(user).get_repo(repo)
        content = git.get_file_contents(environment + "-config.yml").content.decode(
            git.get_contents(environment + "-config.yml").encoding)
        return content
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
    return getYmlContent(environment)


@app.route("/v1/<environment>-config.json")
def configJson(environment):
    return generateJSON(getYmlContent(environment))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
