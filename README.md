Example from https://www.reg.ru/blog/keras/ (origin https://www.pyimagesearch.com/2018/09/10/keras-tutorial-how-to-get-started-with-keras-deep-learning-and-python/)
With one change: to train with one object.


First of all you need to install dependencies from the `requirements.txt` file or use Docker file to run a docker container.
Prepare two image set: with object and without.

To train your Convolutional Neural Network with Keras see [train_vgg.py](train_vgg.py).

To make predictions on new data using your Keras model see [predict.py](predict.py).