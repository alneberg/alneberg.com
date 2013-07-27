import os
from flask import Flask


app = Flas(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
