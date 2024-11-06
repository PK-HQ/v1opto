# models/neuron_models.py

import numpy as np


class BaseNeuronModel:
    """Base class for neuron models with a common interface."""

    def __init__(self):
        self.parameters = {}

    def simulate_step(self, input_current):
        raise NotImplementedError("This method should be implemented by subclasses.")


class LIFNeuron(BaseNeuronModel):
    """Leaky Integrate-and-Fire Neuron."""

    def __init__(self):
        super().__init__()
        self.parameters = {"tau_m": 20, "R_m": 1, "V_th": -50, "V_reset": -70}
        self.membrane_potential = self.parameters["V_reset"]

    def simulate_step(self, input_current):
        # Simple LIF model equation
        self.membrane_potential += (input_current - self.membrane_potential) / self.parameters["tau_m"]
        if self.membrane_potential >= self.parameters["V_th"]:
            self.membrane_potential = self.parameters["V_reset"]
            return 1  # Spike
        return 0

# Add additional neuron models here, such as Exponential Integrate-and-Fire or Theta Neuron.
