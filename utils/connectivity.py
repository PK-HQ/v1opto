# utils/connectivity.py

import numpy as np

def gaussian_decay(distance, std_dev):
    """Compute Gaussian decay for connectivity."""
    return np.exp(-0.5 * (distance / std_dev) ** 2)

# Add more connectivity functions here if needed
