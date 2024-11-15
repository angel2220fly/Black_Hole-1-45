# Function to count zeros in a sequence of numbers
def count_zeros(sequence):
    zero_count = sum(1 for number in sequence if number == 0)
    return zero_count
import paq
#Author Jurijus Pacalovas

# Function to compress binary data
def compress_binary_data(data):
    compressed_data = paq.compress(data)
    return compressed_data

# Function to extract binary data
def extract_binary_data(compressed_data):
    extracted_data = paq.decompress(compressed_data)
    return extracted_data

# Function to read pi value from a text file
def read_pi_value(file_name):
    with open(file_name, 'r') as file:
        pi_value = file.readline().strip()
    return pi_value

# Function to generate a sequence of numbers by incrementing pi
def generate_pi_sequence(pi_value, start, end):
    results = []
    pi_value = float(pi_value)
    for value in range(start, end + 1):
        result = pi_value + value
        results.append(result)
    return results

# Function to generate a sequence of numbers from 5 to 2^20
def generate_sequence_5_to_2_20():
    start_range = 1

    end_range = 1875968
    sequence = list(range(start_range, end_range + 1))
    return sequence

# Function to count zeros in a sequence of numbers
def count_zeros(sequence):
    zero_count = sum(1 for number in sequence if number == 0)
    return zero_count

while True:
    print("Options:")
    print("1. Compress")
    print("2. Extract")
    print("3. Generate Pi Sequence")
    print("4. Generate Sequence 5 to 2GB")
    print("5. Count Zeros in Sequence")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        # Compression
        input_file = input("Enter the input file name for compression: ")
        output_file = input("Enter the output file for saving compressed data: ")

        # Read binary data from the input file
        with open(input_file, 'rb') as file:
            binary_data = file.read()

        # Compress the binary data using paq
        compressed_data = compress_binary_data(binary_data)

        # Save the compressed data to the specified output file
        with open(output_file, 'wb') as file:
            file.write(compressed_data)

        print("Compression complete.")
    
    elif choice == '2':
        # Extraction
        input_file = input("Enter the input file name for extraction: ")
        output_file = input("Enter the output file for saving extracted data: ")

        # Read the compressed data from the input file
        with open(input_file, 'rb') as file:
            compressed_data = file.read()

        # Extract the data from the compressed data using paq
        extracted_data = extract_binary_data(compressed_data)

        # Save the extracted data to the specified output file
        with open(output_file, 'wb') as file:
            file.write(extracted_data)

        print("Extraction complete.")
    
    elif choice == '3':
        # Read pi value from a text file
        pi_file = "PI_10M.txt"
        pi_value = read_pi_value(pi_file)

        # Generate a sequence of numbers by incrementing pi
        start_range = 1
        end_range =  1875968
        results = generate_pi_sequence(pi_value, start_range, end_range)

        # Print the list of results
        for index, value in enumerate(results, start=start_range):
            print(f"Result {index}: {value}")
    
    elif choice == '4':
        # Generate a sequence of numbers from 5 to 2^20
        sequence_5_to_2_20 = generate_sequence_5_to_2_20()
        print("Generated sequence from 5 to 2^20:")
        print(sequence_5_to_2_20)

    elif choice == '5':
        # Count zeros in a sequence
        sequence = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))
        zero_count = count_zeros(sequence)
        print(f"Number of zeros in the sequence: {zero_count}")

    elif choice == '6':
        # Quit the program
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
