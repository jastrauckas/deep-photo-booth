from flask import Flask, request, send_from_directory
import flask
import base64
import os, sys, inspect, time
app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    #snapshot = request.args.get('snapshot')
    #print snapshot
    #outputPath = request.args.get('output')
    snapshot_str = request.values['snapshot']
    print 'CONTENT: ' + str(snapshot_str.split(',')[1])
	imgdata = base64.b64decode(snapshot_str.split(',')[1])
	if not os.path.exists('cfns/sample_images'):
		os.makedirs('cfns/sample_images')
    input_filename = 'cfns/sample_images/snapshot' + str(time.time()) + '.jpg'
    output_filename = 'cfns/sample_images/output' + str(time.time()) + '.jpg'
    with open(input_filename, 'wb+') as f:
        f.write(imgdata)
    os.system('python cfns/generate.py ' + input_filename + ' -m cfns/models/seurat.model -o ' + output_filename)
    #return flask.render_template('index.html')
    return '/' + output_filename

@app.route('/cfns/sample_images/<path:image_name>')
def send_image(image_name):
    return send_from_directory('cfns/sample_images/', image_name)

