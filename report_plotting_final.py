#this file will plot AB and DEAB (to show the difference between a compound which will fully convert and one which does not fully convert)
import matplotlib.pyplot as plt
import numpy as np
from UV_VIS_base_line_adjustment import *

# Load AB datasets
# baseline_path_ab = r"Data/UV-aB/365nmn/100% or 0 Absorbance Baseline.Correction.Raw.csv"
baseline_path_ab = r"Data/UV-aB/365nmn/100% or 0 Absorbance Baseline.Correction.Raw.csv"
data_ab_5min = read_csv(r"Data/UV-aB/365nmn/aB 50uM 5min 365nm.Sample.Raw.csv", base_line=False, base_line_path=baseline_path_ab)
data_ab_10min = read_csv(r"Data/UV-aB/365nmn/aB 50uM 10min 365nm.Sample.Raw.csv", base_line=False, base_line_path=baseline_path_ab)
data_ab_15min = read_csv(r"Data/UV-aB/365nmn/aB 50uM 15min 365nm.Sample.Raw.csv", base_line=False, base_line_path=baseline_path_ab)
data_ab_45min = read_csv(r"Data/UV-aB/365nmn/aB 50uM 45min 365nm.Sample.Raw.csv", base_line=False, base_line_path=baseline_path_ab)
data_ab_60min = read_csv(r"Data/UV-aB/365nmn/aB 50um 60min 365nm.Sample.Raw.csv", base_line=False, base_line_path=baseline_path_ab)

# Load DEAB datasets
baseline_path_deab = r"Data/UV-VIS_new/measurements 22-11-24/ACN solution.Sample.Raw.csv"
data_deab_nonexited = read_csv(r"/Users/oliverlohr/Documents/DBL-Energy/Data/UV-DEAB/DEAM/DEAM non excited.Sample.Raw.csv", base_line=True, base_line_path=baseline_path_deab)
data_deab_1min = read_csv(r"/Users/oliverlohr/Documents/DBL-Energy/Data/UV-DEAB/DEAM/DEAM 1 min.Sample.Raw.csv", base_line=True, base_line_path=baseline_path_deab)
#data_deab_10min = read_csv(r"Data\UV-DMAB\ACN_365nm\DMAB ACN 10min 365nm.Sample.Raw.csv", base_line=False)

# Plotting AB datasets
plt.figure(figsize=(10, 6))
plt.plot(data_ab_5min['nm'], data_ab_5min['A'], label='AB 5 min', color='orange', linestyle='-', linewidth=2)  # Blue, straight line
plt.plot(data_ab_10min['nm'], data_ab_10min['A'], label='AB 10 min', color='green', linestyle='-', linewidth=2)  # Orange, straight line
plt.plot(data_ab_15min['nm'], data_ab_15min['A'], label='AB 15 min', color='slategrey', linestyle='-', linewidth=2)  # Green, straight line
plt.plot(data_ab_45min['nm'], data_ab_45min['A'], label='AB 45 min', color='dodgerblue', linestyle='-', linewidth=2)  # Red, straight line
# plt.plot(data_ab_60min['nm'], data_ab_60min['A'], label='AB 60 min', color='#9467bd', linestyle='-', linewidth=2)  # Purple, straight line

# Plotting DMAB datasets
plt.plot(data_deab_nonexited['nm'], data_deab_nonexited['A'], label='DMAB Non-excited', color='darkred', linestyle='-.', linewidth=2)  # Brown, dashed-dot
plt.plot(data_deab_1min['nm'], data_deab_1min['A'], label='DMAB 5 min', color='deeppink', linestyle='-.', linewidth=2)  # Pink, dashed-dot
# plt.plot(data_dmab_10min['nm'], data_dmab_10min['A'], label='DMAB 10 min', color='#7f7f7f', linestyle='-.', linewidth=2)  # Gray, dashed-dot

# Highlight 365 nm line
plt.axvline(365, color='black', linestyle='-.', linewidth=1, alpha=0.7, label='365 nm Light')
plt.axhline(0, color='black', linewidth=0.5)
# Formatting
plt.xlabel('Wavelength (nm)', fontsize=28)
plt.ylabel('Absorbance (A)', fontsize=28)
plt.xticks(np.arange(300, 601, 50), fontsize=12)
plt.yticks(np.arange(0, 1.1, 0.2), fontsize=12)
plt.ylim(0, 1)
plt.xlim(290, 600)
plt.grid(True, linestyle='--', alpha=0.5)

# Legend inside the plot (top-right corner)
plt.legend(fontsize=10, loc='upper right', frameon=False)

# Tight layout for professional appearance
plt.tight_layout()

# Save the plot for high-quality output
plt.savefig('UV_Vis_Absorbance_Plot_report.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
