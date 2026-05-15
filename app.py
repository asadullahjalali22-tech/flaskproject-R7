from flask import Flask

app =Flask(__name__)

@app.route("/")
def home():
    return "this home for project R7"

@app.route("/about")
def about():
    return "this is a test for CI github"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
