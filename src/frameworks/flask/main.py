import sentry_sdk
from flask import Flask

sentry_sdk.init(
    dsn="https://0d4c6edfff40c66e5cdc6588154eb8ce@o4506547783270400.ingest.sentry.io/4506554556874752",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    1/0  # raises an error
    return "<p>Hello, World!</p>"