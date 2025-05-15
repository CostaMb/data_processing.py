import sys

def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file if line.strip()]
            if len(data) < 3:
                raise ValueError("Insufficient data. At least 3 values required.")
            return data
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def calculate(data):
    sum_data = sum(data)
    avg_data = sum_data / len(data)
    return sum_data, avg_data

def write_results(results, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write(f"Sum of data: {results[0]}\n")
            file.write(f"Average of data: {results[1]}\n")
    except Exception as e:
        print(f"Error writing results: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python data_processing.py input.txt output.txt")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data = read_data(input_file)
    results = calculate(data)
    write_results(results, output_file)
    print("Processing complete. Results written to output file.")