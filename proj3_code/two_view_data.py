"""Data from two views."""

import numpy as np

def preprocess_data(x_0s, x_1s):
    """Preprocess data to make them homogeneous."""
    x_0s = np.append(x_0s, np.ones((x_0s.shape[0], 1)), axis=1)
    x_1s = np.append(x_1s, np.ones((x_1s.shape[0], 1)), axis=1)
    return x_0s, x_1s

def read_from_text(path_0='../data/pts2d-pic_a.txt',
                   path_1='../data/pts2d-pic_b.txt'):
    """Load a pair of 2D point files and return them in homogeneous form."""
    x_0s = np.loadtxt(path_0)
    x_1s = np.loadtxt(path_1)
    return preprocess_data(x_0s, x_1s)

