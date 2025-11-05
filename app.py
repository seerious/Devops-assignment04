import os
from flask import Flask, Response

app = Flask(__name__)

APP_MESSAGE = os.environ.get("APP_MESSAGE", "Hello from Matthew")
APP_HEALTH = os.environ.get("APP_HEALTH", "Ok")

@app.route("/")
def index():
    return Response(APP_MESSAGE, mimetype="text/plain")

@app.route("/health")
def health():
    return Response(APP_HEALTH, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)