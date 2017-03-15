from flask import Flask
from github import Github

app = Flask(__name__)
g = Github(None,None,"https://github.com/sithu/assignment1-config-example")   

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<username>")
def getFile(username):
    return ""

repos = g.get_repo("sithu")

## TODO: Add some error checking code here to see whether
##  the lookup was successful.  Do we try/except or check the return value?

# repos = org.get_repos()

# for repo in repos:
    # print (repo.name)

print repos

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')