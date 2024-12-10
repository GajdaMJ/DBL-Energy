from UV_VIS_base_line_adjustment import *

import os

# Specify the directory path

directory_path = r'Data\UV-aB\310nm'
# List all files in the directory
for file_name in os.listdir(directory_path):
    full_path = os.path.join(directory_path, file_name)
    if os.path.isfile(full_path):  # Ensure it's a file, not a folder
        print(file_name)



data_0 = read_csv(r"Data\UV-aB\\310nm\AB air_base.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")
data_10min = read_csv(r"Data\UV-aB\\310nm\AB air_base 10min 310nm.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")
data_15min = read_csv(r"Data\UV-aB\\310nm\AB air_base 15min 310nm.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")
data_20min = read_csv(r"Data\UV-aB\\310nm\AB air_base 20min 310nm.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")
data_45min = read_csv(r"Data\UV-aB\\310nm\AB air_base 45min 310nm.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")
data_5min = read_csv(r"Data\UV-aB\\310nm\AB air_base 5min 310nm.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")
data_60min = read_csv(r"Data\UV-aB\\310nm\Ab air_base 60min 310nm.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")



import matplotlib.pyplot as plt
import numpy as np

# Updated colors to ensure coherent transition from red to blue
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']  # Adjusted for smooth transition

# Plotting each dataset with matching labels and colors
plt.figure(figsize=(12, 6))

plt.plot(data_0['nm'], data_0['A'], label='0 min', color=colors[0])       # Red
plt.plot(data_5min['nm'], data_5min['A'], label='5 min', color=colors[1]) # Orange
plt.plot(data_10min['nm'], data_10min['A'], label='10 min', color=colors[2]) # Yellow
plt.plot(data_15min['nm'], data_15min['A'], label='15 min', color=colors[3]) # Green
plt.plot(data_20min['nm'], data_20min['A'], label='20 min', color=colors[4]) # Blue
plt.plot(data_45min['nm'], data_45min['A'], label='45 min', color=colors[5]) # Indigo
plt.plot(data_60min['nm'], data_60min['A'], label='60 min', color=colors[6]) # Purple

# Highlighting maximum value in `data_0`
max_y_value = np.max(data_0['A'])
max_y_index = np.argmax(data_0['A'])
max_x_value = data_0['nm'][max_y_index]  # The corresponding x-value for max y

# Add vertical and horizontal reference lines
plt.axvline(max_x_value, color='black', linestyle='--', linewidth=1, label=f'Max at nm = {max_x_value:.2f}')
plt.axvline(310, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='Compounds exposed with 310nm light')
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Set plot limits
plt.xlim(275, 550)
plt.ylim(-0.5, 1.1)

# Add labels, title, and legend
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (A)')
plt.suptitle('Absorbance vs. Wavelength for Azobenzene Sample', weight='bold')
plt.title('Samples Exposed to 310nm Light')
plt.legend()

# Show the plot
plt.show()



