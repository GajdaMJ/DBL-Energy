import numpy as np
import matplotlib.pyplot as plt

def data_extract(file_path):
    # Skip the first 91 lines (metadata)
    # skip_lines = 91 #ignore this since there are no headers in this document 
    columns_to_extract = (0, 1, 2, 3, 4, 5, 6)  # Indices of the columns to extract

    data = np.genfromtxt(
        file_path,
        usecols=columns_to_extract,
        delimiter=";",  # Auto-detect, switch to '\t' if required
        invalid_raise=False,  # Ignore lines with errors
        encoding='ISO-8859-1'
    )
    # Extract columns
    time = data[:, 0]
    voltage = data[:, 1]
    energy_charge = data[:, 2]
    energy_discharge = data[:, 3]
    q_discharge = data[:, 4]
    q_charge = data[:, 5]
    cycle_number = data[:, 6]

    return time, voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number



results = data_extract("Data/RFB/OGO2024_flow battery 3_cycling_6 mM ethoxyAB + DBBB + 200 mM TBAPF6 in MeCN_02_CV_C05.txt")
time, voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number = results

plt.plot(time[:1000], voltage[:1000])
plt.show()


# # making the figure
# fig = plt.figure()
# ax1 = fig.add_subplot(111)

# # plotting the data
# ax1.plot(time[:1000], voltage[:1000])
# ax1.set_ylim(0.75, 4)
# ax1.set_xlim(0, 1215)

# # setting axis labels with larger font size
# ax1.set_ylabel("Voltage [V]", weight='bold', fontsize=18)
# ax1.set_xlabel("Time [s]", weight='bold', fontsize=18)

# ax2 = ax1.twiny()
# ax2.set_xlabel("Cycle Number", weight='bold', fontsize=18)

# # fixing the cycles to times
# ax2.set_xlim(0, 1215)
# ax2.set_xticks([8, 634, 931])
# ax2.set_xticklabels(['1', '2', '3'], fontsize=16)  # larger font size for tick labels

# # enabling and customizing minor and major ticks
# ax1.minorticks_on()
# ax1.grid(which='major', linewidth=1.5)
# ax1.grid(which='minor', linewidth=0.5)

# # making tick marks and labels larger
# ax1.tick_params(axis='both', which='major', length=12, width=2, labelsize=16)  # major ticks
# ax1.tick_params(axis='both', which='minor', length=6, width=1)  # minor ticks
# ax2.tick_params(axis='x', which='major', length=12, width=2, labelsize=16)  # twiny ticks

# plt.show()
