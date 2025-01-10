from data_extraction_code import * 
result = data_extract("battery 3/OGO2024_flow battery 4_battery_6 mM ethoxyAB + MEEPT + 200 mM TBAPF6 in MeCN_C05.txt")
time, voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number = result

import matplotlib.pyplot as plt
# making the figure
fig = plt.figure()
ax1 = fig.add_subplot(111)

# plotting the data
ax1.plot(time[:1000], voltage[:1000], linewidth= 3)
ax1.set_ylim(0.75, 3)
ax1.set_xlim(335, 1170)

# setting axis labels with larger font size
ax1.set_ylabel("Voltage (V)", fontsize=28)
ax1.set_xlabel("Time (s)", fontsize=28)

ax2 = ax1.twiny()
ax2.set_xlabel("Cycle (#)", fontsize=28)

# fixing the cycles to times
ax2.set_xlim(335, 1170)
ax2.set_xticks([335, 642, 937])
ax2.set_xticklabels(['1', '2', '3'], fontsize=16)  # larger font size for tick labels

# enabling and customizing minor and major ticks
ax1.minorticks_on()
ax1.grid(which='major', linewidth=1.5)
ax1.grid(which='minor', linewidth=0.5)

# making tick marks and labels larger
ax1.tick_params(axis='both', which='major', length=15, width=3, labelsize=20)  # major ticks
ax1.tick_params(axis='both', which='minor', length=8, width=2)  # minor ticks
ax2.tick_params(axis='x', which='major', length=15, width=3, labelsize=20)  # twiny ticks

# Adding the (a) label to the top-left outside the plot
fig.text(0.05, 0.95, '(a)', fontsize=28, va='top', ha='left')

plt.show()
