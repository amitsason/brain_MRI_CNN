# brain_MRI_CNN
DIP (digital image processing) project.
classifying brain MRI images with tumors and without using a Convolutional Neural Network in Python. 

about the dataset:
the dataset was aquiered from the web and contains 150 samples of different brain images.
training set contains 120 images and test set contains 30 images (common ratio of 80:20).
the dataset is very poor in size and resolution and was hand cropped.
* Brains with Tumer ![picture alt](https://github.com/amitsason/brain_MRI_CNN/blob/master/readme%20images/tumorExmple.JPG)
* Brains without Tumer ![picture alt](https://github.com/amitsason/brain_MRI_CNN/blob/master/readme%20images/normalExample.JPG)


about the CNN:
Keras deep learning library was used.
input image resolution for my model is 128X128X3 RGB.
each photo was passed through 32 filters each one 3X3 in size. the result was that each image had 32 featured images.
the featured images were passed through a pooling layer with Max Pooling of 2X2 in size. the max pooling got rid of 75% of the "irelevant" or "excess" information pixels and we were left with 32 images each one with 0.25(128X128) = 32X32 pixel resolution.
Next a second convolution layer with 32 3X3 fiters and 2X2 max pooling was added. Now each original image has 1024 pooled feature maps with 8X8 resolution. All the feature maps were flattened into a single vector which is the input vector for our Artificial Neural Network e.g. a vector size of 1024(8X8) = 65,536.
two convolution layers were used, and 64 neurons in the neural network.
![picture alt](https://github.com/amitsason/brain_MRI_CNN/blob/master/readme%20images/convolutional_neural_network.png)

model result:
my goals in this project were to succeed in classifying images with tumors.
the results of my model is are 98.5% success rate on the training set, and 76.6% success rate on the test set.


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



