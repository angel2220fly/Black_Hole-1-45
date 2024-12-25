import base64
import os
import paq  # Assuming PAQ is installed for compression
print("Created by Jurijus Pacalovas.")
print("Black_Hole_53")

# Function for Base256 encoding and decoding
def base256_encode(data):
    return base64.b64encode(data).decode("utf-8")

def base256_decode(data):
    return base64.b64decode(data.encode("utf-8"))

# Function to transform zeros to ones or vice versa
def transform_zeros_ones(data, transform_type="zeros_to_ones"):
    transformed_data = []
    for byte in data:
        for i in range(8):  # Process each bit in the byte
            bit = (byte >> (7 - i)) & 1
            if transform_type == "zeros_to_ones" and bit == 0:
                transformed_data.append(1)
            elif transform_type == "ones_to_zeros" and bit == 1:
                transformed_data.append(0)
            else:
                transformed_data.append(bit)
    return transformed_data

# Function to add padding (zeros or ones)
def add_padding_zeros_ones(data, padding_type="add_zeros", padding_length=8):
    padding = [0] * padding_length if padding_type == "add_zeros" else [1] * padding_length
    return data + padding

# Function to convert binary data to bytes
def binary_to_bytes(binary_data):
    byte_data = []
    for i in range(0, len(binary_data), 8):
        byte = 0
        for j in range(8):
            if i + j < len(binary_data):
                byte |= (binary_data[i + j] << (7 - j))
        byte_data.append(byte)
    return byte_data

# Compression Process with 10 Iterations
def compress_10_times(input_filename, output_filename, iterations=10):
    try:
        data = open(input_filename, "rb").read()
        for i in range(iterations):
            # Compression steps
            transformed_data = transform_zeros_ones(data)
            padded_data = add_padding_zeros_ones(transformed_data)
            byte_data = binary_to_bytes(padded_data)
            byte_data = base256_encode(bytes(byte_data))
            data = paq.compress(byte_data.encode())
        with open(output_filename, "wb") as outfile:
            outfile.write(data)
            print(f"File successfully compressed 10 times as '{output_filename}'.")
    except Exception as e:
        print(f"Error during compression: {e}")

# Decompression Process with 10 Iterations
def extract_10_times(input_filename, output_filename, iterations=10):
    try:
        data = open(input_filename, "rb").read()
        for i in range(iterations):
            # Decompression steps
            decompressed_data = paq.decompress(data)
            decompressed_data = base256_decode(decompressed_data.decode())
            binary_data = []
            for byte in decompressed_data:
                for i in range(8):
                    binary_data.append((byte >> (7 - i)) & 1)
            binary_data = binary_data[:-8]  # Assuming padding_length is 8
            reversed_data = transform_zeros_ones(binary_data, transform_type="ones_to_zeros")
            data = bytes(binary_to_bytes(reversed_data))
        with open(output_filename, "wb") as outfile:
            outfile.write(data)
            print(f"File successfully extracted 10 times as '{output_filename}'.")
    except Exception as e:
        print(f"Error during extraction: {e}")

# Main function to interact with the user
def main():
    print("Choose the input file format (e.g., .b): ")
    input_filename = input("Enter the input file name (with .b extension): ").strip()

    print("Choose an option:")
    print("1. Compress")
    print("2. Extract")
    choice = input("Enter your choice (1/2): ").strip()

    output_filename = input_filename + ".b" if choice == "1" else input_filename[:-2]  # .b extension for compress and remove it for extract

    if choice == "1":
        compress_10_times(input_filename, output_filename)
    elif choice == "2":
        extract_10_times(input_filename, output_filename)
    else:
        print("Invalid choice, exiting.")

if __name__ == "__main__":
    main()