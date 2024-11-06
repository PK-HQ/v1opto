# models/v1_simulation.py

import numpy as np
from .neuron_layer import LIFNeuronLayer
from .orientation_map import OrientationMap
from .visual_stimulus import VisualStimulus
from .optogenetic_stimulus import OptogeneticStimulus
from utils.gcamp_conversion import convert_to_gcamp


class V1ModelSimulation:
    def __init__(self, neuron_layer, orientation_map, camkii_expression=None):
        self.neuron_layer = neuron_layer
        self.orientation_map = orientation_map
        self.camkii_expression = camkii_expression if camkii_expression is not None else np.ones(neuron_layer.size)
        self.trial_data = None  # Initialize trial_data as None

    def run_trial(self, visual_stim, opto_stim, trial_duration=1.2, bin_size=0.05):
        time_bins = int(trial_duration / bin_size)
        trial_data = np.zeros((self.neuron_layer.size[0], self.neuron_layer.size[1], time_bins))

        # Placeholder for applying visual and optogenetic stimuli
        # This will record the spiking activity over each time bin
        for t in range(time_bins):
            self.neuron_layer.stimulate_neurons(np.random.rand(*self.neuron_layer.size))  # Simulated input
            trial_data[:, :, t] = self.neuron_layer.spiking_activity

        # Store the trial data as an instance attribute so it can be accessed by output_activity
        self.trial_data = convert_to_gcamp(trial_data, self.camkii_expression)
        return self.trial_data

    def output_activity(self, save_path="output_activity.npy"):
        # Save the trial data if it exists
        if self.trial_data is not None:
            np.save(save_path, self.trial_data)
        else:
            print("Error: No trial data found. Please run run_trial() before output_activity().")
