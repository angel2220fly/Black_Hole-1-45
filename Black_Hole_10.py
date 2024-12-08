import random
import os
import paq

# Pseudorandom number generator for compression
def prng_compress(data):
    compressed = []
    seed = random.randint(0, 2**24 - 1)  # Random seed for compression
    random.seed(seed)
    for char in data:
        compressed.append(chr((ord(char) ^ random.randint(0, 255)) % 256))  # XOR with random number
    return ''.join(compressed), seed

# Pseudorandom number generator for extraction
def prng_extract(compressed_data, seed):
    extracted = []
    random.seed(seed)
    for char in compressed_data:
        extracted.append(chr((ord(char) ^ random.randint(0, 255)) % 256))  # Reverse XOR
    return ''.join(extracted)

# Compress file using PRNG and zlib
def compress_file():
    input_file_name = input("Enter the input file name for compression: ")
    if not os.path.exists(input_file_name):
        print("The specified file does not exist.")
        return

    with open(input_file_name, 'rb') as f:
        input_data = f.read()  # Read entire file in binary mode

    # Convert binary data to string for PRNG compression
    input_data_str = ''.join(map(chr, input_data))
    prng_compressed_data, seed = prng_compress(input_data_str)  # PRNG compression

    # Apply zlib compression to the PRNG output
    zlib_compressed_data = paq.compress(prng_compressed_data.encode('utf-8'))

    output_file_name = input("Enter the output file name for compressed data: ")
    with open(output_file_name, 'wb') as f:
        f.write(seed.to_bytes(3, 'big'))  # Save the seed as 3 bytes
        f.write(zlib_compressed_data)  # Save zlib-compressed data
    print(f"File compressed and saved to {output_file_name}")

# Extract file compressed with PRNG and zlib
def extract_file():
    input_file_name = input("Enter the input file name for extraction: ")
    if not os.path.exists(input_file_name):
        print("The specified file does not exist.")
        return

    with open(input_file_name, 'rb') as f:
        seed = int.from_bytes(f.read(3), 'big')  # Read the 3-byte seed
        zlib_compressed_data = f.read()  # Read the rest of the file

    # Decompress using zlib
    prng_compressed_data = paq.decompress(zlib_compressed_data).decode('utf-8')

    # Extract original data using PRNG
    extracted_data = prng_extract(prng_compressed_data, seed)

    # Convert the extracted string back to bytes
    extracted_data_bytes = bytes(map(ord, extracted_data))

    output_file_name = input("Enter the output file name for extracted data: ")
    with open(output_file_name, 'wb') as f:
        f.write(extracted_data_bytes)  # Save extracted data as binary
    print(f"Data extracted and saved to {output_file_name}")

# Main program logic
def main():
    print("Select an option:")
    print("1. Compress File")
    print("2. Extract File")
    option = input("Enter option (1 or 2): ")

    if option == '1':
        compress_file()
    elif option == '2':
        extract_file()
    else:
        print("Invalid option. Please select 1 or 2.")

if __name__ == '__main__':
    main()