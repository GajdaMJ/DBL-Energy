from UV_VIS_base_line_adjustment import *

import os

# Specify the directory path

directory_path = r'Data\UV-aB\310nm'
# List all files in the directory
for file_name in os.listdir(directory_path):
    full_path = os.path.join(directory_path, file_name)
    if os.path.isfile(full_path):  # Ensure it's a file, not a folder
        print(file_name)


# Read the new files for DEAB (diethoxyazobenzene) with correct file paths
data_DEAB_5min = read_csv(r"Data\\UV-DEAB\\PC\\365nm Light\\DEAB 5 min 365 nm.Sample.Raw.csv", base_line=True  , base_line_path=r'Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv')
data_DEAB_10min = read_csv(r"Data\\UV-DEAB\\PC\\365nm Light\\DEAB 10 min 365 nm.Sample.Raw.csv", base_line=True, base_line_path=r'Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv')


import matplotlib.pyplot as plt
import numpy as np

# Colors for DEAB datasets
colors = ['red', 'blue']  # Assign red for 5 min and blue for 10 min

# Plotting
plt.figure(figsize=(12, 6))

# Plot the DEAB data
plt.plot(data_DEAB_5min['nm'], data_DEAB_5min['A'], label='DEAB 5 min', color=colors[0])
plt.plot(data_DEAB_10min['nm'], data_DEAB_10min['A'], label='DEAB 10 min', color=colors[1])

# Highlighting the maximum value in `DEAB 5 min`
max_y_value = np.max(data_DEAB_5min['A'])
max_y_index = np.argmax(data_DEAB_5min['A'])
max_x_value = data_DEAB_5min['nm'][max_y_index]  # The corresponding x-value for max y

# Add vertical and horizontal reference lines
plt.axvline(max_x_value, color='black', linestyle='--', linewidth=1, label=f'Max at nm = {max_x_value:.2f}')
plt.axvline(365, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='Exposed with 365nm light')
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Set plot limits
plt.xlim(275, 800)
plt.ylim(-0.5, 1.1)

# Add labels, title, and legend
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (A)')
plt.suptitle('Absorbance vs. Wavelength for DEAB (Diethoxyazobenzene) Samples', weight='bold')
plt.title('Samples Exposed to 365nm Light')
plt.legend()

# Show the plot
plt.show()




# Read the new files for DEAB in the dark
data_DEAB_15min_dark = read_csv(r"Data\\UV-DEAB\\PC\\Dark\\DEAB 15 min in the dark.Sample.Raw.csv", base_line=True, base_line_path=r'Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv')
data_DEAB_30min_dark = read_csv(r"Data\\UV-DEAB\\PC\\Dark\\DEAB 30 min in the dark.Sample.Raw.csv", base_line=True, base_line_path=r'Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv')

import matplotlib.pyplot as plt
import numpy as np

# Colors for DEAB datasets in the dark
colors = ['green', 'purple']  # Assign green for 15 min and purple for 30 min

# Plotting
plt.figure(figsize=(12, 6))

# Plot the DEAB in the dark data
plt.plot(data_DEAB_15min_dark['nm'], data_DEAB_15min_dark['A'], label='DEAB 15 min in the dark', color=colors[0])
plt.plot(data_DEAB_30min_dark['nm'], data_DEAB_30min_dark['A'], label='DEAB 30 min in the dark', color=colors[1])

# Highlighting the maximum value in `DEAB 15 min in the dark`
max_y_value = np.max(data_DEAB_15min_dark['A'])
max_y_index = np.argmax(data_DEAB_15min_dark['A'])
max_x_value = data_DEAB_15min_dark['nm'][max_y_index]  # The corresponding x-value for max y

# Add vertical and horizontal reference lines
plt.axvline(max_x_value, color='black', linestyle='--', linewidth=1, label=f'Max at nm = {max_x_value:.2f}')
plt.axvline(365, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='Exposed with 365nm light')
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Set plot limits
plt.xlim(275, 800)
plt.ylim(-0.5, 1.1)

# Add labels, title, and legend
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (A)')
plt.suptitle('Absorbance vs. Wavelength for DEAB (Diethoxyazobenzene) Samples', weight='bold')
plt.title('Samples in the Dark')
plt.legend()

# Show the plot
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Colors for DEAB datasets exposed to visible light
colors = ['yellow', 'green', 'blue', 'indigo', 'violet']  # Assign colors to different time points

# Plotting
plt.figure(figsize=(12, 6))
# Read the new files for DEAB exposed to visible light with baseline correction
data_DEAB_2min_vis = read_csv(r"Data\\UV-DEAB\\PC\\Sunlight\\DEAB 2 min vis light.Sample.Raw.csv", 
                              base_line=True, 
                              base_line_path=r"Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv")

data_DEAB_5min_vis = read_csv(r"Data\\UV-DEAB\\PC\\Sunlight\\DEAB 5 min vis light.Sample.Raw.csv", 
                              base_line=True, 
                              base_line_path=r"Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv")

data_DEAB_10min_vis = read_csv(r"Data\\UV-DEAB\\PC\\Sunlight\\DEAB 10 min vis light.Sample.Raw.csv", 
                               base_line=True, 
                               base_line_path=r"Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv")

data_DEAB_15min_vis = read_csv(r"Data\\UV-DEAB\\PC\\Sunlight\\DEAB 15 mins vis light.Sample.Raw.csv", 
                               base_line=True, 
                               base_line_path=r"Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv")

data_DEAB_20min_vis = read_csv(r"Data\\UV-DEAB\\PC\\Sunlight\\DEAB 20 min vis light.Sample.Raw.csv", 
                               base_line=True, 
                               base_line_path=r"Data\\UV-DEAB\\PC\\365nm Light\\PC baseline.Sample.Raw.csv")

# Plot the DEAB data exposed to visible light
plt.plot(data_DEAB_2min_vis['nm'], data_DEAB_2min_vis['A'], label='DEAB 2 min visible light', color=colors[0])
plt.plot(data_DEAB_5min_vis['nm'], data_DEAB_5min_vis['A'], label='DEAB 5 min visible light', color=colors[1])
plt.plot(data_DEAB_10min_vis['nm'], data_DEAB_10min_vis['A'], label='DEAB 10 min visible light', color=colors[2])
plt.plot(data_DEAB_15min_vis['nm'], data_DEAB_15min_vis['A'], label='DEAB 15 min visible light', color=colors[3])
plt.plot(data_DEAB_20min_vis['nm'], data_DEAB_20min_vis['A'], label='DEAB 20 min visible light', color=colors[4])

# Highlighting the maximum value in `DEAB 2 min visible light`
max_y_value = np.max(data_DEAB_2min_vis['A'])
max_y_index = np.argmax(data_DEAB_2min_vis['A'])
max_x_value = data_DEAB_2min_vis['nm'][max_y_index]  # The corresponding x-value for max y

# Add vertical and horizontal reference lines
plt.axvline(max_x_value, color='black', linestyle='--', linewidth=1, label=f'Max at nm = {max_x_value:.2f}')
plt.axvline(365, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='Exposed with 365nm light')
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Set plot limits
plt.xlim(275, 800)
plt.ylim(-0.5, 1.1)

# Add labels, title, and legend
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (A)')
plt.suptitle('Absorbance vs. Wavelength for DEAB (Diethoxyazobenzene) Samples', weight='bold')
plt.title('Samples Exposed to Visible Light')
plt.legend()

# Show the plot
plt.show()
