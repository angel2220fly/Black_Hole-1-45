import random
import paq
import pickle
import os
print("Created by Jurijus Pacalovas.")

def generate_headings_and_variations(filename="data.pkl"):
    """Generates data and saves it to a pickle file."""
    max_headings = 2**17
    variations_per_heading = 128
    half_variations = variations_per_heading // 2
    random.seed(42)
    data = {}
    for heading in range(max_headings):
        first_half = random.sample(range(256), half_variations)
        second_half = list(reversed(first_half))
        variations_8_bits = first_half + second_half
        data[heading] = variations_8_bits
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print(f"Data generated and saved to {filename}")


def compress_file(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as infile:
            data = infile.read()
        compressed_data = paq.compress(data)
        with open(output_filename, 'wb') as outfile:
            outfile.write(compressed_data)
        print(f"Compression successful. Output saved to {output_filename}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred during compression: {e}")

def decompress_file(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as infile:
            compressed_data = infile.read()
        decompressed_data = paq.decompress(compressed_data)
        with open(output_filename, 'wb') as outfile:
            outfile.write(decompressed_data)
        print(f"Decompression successful. Output saved to {output_filename}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except paq.error as e:
        print(f"Error during decompression: {e}")
    except Exception as e:
        print(f"An error occurred during decompression: {e}")


def main():
    if not os.path.exists("data.pkl"):
        generate_headings_and_variations()

    while True:
        print("\nChoose an option:")
        print("1: Compress the data file")
        print("2: Decompress a file")
        print("3: Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_file = input("Enter the name of the input file (data.pkl): ")
            output_file = input("Enter the name of the output file (data.paq): ")
            compress_file(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the compressed file to decompress (data.paq): ")
            output_file = input("Enter the name of the output file for decompression (data_decompressed.pkl): ")
            decompress_file(input_file, output_file)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
