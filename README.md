<<<<<<< HEAD
# picking-lovely-subdataset
Compressing a large and potentially redundant dataset into a compact and expected subdataset.
=======
# Project: picking-lovely-subdataset
Compressing a large and potentially redundant dataset into a compact and expected subdataset.

<h2>Introduction</h2>
This project implements a general method to effectively compress a raw, potentially redundant dataset into a smaller and more attractive sub-dataset. 

It supports text data and image data (including VR images) and is applicable to fields such as data mining and machine learning.

<h2>Data preparation</h2>
Place the image data in the "dataset" folder (skip this section if you're working with text data).

<h2>Viewport extraction (for vr images)</h2>
You can open Matlab and run the "demo.m" file in the "getImageViewport" folder to extract viewports if you are working with VR images.

The default parameters of the program are: 8 viewports extracted per VR image, viewport size of 512, FOV of 60 degrees, and uniform sampling along the equator.

An example is shown below:

<img src="https://github.com/WenJuing/picking-lovely-subdataset/blob/master/imgs/viewport.png" alt="fff" width="750" height="250">

<h2>Feature extraction</h2>
Run extract_features.py to generate a feature.txt file, where each line represents the feature vector of an image for representation.

Then run remove_same_img.py to obtain the unique_feature.txt file, which removes duplicated feature vectors.

<h2>Distributional dataset undersampling</h2>
Run the demo.py file under the distributional_dataset_undersampling folder to generate the select_idx.txt file, which records whether each image is selected.

To select the images based on the select_idx.txt file, run the select_img.py script. 

This script will classify the images in the dataset into two folders based on whether they were selected or not.

<h2>Example</h2>
This is the experimental result on a small dataset consisting of only 20 images, some of which are identical or similar, compressed to 6 images using the proposed method.

Explanation: The bool matrix output by some of the programs for the bottom part of the images represents whether the corresponding image at that position should be selected or not.

<img src="https://github.com/WenJuing/picking-lovely-subdataset/blob/master/imgs/example.png" alt="fff" width="770" height="550">

<h2>Acknowlegde</h2>
The partial code `distributional_dataset_undersampling` in this project from the `distributional_dataset_undersampling` repository by bbonik (https://github.com/bbonik/distributional_dataset_undersampling).
>>>>>>> master
