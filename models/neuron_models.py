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

    def __init__(self, threshold=-50, reset_value=-70, tau_m=20, resistance=1):
        super().__init__()
        # Define parameters, allowing for flexibility in threshold and reset values
        self.parameters = {
            "tau_m": tau_m,
            "R_m": resistance,
            "V_th": threshold,
            "V_reset": reset_value,
        }
        self.membrane_potential = self.parameters["V_reset"]

    def simulate_step(self, input_current):
        # Debugging statement to track membrane potential changes
        print(f"Membrane potential before: {self.membrane_potential}")

        # Update membrane potential
        self.membrane_potential += (input_current * self.parameters["R_m"] - self.membrane_potential) / self.parameters[
            "tau_m"]

        # Check if membrane potential has reached the threshold
        if self.membrane_potential >= self.parameters["V_th"]:
            # Reset potential and return a spike
            print("Spike generated!")
            self.membrane_potential = self.parameters["V_reset"]
            return 1  # Spike
        return 0  # No spike

# Add additional neuron models here, such as Exponential Integrate-and-Fire or Theta Neuron.
