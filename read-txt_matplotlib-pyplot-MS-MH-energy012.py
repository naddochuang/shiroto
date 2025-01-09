import matplotlib.pyplot as plt

# Function to read the input file and extract data
def read_input_file(file_path):
    data = {}
    current_key = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("energy"):
                current_key = line
                data[current_key] = {'mz': [], 'intensity': []}
            else:
                mz, intensity = map(float, line.split())
                data[current_key]['mz'].append(mz)
                data[current_key]['intensity'].append(intensity)
    return data

# Function to plot the graph
def plot_graph(data):
    for key, values in data.items():
        plt.figure(figsize=(10, 6))
        for mz, intensity in zip(values['mz'], values['intensity']):
            plt.vlines(mz, 0, intensity, colors='b', linestyles='-', lw=2)
        plt.ylim(0, 100)
        plt.xlim(0, max(max(values['mz']) for values in data.values()))
        plt.xlabel('m/z')
        plt.ylabel('Intensity')
        plt.title(f'Intensity vs. m/z Graph - {key}')
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.show()

# Main function
def main():
    input_file = 'input_data-energy012.txt'  # Replace with your input file path
    data = read_input_file(input_file)
    plot_graph(data)

if __name__ == '__main__':
    main()
