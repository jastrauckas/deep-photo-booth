import base64
import flask
from flask import Flask, request, send_from_directory
import os, sys, inspect, time
import json
from subprocess import Popen

app = Flask(__name__)

@app.route('/')
def index():
	return flask.render_template('index.html')

@app.route('/static/css/<path:stylesheet_name>')
def send_css(stylesheet_name):
	return send_from_directory('static/css/', stylesheet_name)

@app.route('/generate', methods=['POST'])
def generate():
	snapshot_str = request.values['snapshot']
	style_names = json.loads(request.values['styles'])
	#print "SELECTED STYLE: " + style_names[0]
	#print 'CONTENT: ' + str(snapshot_str.split(',')[1])

	imgdata = base64.b64decode(snapshot_str.split(',')[1])
	if not os.path.exists('cfns/sample_images'):
		os.makedirs('cfns/sample_images')
	input_filename = 'cfns/sample_images/snapshot' + str(time.time()) + '.jpg'
	with open(input_filename, 'wb+') as f:
		f.write(imgdata)
	
	output_paths = []
	procs = [] 

	# start file transfer commands in parallel
	for i in range(len(style_names)):
		style_str = style_names[i]
		output_filename = 'cfns/sample_images/output' + style_str + str(time.time()) + '.jpg'
		p = Popen(['python', 'cfns/generate.py', input_filename, '-m', 'chainer-fast-neuralstyle-models/models/'+style_str+'.model', '-o', output_filename])
		procs.append(p)
		output_paths.append('/' + output_filename)
		
	# poll procs until they are all finished
	all_done = False
	while not all_done:
		time.sleep(0.5)
		all_done = True
		for p in procs:
			if p.poll() is None:
				all_done = False

	return json.dumps(output_paths)

@app.route('/cfns/sample_images/<path:image_name>')
def send_image_old(image_name):
	return send_from_directory('cfns/sample_images/', image_name)

@app.route('/chainer-fast-neuralstyle-models/images/<path:image_name>')
def send_image(image_name):
	return send_from_directory('chainer-fast-neuralstyle-models/images/', image_name)

if __name__ == "__main__":
	if os.path.isfile('ssl/server.crt'):
		from tornado.wsgi import WSGIContainer
		from tornado.httpserver import HTTPServer
		from tornado.ioloop import IOLoop

		http_server = HTTPServer(WSGIContainer(app), ssl_options={
			'certfile': 'ssl/server.crt',
			'keyfile': 'ssl/server.key'
		 })

		http_server.listen(5000)
		print('hello')
		try:
				IOLoop.instance().start()
		except KeyboardInterrupt:
			IOLoop.instance().stop()
	else:
		app.run(host="0.0.0.0", port=int("5000"))
		

