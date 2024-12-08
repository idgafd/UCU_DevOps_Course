import configparser
from flask import Flask

def get_message():
    config = configparser.RawConfigParser()
    config.read('config.properties')
    if config.getboolean("features", "feature_1"):
        return "Hello, Anastasiia!"
    else:
        return "Hello, World!"

app = Flask(__name__)

@app.route("/")
def hello():
    return get_message()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050)
