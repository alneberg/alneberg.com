import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/elin')
def elin():
    return render_template('elin.html')

if __name__ == '__main__':
    app.run()
