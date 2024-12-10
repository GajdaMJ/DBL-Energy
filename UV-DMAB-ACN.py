from UV_VIS_base_line_adjustment import *

import os


# Read the DMAB files with baseline correction applied
data_DMAB_3min_254nm = read_csv(r"Data/UV-DMAB/ACN/254nm/DMAB excited for 3 min (254).Sample.Raw.csv", 
                                base_line=False)

data_DMAB_5min_310nm = read_csv(r"Data/UV-DMAB/ACN/310nm/DMAB excited for 5 min (310).Sample.Raw.csv", 
                                base_line=False)

data_DMAB_10min_310nm = read_csv(r"Data/UV-DMAB/ACN/310nm/DMAB excited for 10 min (310).Sample.Raw.csv", 
                                 base_line=False)

data_DMAB_6min_365nm = read_csv(r"Data/UV-DMAB/ACN/365nm/DMAB excited for 6 min (365).Sample.Raw.csv", 
                                base_line=False)

data_DMAB_40min_365nm = read_csv(r"Data/UV-DMAB/ACN/365nm/DMAB excited for 40 min ( 365).Sample.Raw.csv", 
                                 base_line=False)

data_DMAB_385nm_peak = read_csv(r"Data/UV-DMAB/ACN/385nm/DMAB air_base (peak_over_1).Sample.Raw.csv", 
                                base_line=False)

data_DMAB_5min_385nm = read_csv(r"Data/UV-DMAB/ACN/385nm/DMAB air_base 5min 385nm.Sample.Raw.csv", 
                                base_line=False)

data_DMAB_30min_385nm = read_csv(r"Data/UV-DMAB/ACN/385nm/DMAB air_base 30min 385nm.Sample.Raw.csv", 
                                 base_line=False)

data_DMAB_45min_385nm = read_csv(r"Data/UV-DMAB/ACN/385nm/DMAB air_base 45min 385nm.Sample.Raw.csv", 
                                 base_line=False)



import matplotlib.pyplot as plt
import numpy as np

# Colors for DMAB datasets exposed to different wavelengths (using a gradient from red to purple)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'brown']

# Plotting
plt.figure(figsize=(12, 6))

# Plot the DMAB data for different wavelengths
plt.plot(data_DMAB_3min_254nm['nm'], data_DMAB_3min_254nm['A'], label='DMAB 3 min 254nm', color=colors[0])
plt.plot(data_DMAB_5min_310nm['nm'], data_DMAB_5min_310nm['A'], label='DMAB 5 min 310nm', color=colors[1])
plt.plot(data_DMAB_10min_310nm['nm'], data_DMAB_10min_310nm['A'], label='DMAB 10 min 310nm', color=colors[2])
plt.plot(data_DMAB_6min_365nm['nm'], data_DMAB_6min_365nm['A'], label='DMAB 6 min 365nm', color=colors[3])
plt.plot(data_DMAB_40min_365nm['nm'], data_DMAB_40min_365nm['A'], label='DMAB 40 min 365nm', color=colors[4])
plt.plot(data_DMAB_385nm_peak['nm'], data_DMAB_385nm_peak['A'], label='DMAB peak 385nm', color=colors[5])
plt.plot(data_DMAB_5min_385nm['nm'], data_DMAB_5min_385nm['A'], label='DMAB 5 min 385nm', color=colors[6])
plt.plot(data_DMAB_30min_385nm['nm'], data_DMAB_30min_385nm['A'], label='DMAB 30 min 385nm', color=colors[7])
plt.plot(data_DMAB_45min_385nm['nm'], data_DMAB_45min_385nm['A'], label='DMAB 45 min 385nm', color=colors[8])

# Highlighting the maximum value in `DMAB 3 min 254nm`
max_y_value = np.max(data_DMAB_3min_254nm['A'])
max_y_index = np.argmax(data_DMAB_3min_254nm['A'])
max_x_value = data_DMAB_3min_254nm['nm'][max_y_index]  # The corresponding x-value for max y

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
plt.suptitle('Absorbance vs. Wavelength for DMAB (Dimethoxyazobenzene) Samples', weight='bold')
plt.title('DMAB Samples Exposed to Various Light Conditions')
plt.legend()

# Show the plot
plt.show()
