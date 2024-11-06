# models/optogenetic_stimulus.py

import numpy as np

class OptogeneticStimulus:
    def __init__(self, column_tuning, num_columns, column_area, power, onset=41, pulse_cycles=6, pulse_duration=50):
        self.column_tuning = column_tuning
        self.num_columns = num_columns
        self.column_area = column_area
        self.power = power
        self.onset = onset
        self.pulse_cycles = pulse_cycles
        self.pulse_duration = pulse_duration

    def calculate_light_decay(self, center, f_50=0.1):
        """Calculate optogenetic light decay based on distance from center (1/(f^2) decay)."""
        x, y = np.indices((512, 512))
        distances = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
        decay = self.power / (1 + (distances / f_50) ** 2)
        return decay
