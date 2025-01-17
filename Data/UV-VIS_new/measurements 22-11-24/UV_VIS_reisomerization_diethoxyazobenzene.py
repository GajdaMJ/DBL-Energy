import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def read_csv(path, base_line=False, base_line_path=None):
    def process_file(input_file, output_file):
        # Process the file to fix delimiters and remove commas in numbers
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for i, line in enumerate(infile):
                # For the first line, replace the first comma with a semicolon
                if i == 0:
                    line = line.replace(",", ";", 1)
                    line = line.replace(' ', '', 1)
                else:
                    # For other lines, replace the second comma with a semicolon
                    parts = line.split(",")
                    if len(parts) > 2:
                        line = ",".join(parts[:2]) + ";" + ",".join(parts[2:])
                        line = line.replace(' ', '', 1)
                        line = line.replace(',', '.', 2)
                outfile.write(line)

    # Process baseline file if required
    if base_line:
        output_baseline_file = base_line_path.replace('.csv', '_fixed.csv')
        process_file(base_line_path, output_baseline_file)
        data_base = np.genfromtxt(output_baseline_file, delimiter=";", dtype=None, names=True, encoding='ISO-8859-1')

    # Process the input file
    output_file = path.replace('.csv', '_fixed.csv')
    process_file(path, output_file)
    data = np.genfromtxt(output_file, delimiter=";", dtype=None, names=True, encoding='ISO-8859-1')

    if base_line:
        # Ensure the data lengths match
        if len(data) != len(data_base):
            raise ValueError("Data and baseline files have mismatched lengths.")

        # Subtract the baseline from the data for each field
        adjusted_data = np.zeros_like(data)
        adjusted_data['nm'] = data['nm']
        adjusted_data['A'] = data['A'] - data_base['A']
        return adjusted_data
    else:
        return data


if __name__ == '__main__':
    data_0 = read_csv('air base sample.csv',base_line = True, base_line_path="ACN solution.Sample.Raw.csv")
    data_1min = read_csv("DEAM 1 min.Sample.Raw.csv",base_line = True, base_line_path="ACN solution.Sample.Raw.csv")
    data_5min = read_csv("DEAM 5 min.Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_10min = read_csv("DEAM 10 min.Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_15min = read_csv("DEAM 15 min.Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_25min = read_csv("DEAM 25 min.Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_35min = read_csv("DEAM 35 min.Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_45min = read_csv("DEAM 45 min.Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_60min = read_csv("DEAM 60 min.Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_90min = read_csv("DEAM 90 min (1220).Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    data_160min = read_csv("DEAM 160 min (1330).Sample.Raw.csv", base_line = True, base_line_path = "ACN solution.Sample.Raw.csv")
    
    plt.plot(data_1min['nm'], data_1min['A'], label='1 min', color='#ff7f0e')
    plt.plot(data_5min['nm'], data_5min['A'], label='5 min', color='#2ca02c')
    plt.plot(data_10min['nm'], data_10min['A'], label='10 min', color='#d62728')
    plt.plot(data_15min['nm'], data_15min['A'], label='15 min', color='#9467bd')
    plt.plot(data_25min['nm'], data_25min['A'], label='25 min', color='#8c564b')
    plt.plot(data_35min['nm'], data_35min['A'], label='35 min', color='#e377c2')
    plt.plot(data_45min['nm'], data_45min['A'], label='45 min', color='#7f7f7f')
    plt.plot(data_60min['nm'], data_60min['A'], label='60 min', color='#bcbd22')

    plt.axvline(365, color='black', linestyle='-.', linewidth=0.5, alpha=0.5, label='Compounds exposed with 365nm light')
    # Add labels and title
    plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Horizontal line at y=0
    plt.xlim(275, 550)  # Set x-axis limits
    plt.ylim(0, 0.4)  # Set y-axis limits
    plt.xlabel('Wavelength (nm)')  # Label x-axis
    plt.ylabel('Absorbance (A)')  # Label y-axis
    plt.suptitle('Absorbance vs. Wavelength for Azobenzene Samples', weight='bold')  # Title of the plot
    # Add legend to identify each line
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

    ## Plotting time vs abs_max

    time = [0,5,10,15,45,60]
    # Collect maximum absorbance values at each time point
    abs_max = [np.max(data_0["A"])]#, np.max(data_5min["A"]), np.max(data_10min["A"]),np.max(data_15min["A"]), np.max(data_45min["A"]), np.max(data_60min["A"])]

    def exponential_decay(t, A, B, C):
        return A * np.exp(-B * t) + C

    # Fit the exponential decay curve to the time vs abs_max data
    params, covariance = curve_fit(exponential_decay, time, abs_max, p0=[1, 0.1, 0])

    # Extract the fitted parameters
    A_fit, B_fit, C_fit = params

    # Generate fitted data points
    time_fine = np.linspace(min(time), max(time), 1000)  # Fine time points for a smooth curve
    abs_max_fit = exponential_decay(time_fine, A_fit, B_fit, C_fit)

    # Plot Time vs Maximum Absorbance
    plt.figure(figsize=(8, 6))
    plt.plot(time, abs_max, marker='o', linestyle='-', color='b', label='Max Absorbance')
    plt.plot(time_fine, abs_max_fit, linestyle='--', color='r', label='Exponential Fit')

    # Labels and Title
    plt.xlabel('Time (min)')
    plt.ylabel('Maximum Absorbance (A)')
    plt.title('Maximum Absorbance with Exponential Decay Fit')
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

    # Print fitted parameters
    print(f"Fitted parameters: A = {A_fit:.4f}, B = {B_fit:.4f}, C = {C_fit:.4f}")