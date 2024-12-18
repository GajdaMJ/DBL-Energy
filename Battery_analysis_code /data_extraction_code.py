import numpy as np
import matplotlib.pyplot as plt 

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


if __name__ == 'main':
    data_1 = read_csv("Data/RFB/OGO2024_flow battery 2_cycling_6 mM ethoxyAB + MEEPT + 200 mM TBAPF6 in MeCN_C05.txt")
    print(data_1)