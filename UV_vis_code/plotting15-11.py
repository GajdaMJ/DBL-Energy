from UV_VIS_base_line_adjustment import *

data = read_csv('UV_vis_code/thing.Raw.csv')

plt.plot(data['nm'], data['A'])

plt.show()