# brain_MRI_CNN
DIP (digital image processing) project.
classifying brain MRI images with tumors and without using a Convolutional Neural Network in Python. 

about the dataset:
the dataset was aquiered from the web and contains 150 samples of different brain images.
training set contains 120 images and test set contains 30 images (common ratio of 80:20).
the dataset is very poor in size and resolution and was hand cropped.

about the CNN:
Keras deep learning library was used.
input image resolution for my model is 128X128X3 RGB.
two convolution layers were used, and 64 neurons in the neuron network.

model result:
my goals in this project were to succeed in classifying images with tumors.
the results of my model is are 98.5% success rate on the training set, and 76.6% success rate on the test set.

reccomendation
get a better dataset and get better results, GIGO principle follows here
Garbage In Garbage Out.
