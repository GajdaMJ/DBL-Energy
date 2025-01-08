from data_extraction_code import * 
result = data_extract("battery 3/OGO2024_flow battery 4_battery_6 mM ethoxyAB + MEEPT + 200 mM TBAPF6 in MeCN_C05.txt")
time, voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number = result

import matplotlib.pyplot as plt
# making the figure
fig = plt.figure()
ax1 = fig.add_subplot(111)

# plotting the data
ax1.plot(time[:1000], voltage[:1000])
ax1.set_ylim(0.75, 3)
ax1.set_xlim(280, 1215)

# setting axis labels with larger font size
ax1.set_ylabel("Voltage [V]", weight='bold', fontsize=18)
ax1.set_xlabel("Time [s]", weight='bold', fontsize=18)

ax2 = ax1.twiny()
ax2.set_xlabel("Cycle Number", weight='bold', fontsize=18)

# fixing the cycles to times
ax2.set_xlim(290, 1215)
ax2.set_xticks([280, 634, 931])
ax2.set_xticklabels(['1', '2', '3'], fontsize=16)  # larger font size for tick labels

# enabling and customizing minor and major ticks
ax1.minorticks_on()
ax1.grid(which='major', linewidth=1.5)
ax1.grid(which='minor', linewidth=0.5)

# making tick marks and labels larger
ax1.tick_params(axis='both', which='major', length=12, width=2, labelsize=16)  # major ticks
ax1.tick_params(axis='both', which='minor', length=6, width=1)  # minor ticks
ax2.tick_params(axis='x', which='major', length=12, width=2, labelsize=16)  # twiny ticks

plt.show()
