# brain_MRI_CNN
DIP (digital image processing) project.
classifying brain MRI images with tumors and without using a Convolutional Neural Network in Python. 

about the dataset:
the dataset was aquiered from the web and contains 150 samples of different brain images.
training set contains 120 images and test set contains 30 images (common ratio of 80:20).
the dataset is very poor in size and resolution and was hand cropped.
![picture alt](https://github.com/amitsason/brain_MRI_CNN/blob/master/dataset/test_set/normal/normal.1.jpg)

about the CNN:
Keras deep learning library was used.
input image resolution for my model is 128X128X3 RGB.
two convolution layers were used, and 64 neurons in the neural network.
![picture alt]()

model result:
my goals in this project were to succeed in classifying images with tumors.
the results of my model is are 98.5% success rate on the training set, and 76.6% success rate on the test set.
![picture alt]()

reccomendation
get a better dataset and get better results, GIGO principle follows here
Garbage In Garbage Out.

# how to use the CNN:

## using the hdf5 ready to use weights file:
the weights hdf5 file 'mri_model_weights.h5' is attached and you can put it in a directory along with the 'predicting single image.py'
python file and the dataset folder containing the test set.
you can even upload an image of your own if you want to test it.


## teaching the network from scratch:
you have to get your own dataset (mine was to big to upload here)
and run the 'mri_cnn.py' file



