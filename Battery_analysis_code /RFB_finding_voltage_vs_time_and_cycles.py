from data_extraction_code import *

#### modifying the data to find the efficiency
time, voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number = result

#making a figure
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()


