import random
import os

def prng_compress(data, seed):
    """Compresses data using a PRNG with a given seed."""
    random.seed(seed)
    compressed = bytes([ord(c) ^ random.randint(0, 255) for c in data])
    return compressed

def prng_extract(compressed_data, seed):
    """Extracts data using a PRNG with a given seed."""
    random.seed(seed)
    extracted = ''.join([chr(c ^ random.randint(0, 255)) for c in compressed_data])
    return extracted

def compress_file():
    """Compresses a file using PRNG and zlib."""
    input_filename = input("Enter input filename: ")
    if not os.path.exists(input_filename):
        print("File not found.")
        return

    try:
        with open(input_filename, 'rb') as infile:
            data = infile.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    seed = random.randint(0, 2**24 - 1)
    compressed_data = prng_compress(data.decode('latin-1', errors='replace'), seed) #Handle potential encoding issues
    zlib_compressed = compressed_data

    output_filename = input("Enter output filename: ")
    try:
        with open(output_filename, 'wb') as outfile:
            outfile.write(seed.to_bytes(3, 'big'))
            outfile.write(zlib_compressed)
        print(f"File compressed to {output_filename}")
    except Exception as e:
        print(f"Error writing file: {e}")


def extract_file():
    """Extracts a file compressed with PRNG and zlib."""
    input_filename = input("Enter input filename: ")
    if not os.path.exists(input_filename):
        print("File not found.")
        return

    try:
        with open(input_filename, 'rb') as infile:
            seed = int.from_bytes(infile.read(3), 'big')
            zlib_compressed = infile.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    try:
        compressed_data = zlib_compressed
        extracted_data = prng_extract(compressed_data, seed)
        output_filename = input("Enter output filename: ")
        with open(output_filename, 'wb') as outfile:
            outfile.write(extracted_data.encode('latin-1', errors='replace')) #Handle potential encoding issues
        print(f"File extracted to {output_filename}")
    except Exception as e:
        print(f"Error extracting file: {e}")


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
        print("Invalid option.")

if __name__ == '__main__':
    main()