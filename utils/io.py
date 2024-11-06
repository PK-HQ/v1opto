# utils/io.py

import numpy as np

def save_data(data, file_name):
    np.save(file_name, data)

def load_orientation_map(file_name):
    return np.load(file_name)
