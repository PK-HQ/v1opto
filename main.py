# main.py

from models.orientation_map import OrientationMap
from models.neuron_layer import LIFNeuronLayer
from models.visual_stimulus import VisualStimulus
from models.optogenetic_stimulus import OptogeneticStimulus
from models.v1_simulation import V1ModelSimulation

# Initialize components
orientation_map = OrientationMap(size=(512, 512))
neuron_layer = LIFNeuronLayer(size=(512, 512), neuron_model="LIF")
v1_simulation = V1ModelSimulation(neuron_layer=neuron_layer, orientation_map=orientation_map)

# Define stimuli
visual_stimulus = VisualStimulus(orientation=0, spatial_frequency=1, contrast=0.5, size=2, onset=0)
optogenetic_stimulus = OptogeneticStimulus(column_tuning=0, num_columns=10, column_area=50, power=1.0)

# Run a trial
trial_data = v1_simulation.run_trial(visual_stim=visual_stimulus, opto_stim=optogenetic_stimulus)
v1_simulation.output_activity("output_activity.npy")
