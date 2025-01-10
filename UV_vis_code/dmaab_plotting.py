from UV_VIS_base_line_adjustment import *

data = read_csv('Data/UV-DMAAB/365nm/DMAAB ACN 0min.Sample.Raw_fixed.csv')
data_1 = read_csv('Data/UV-DMAAB/365nm/DMAAB ACN 25min.Sample.Raw.csv')

#plotting
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'brown']

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(data['nm'], data['A'], label = 'No irradiation')
plt.plot(data_1['nm'], data_1['A'], label = 'After x amount of time')


# Highlighting the maximum value in `DMAB 3 min 254nm`
max_y_value = np.max(data['A'])
max_y_index = np.argmax(data['A'])
max_x_value = data['nm'][max_y_index]  # The corresponding x-value for max y

# Add vertical and horizontal reference lines
plt.axvline(max_x_value, color='black', linestyle='--', linewidth=1, label=f'Max at nm = {max_x_value:.2f}')
# plt.axvline(365, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='Exposed with 365nm light')
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
