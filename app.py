from flask import Flask
from datadog import initialize, statsd

options = {
    'statsd_host':'data-dog-agent-4l5l',
    'statsd_port':8125
}

initialize(**options)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Render!'

@app.route('/bad')
def good_bye_world():
    return "Page nut found", 404

@app.route('/disk')
def test():
    with open("test.txt", 'w') as f:
        f.write("test")
    with open("test.txt", 'r') as f:
        c = f.readlines()
    return c
