from UV_VIS_base_line_adjustment import *

data = read_csv('Data/UV-aB/310nm/AB air_base.Sample.Raw.csv')
data_1 = read_csv('Data/UV-aB/310nm/Ab air_base 60min 310nm.Sample.Raw.csv')

plt.plot(data['nm'], data['A'], label = 'No irradiation')
plt.plot(data_1['nm'], data_1['A'], label = 'After x amount of time')

plt.legend()
plt.show()