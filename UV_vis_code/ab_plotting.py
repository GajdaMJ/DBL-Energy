from UV_VIS_base_line_adjustment import *

data = read_csv('Data/UV-aB/310nm/AB air_base.Sample.Raw.csv', base_line= True, base_line_path= "Data/UV-aB/310nm/AC air_base.Sample.Raw.csv")
data_1 = read_csv('Data/UV-aB/365nmn/aB 50um 60min 365nm.Sample.Raw.csv')

#plotting
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'brown']

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(data['nm'], data['A'], label = 'No irradiation of AB')
plt.plot(data_1['nm'], data_1['A'], label = 'After irradiation of AB')


# Highlight 365 nm line
# plt.axvline(365, color='black', linestyle='-.', linewidth=1, alpha=0.7, label='365 nm Light')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
# Formatting
plt.xlabel('Wavelength (nm)', fontsize=14, fontweight='bold')
plt.ylabel('Absorbance (A)', fontsize=14, fontweight='bold')
plt.xticks(np.arange(250, 601, 50), fontsize=12)
plt.yticks(np.arange(-0.2, 1.1, 0.2), fontsize=12)
plt.ylim(0, 1)
plt.xlim(290, 600)
plt.grid(True, linestyle='--', alpha=0.5)

# Legend inside the plot (top-right corner)
plt.legend(fontsize=20, loc='upper right', frameon=False)

# Tight layout for professional appearance
plt.tight_layout()

# Save the plot for high-quality output
plt.savefig('UV_Vis_Absorbance_Plot_AB_Presentation.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
