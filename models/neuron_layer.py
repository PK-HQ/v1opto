# models/neuron_layer.py

import numpy as np
from .neuron_models import LIFNeuron

class LIFNeuronLayer:
    def __init__(self, size=(512, 512), neuron_model="LIF", input_scaling=10):
        self.size = size
        self.neurons = [[LIFNeuron() for _ in range(size[1])] for _ in range(size[0])]
        self.spiking_activity = np.zeros(size)  # Track spikes in the 2D layer
        self.input_scaling = input_scaling  # Scale factor for input

    def stimulate_neurons(self, input_matrix):
        """Stimulate neurons based on the input matrix of currents."""
        # Scale the input matrix for better compatibility with neuron thresholds
        input_matrix *= self.input_scaling
        print("Scaled input matrix min/max:", np.min(input_matrix), np.max(input_matrix))  # Debugging statement

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.spiking_activity[i, j] = self.neurons[i][j].simulate_step(input_matrix[i, j])

        print("Spiking activity after stimulation:", np.sum(self.spiking_activity))  # Total spikes as debug info

    def reset_activity(self):
        """Reset the spiking activity matrix for a new trial."""
        self.spiking_activity.fill(0)
