# Hello World in flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello CSEU2!"

@app.route("/sum")
def sum():
    return f"2 * 4 = {2 * 4}"

if __name__ == '__main__':
    app.run()