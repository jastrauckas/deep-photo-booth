# Photo booth based on Chainer implementation of "Perceptual Losses for Real-Time Style Transfer and Super-Resolution"
Fast artistic style transfer by using feed forward network.

## Requirements and Setup
- [Chainer](https://github.com/pfnet/chainer)
- [Pillow](https://python-pillow.org/)

Set up Chainer impplementation of fast neural style in  directory called 'cfns' inside the root directory.
Chainer source can be obtained [here](https://github.com/yusuketomoto/chainer-fast-neuralstyle).  

Pillow can be installed with either
```
$ pip install Pillow```  
or
```
$ easy_install Pillow
```

## Reference
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://arxiv.org/abs/1603.08155)

Code written in this repository uses the following projects.
- [webcam.js](https://github.com/jhuckaby/webcamjs)
- [chainer-gogh](https://github.com/mattya/chainer-gogh.git) Chainer implementation of neural-style. I heavily referenced it.
- [chainer-cifar10](https://github.com/mitmul/chainer-cifar10) Residual block implementation is referred.
