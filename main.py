#!/usr/bin/env python

from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/shutdown', methods=['POST'])
def handle():
    CMD = ['echo', 'hi']
    process = subprocess.Popen(CMD, stdout=subprocess.PIPE)
    out, err = process.communicate()
    print(out)
    return ''

@app.route('/')
def dashboard():
    return app.send_static_file('dashboard.html')

if __name__ == '__main__':
    app.run()
