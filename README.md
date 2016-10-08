# Photo booth based on Chainer implementation of "Perceptual Losses for Real-Time Style Transfer and Super-Resolution"
Fast artistic style transfer by using feed forward network.

## Requirements and Setup
- [Chainer](https://github.com/pfnet/chainer)
- [Pre-trained Models](https://github.com/gafr/chainer-fast-neuralstyle-models)
- [Pillow](https://python-pillow.org/)
- [Flask](http://flask.pocoo.org/)
- [Tornado](http://www.tornadoweb.org)

Set up Chainer impplementation of fast neural style in  directory called 'cfns' inside the root directory.
Chainer source can be obtained [here](https://github.com/yusuketomoto/chainer-fast-neuralstyle).  

Clone the [pre-trained models](https://github.com/gafr/chainer-fast-neuralstyle-models)
in a directory named 'chainer-fast-neuralstyle-models' inside the root directory.  

Then, install the required python packages using pip.
Note that a [virtual environment](https://docs.python.org/3/library/venv.html) can be used to remove the need for sudo access.

Pillow can be installed with either
```
$ pip install Pillow
```  
or
```
$ easy_install Pillow
```  

Install Tornado:
```
$ pip install tornado
```  

Install Flask:
```
$ pip install Flask
```  

Finally, serve the flask app from the project root directory
```
$ python app.py
```

## References
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://arxiv.org/abs/1603.08155)

This app uses the following projects, either directly or slightly adapted:
- [webcam.js](https://github.com/jhuckaby/webcamjs)
- [chainer-fast-neuralstyle](https://github.com/yusuketomoto/chainer-fast-neuralstyle) Chainer implementation of "Perceptual Losses for Real-Time Style Transfer and Super-Resolution".
- [chainer-fast-neuralstyle-models](https://github.com/gafr/chainer-fast-neuralstyle-models) Pre-trained models compatible with the repository above. 
