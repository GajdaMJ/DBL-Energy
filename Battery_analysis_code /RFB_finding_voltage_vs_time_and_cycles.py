# from data_extraction_code import * 

# time,voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number = result

# import matplotlib.pyplot as plt
# #making the figure
# fig = plt.figure()
# ax1 = fig.add_subplot(111)

# #plotting the data
# ax1.plot(time[:1000], voltage[:1000])
# ax1.set_ylim(0.75,3)
# ax1.set_xlim(0,1700)

# ax1.set_ylabel("Voltage [V]", weight = 'bold')
# ax1.set_xlabel("Time [s]", weight = 'bold')

# ax2 = ax1.twiny()
# ax2.set_xlabel("Cycle Number", weight = 'bold')

# #fixing the cycles to times
# ax2.set_xlim(0,1700)
# # ax2.set_xticks([297, 634, 931])
# ax2.set_xticks([12, 297, 634, 931, 1215, 1522])
# # ax2.set_xticklabels(['1', '2', '3'])
# ax2.set_xticklabels(['0', '1', '2', '3', '4', '5'])

# ax1.minorticks_on()
# ax1.grid(which= 'major', linewidth = 1)
# ax1.grid(which= 'minor', linewidth = 0.2)

# plt.show()




from data_extraction_code import * 

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
ax1.set_ylabel("Voltage [V]", weight='bold', fontsize=14)
ax1.set_xlabel("Time [s]", weight='bold', fontsize=14)

ax2 = ax1.twiny()
ax2.set_xlabel("Cycle Number", weight='bold', fontsize=14)

# fixing the cycles to times
ax2.set_xlim(290, 1215)
ax2.set_xticks([280, 634, 931])
ax2.set_xticklabels(['1', '2', '3'], fontsize=12)  # adjust tick label font size here

# enabling and customizing minor and major ticks
ax1.minorticks_on()
ax1.grid(which='major', linewidth=1)
ax1.grid(which='minor', linewidth=0.2)

# make tick marks larger
ax1.tick_params(axis='both', which='major', length=10, width=1.5, labelsize=12)  # major ticks
ax1.tick_params(axis='both', which='minor', length=5, width=1)  # minor ticks
ax2.tick_params(axis='x', which='major', length=10, width=1.5, labelsize=12)  # twiny ticks

plt.show()
