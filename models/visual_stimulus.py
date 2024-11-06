# models/visual_stimulus.py

class VisualStimulus:
    def __init__(self, orientation, spatial_frequency, contrast, size, onset=0):
        self.orientation = orientation
        self.spatial_frequency = spatial_frequency
        self.contrast = contrast
        self.size = size
        self.onset = onset

    def apply_to_layer(self, neuron_layer):
        """Apply visual stimulus to neuron layer (placeholder for actual implementation)."""
        pass
