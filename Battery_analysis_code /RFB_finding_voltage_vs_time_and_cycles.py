from data_extraction_code import *

time, voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number = result

#making a figure
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

#one of the x values is time

ax1.plot(time, voltage)
ax1.set_xlabel('time')

new_tick_location = cycle_number

def tick_function(x):
    V = 1/(1+x)
    return ["%.3f" % z for z in V]

ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(new_tick_location)
ax2.set_xticklabels(tick_function(new_tick_location))
ax2.set_xlabel(r"cycle number")
plt.show()