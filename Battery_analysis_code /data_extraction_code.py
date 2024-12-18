import numpy as np
import matplotlib.pyplot as plt

file_path = 'Data/RFB/OGO2024_flow battery 2_cycling_6 mM ethoxyAB + MEEPT + 200 mM TBAPF6 in MeCN_C05.txt'

def data_extract(file_path):
    # Skip the first 91 lines (metadata)
    skip_lines = 91
    columns_to_extract = (0, 1, 2, 3, 4, 5, 6)  # Indices of the columns to extract

    data = np.genfromtxt(
        file_path,
        skip_header=skip_lines,
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


# Call the function and display the results
result = data_extract(file_path)

if result is not None:
    time, voltage, energy_charge, energy_discharge, q_discharge, q_charge, cycle_number = result
    print("Time (s):", time[:100])
#     # print("Voltage (V):", voltage)
#     # print("Energy Charge (W.h):", energy_charge)
#     # print("Energy Discharge (W.h):", energy_discharge)
#     # print("Q Discharge (mA.h):", q_discharge)
#     # print("Q Charge (mA.h):", q_charge)
#     # print("Cycle Number:", cycle_number)

plt.plot(time[:1000], voltage[:1000])
plt.show()






