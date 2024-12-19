from UV_VIS_base_line_adjustment import *

import os

# Specify the directory path

directory_path = r'Data\UV-aB\310nm'
# List all files in the directory
for file_name in os.listdir(directory_path):
    full_path = os.path.join(directory_path, file_name)
    if os.path.isfile(full_path):  # Ensure it's a file, not a folder
        print(file_name)



baseline_path = r"Data\UV-aB\365nmn\100% or 0 Absorbance Baseline.Correction.Raw.csv"
data_0 = read_csv(r"Data\UV-aB\\310nm\AB air_base.Sample.Raw.csv", base_line=True, base_line_path=r"Data\UV-aB\\310nm\AC air_base.Sample.Raw.csv")
data_5min = read_csv(r"Data\UV-aB\365nmn\aB 50uM 5min 365nm.Sample.Raw.csv", base_line=True, base_line_path=baseline_path)
data_10min = read_csv(r"Data\UV-aB\365nmn\aB 50uM 10min 365nm.Sample.Raw.csv", base_line=True, base_line_path=baseline_path)
data_15min = read_csv(r"Data\UV-aB\365nmn\aB 50uM 15min 365nm.Sample.Raw.csv", base_line=True, base_line_path=baseline_path)
data_45min = read_csv(r"Data\UV-aB\365nmn\aB 50uM 45min 365nm.Sample.Raw.csv", base_line=True, base_line_path=baseline_path)
data_60min_fixed = read_csv(r"Data\UV-aB\365nmn\aB 50um 60min 365nm.Sample.Raw_fixed.csv", base_line=True, base_line_path=baseline_path)
data_60min = read_csv(r"Data\UV-aB\365nmn\aB 50um 60min 365nm.Sample.Raw.csv", base_line=True, base_line_path=baseline_path)



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
# plt.plot(data_20min['nm'], data_20min['A'], label='20 min', color=colors[4]) # Blue
plt.plot(data_45min['nm'], data_45min['A'], label='45 min', color=colors[5]) # Indigo
plt.plot(data_60min['nm'], data_60min['A'], label='60 min', color=colors[6]) # Purple

# Highlighting maximum value in `


plt.axvline(365, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='Compounds exposed with 310nm light')
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



