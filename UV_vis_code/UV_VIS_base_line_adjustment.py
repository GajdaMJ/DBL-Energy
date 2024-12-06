import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def read_csv(path, base_line=False, base_line_path=None):
    def process_file(input_file, output_file):
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for i, line in enumerate(infile):
                if i == 0:
                    line = line.replace(",", ";", 1).replace(' ', '', 1)
                else:
                    parts = line.split(",")
                    if len(parts) > 2:
                        line = ",".join(parts[:2]) + ";" + ",".join(parts[2:])
                        line = line.replace(' ', '', 1).replace(',', '.', 2)
                outfile.write(line)

    if base_line:
        output_baseline_file = base_line_path.replace('.csv', '_fixed.csv')
        process_file(base_line_path, output_baseline_file)
        data_base = np.genfromtxt(output_baseline_file, delimiter=";", dtype=None, names=True, encoding='ISO-8859-1')

    output_file = path.replace('.csv', '_fixed.csv')
    process_file(path, output_file)
    data = np.genfromtxt(output_file, delimiter=";", dtype=None, names=True, encoding='ISO-8859-1')

    if base_line:
        if len(data) != len(data_base):
            raise ValueError("Data and baseline files have mismatched lengths.")
        adjusted_data = np.zeros_like(data)
        adjusted_data['nm'] = data['nm']
        adjusted_data['A'] = data['A'] - data_base['A']
        return adjusted_data
    else:
        return data


if __name__ == '__main__':
    data_0 = read_csv("Data/uv_vis/20_11_airbase/DEAB air_base.Sample.Raw.csv", base_line=True, base_line_path="Data/uv_vis/20_11_airbase/AC_base.Sample.Raw.csv")
    data_5min = read_csv("Data/uv_vis/20_11_airbase/DEAB air_base long_time 365nm.Sample.Raw.csv", base_line=True, base_line_path="Data/uv_vis/20_11_airbase/AC_base.Sample.Raw.csv")

    plt.plot(data_0['nm'], data_0['A'], label='0 min', color='blue')
    plt.plot(data_5min['nm'], data_5min['A'], label='5 min', color='green')

    max_y_value = np.max(data_0['A'])
    max_y_index = np.argmax(data_0['A'])
    max_x_value = data_0['nm'][max_y_index]

    max_x_index = np.argmin(np.abs(data_5min['nm'] - max_x_value))
    A_2 = data_5min['A'][max_x_index]
    percent_trans = (A_2 / max_y_value) * 100  # Convert to percentage
    print(f"Percent Trans = {percent_trans:.2f}%")

    plt.axvline(max_x_value, color='black', linestyle='--', linewidth=1, label=f'Max at nm = {max_x_value:.2f}')
    plt.axvline(365, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='365nm Light Exposure')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.xlim(275, 800)
    plt.ylim(-0.5, 1.1)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance (A)')
    plt.suptitle('Absorbance vs. Wavelength for Azobenzene Samples', weight='bold')
    plt.legend()
    plt.show()

    time = [0, 5, 10, 15, 45, 60]
    abs_max = [
        np.max(data_0["A"]), 
        np.max(data_5min["A"]),
        0.8, 0.7, 0.6, 0.5  # Replace placeholders with real data as needed
    ]

    def exponential_decay(t, A, B, C):
        return A * np.exp(-B * t) + C

    params, covariance = curve_fit(exponential_decay, time, abs_max, p0=[1, 0.1, 0])
    A_fit, B_fit, C_fit = params

    time_fine = np.linspace(min(time), max(time), 1000)
    abs_max_fit = exponential_decay(time_fine, A_fit, B_fit, C_fit)

    plt.figure(figsize=(8, 6))
    plt.plot(time, abs_max, marker='o', linestyle='-', color='b', label='Max Absorbance')
    plt.plot(time_fine, abs_max_fit, linestyle='--', color='r', label='Exponential Fit')
    plt.xlabel('Time (min)')
    plt.ylabel('Maximum Absorbance (A)')
    plt.title('Maximum Absorbance with Exponential Decay Fit')
    plt.legend()
    plt.show()

    print(f"Fitted parameters: A = {A_fit:.4f}, B = {B_fit:.4f}, C = {C_fit:.4f}")
