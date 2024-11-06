# models/neuron_layer.py

import numpy as np
from .neuron_models import LIFNeuron

class LIFNeuronLayer:
    def __init__(self, size=(512, 512), neuron_model="LIF"):
        self.size = size
        self.neurons = [[LIFNeuron() for _ in range(size[1])] for _ in range(size[0])]
        self.spiking_activity = np.zeros(size)  # Track spikes in the 2D layer

    def stimulate_neurons(self, input_matrix):
        """Stimulate neurons based on the input matrix of currents."""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.spiking_activity[i, j] = self.neurons[i][j].simulate_step(input_matrix[i, j])

    def reset_activity(self):
        """Reset the spiking activity matrix for a new trial."""
        self.spiking_activity.fill(0)
