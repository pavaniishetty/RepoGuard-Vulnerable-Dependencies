from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "RepoGuard dependency scanning fixture"

if __name__ == "__main__":
    app.run()
