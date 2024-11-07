from models.orientation_map import OrientationMap
from models.neuron_layer import LIFNeuronLayer
from models.visual_stimulus import VisualStimulus
from models.optogenetic_stimulus import OptogeneticStimulus
from models.v1_simulation import V1ModelSimulation
import numpy as np
import matplotlib.pyplot as plt

### SIMULATION OF V1 VISUAL + OPTO
# Load orientation map
filepath = 'Y:/Chip/Chip20240118/run0/M28D20240118R0OrientationP2.mat'
orientation_map_instance = OrientationMap(filepath=filepath)
orientation_map = orientation_map_instance.map  # Access the loaded orientation map

neuron_layer = LIFNeuronLayer(size=(512, 512), neuron_model="LIF")
v1_simulation = V1ModelSimulation(neuron_layer=neuron_layer, orientation_map=orientation_map)

# Define trial parameters
contrasts = [0.5, 1.0]  # Example contrasts
orientations = [0, 90]  # Example orientations: 0°, 90°
column_tunings = [0, 90]  # Optostim tuning: 0°, 90°

# Preallocate trial_data and metadata arrays
time_bins = 24  # Example value, adjust according to your simulation setup
trial_data = []
metadata = []

# Run simulation for each parameter combination
for contrast in contrasts:
    for orientation in orientations:
        for tuning in column_tunings:
            # Set up visual and optogenetic stimuli based on current parameters
            visual_stimulus = VisualStimulus(orientation=orientation, spatial_frequency=1, contrast=contrast, size=2,
                                             onset=0)
            optogenetic_stimulus = OptogeneticStimulus(column_tuning=tuning, num_columns=10, column_area=50, power=1.0)

            # Run the trial
            trial_result = v1_simulation.run_trial(visual_stim=visual_stimulus, opto_stim=optogenetic_stimulus,
                                                   trial_duration=1.2, bin_size=0.05)

            # Append trial data and metadata for this combination
            trial_data.append(trial_result)
            metadata.append({"contrast": contrast, "orientation": orientation, "tuning": tuning})

# Convert trial_data to a 4D numpy array and metadata to a structured array
trial_data = np.stack(trial_data, axis=-1)  # Shape: 512 x 512 x time_bins x num_trials
metadata = np.array(metadata)  # Array of dictionaries holding each trial’s parameters

### PLOTTING ORT MAP
# Assuming `orientation_map` is a 512x512 array where each value represents the orientation tuning in degrees (0 to 165)
# Example: Load or simulate a placeholder orientation map if not already defined
# orientation_map = np.random.uniform(0, 165, (512, 512))  # Replace this with actual orientation data if available
# Plot the orientation map
orientation_map_instance = OrientationMap(size=(512, 512))
orientation_map = np.array(orientation_map_instance.map, dtype=float)  # Access the .map attribute

orientation_map = np.array(orientation_map, dtype=float)  # Convert to float if it's not already
plt.figure(figsize=(8, 8))
plt.imshow(orientation_map, cmap='hsv', vmin=0, vmax=180)  # 'hsv' colormap for orientation
plt.colorbar(label="Orientation Preference (°)")
plt.title("Orientation Tuning Preference of Neurons in V1 Layer")
plt.axis("off")  # Optional: Turn off axis for a cleaner look
plt.show()

### PLOTTING ACTIVITY
# Assuming metadata and trial_data are available from main.py execution
# Extract unique values for each parameter
contrasts = np.unique([m['contrast'] for m in metadata])
orientations = np.unique([m['orientation'] for m in metadata])
column_tunings = np.unique([m['tuning'] for m in metadata])

# Set up a 2D grid of subplots: rows for (contrast, orientation) combinations, columns for column_tuning
fig, axs = plt.subplots(len(contrasts) * len(orientations), len(column_tunings), figsize=(15, 10), squeeze=False)

# Iterate over each unique combination of contrast, orientation, and tuning
for i, contrast in enumerate(contrasts):
    for j, orientation in enumerate(orientations):
        for k, tuning in enumerate(column_tunings):
            # Find the trials that match this combination of parameters
            trial_indices = [idx for idx, m in enumerate(metadata)
                             if m['contrast'] == contrast and m['orientation'] == orientation and m['tuning'] == tuning]

            # Calculate the average 2D activity for the matching trials
            if trial_indices:
                # First, average over time bins to get a single 512x512 map per trial
                avg_across_time = np.mean(trial_data[:, :, :, trial_indices], axis=2)  # Shape: 512 x 512 x num_trials

                # Then, average across trials for this condition to get the final 512x512 map
                avg_activity_map = np.mean(avg_across_time, axis=2)  # Shape: 512 x 512
            else:
                # If no trials match, set avg_activity_map to zeros for placeholder plot
                avg_activity_map = np.zeros((512, 512))

            # Plot the 2D activity map in the corresponding subplot
            ax = axs[i * len(orientations) + j, k]
            im = ax.imshow(avg_activity_map, cmap="hot", interpolation="nearest")
            ax.set_title(f"Contrast {contrast}, Ori {orientation}°, Tuning {tuning}°")
            ax.axis('off')

# Adjust layout and colorbar
fig.colorbar(im, ax=axs, orientation='horizontal', fraction=0.05, pad=0.05)
plt.tight_layout()
plt.show()
