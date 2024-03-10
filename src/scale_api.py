from flask import Flask

app = Flask(__name__)

@app.route("/scales")
def scales():
    return "<p>Hello, World!</p>"