#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 22:44:36 2019
@author: bbonik

Example script to demonstrate the use of the distributional undersampling
technique. A 6-dimensional dataset is loaded. Then the undersampling function 
is called, in order to create a balanced subset across all 6 dimensions. 
Different tarket distributions can be achieved by using the correct input
string.
"""

import scipy.io
import matplotlib.pyplot as plt
from distributional_undersampling import undersample_dataset
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA


def get_data(file_path="./unique_feature.txt"):
    data = pd.read_csv(file_path, header=None)
    name_list, data = np.array(data)[:, 0], np.array(data)[:, 1:]
    data = scale(data, axis=1)  # 标准化
    pca = PCA(n_components=10)
    reduced_data = pca.fit_transform(data)
    # print(reduced_data.shape)
    return name_list, reduced_data

def main():

    plt.close('all')
    
    # loading precomputed 6-dimensional data
    name_list, data = get_data()
  
    indices_to_keep = undersample_dataset(data=data,
                                          data_to_keep=3000,
                                          target_distribution='uniform',
                                          bins=10,
                                          lamda=0.5,
                                          verbose=True,
                                          scatterplot_matrix='auto')
    
    data_undersampled = data[indices_to_keep]
    f = open("select_idx.txt", "w")
    for i in range(len(indices_to_keep)):
        f.write(name_list[i]+','+str(indices_to_keep[i])+'\n')
    f.close()
    print ('Original dataset size:', str(data.shape))
    print ('Undersampled dataset size:', str(data_undersampled.shape))
    

if __name__ == '__main__':
    main()
