# utils/gcamp_conversion.py

import numpy as np

def convert_to_gcamp(spiking_data, expression_map):
    """Convert spiking data to GCaMP fluorescence signal, modulated by expression map."""
    fluorescence = spiking_data * expression_map[..., np.newaxis]
    # Add fluorescence decay and blurring if needed (placeholder)
    return fluorescence
