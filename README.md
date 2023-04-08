# picking-lovely-subdataset
Compressing a large and potentially redundant dataset into a compact and expected subdataset.

<h1>Introduction</h1>
This project implements a general method to effectively compress a raw, potentially redundant dataset into a smaller and more attractive sub-dataset. It supports text data and image data (including VR images) and is applicable to fields such as data mining and machine learning.

<h1>Data Preparation</h1>
Place the image data in the "dataset" folder (skip this section if you're working with text data).

<h1>Viewport Extraction (for VR Images)</h1>
You can open Matlab and run the "demo.m" file in the "getImageViewport" folder to extract viewports if you are working with VR images.The default parameters of the program are: 8 viewports extracted per VR image, viewport size of 512, FOV of 60 degrees, and uniform sampling along the equator.

An example is shown below:

<img src="https://github.com/WenJuing/picking-lovely-subdataset/blob/master/imgs/viewport.png" alt="fff" width="750" height="250">
<h1>Feature Extraction</h1>
Run extract_features.py to generate a feature.txt file, where each line represents the feature vector of an image for representation.

<h1>Acknowledgements</h1>
The partial code `distributional_dataset_undersampling` in this project from the `distributional_dataset_undersampling` repository by bbonik (https://github.com/bbonik/distributional_dataset_undersampling).
