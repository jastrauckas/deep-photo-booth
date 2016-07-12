from flask import Flask
import flask
import os, sys, inspect
app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/generate')
def generate():
    #inputPath = request.args.get('input')
    #outputPath = request.args.get('output')
    os.system('python cfns/generate.py cfns/sample_images/tubingen.jpg -m cfns/models/starrynight.model -o cfns/sample_images/output2.jpg')
    return flask.render_template('index.html')
