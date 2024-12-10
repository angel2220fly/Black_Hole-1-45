import paq
from collections import Counter
#Created by Jurijus Pacalovas.


def create_opposite_table(data):
    """
    Create an opposite table mapping frequently occurring bytes to shorter values.
    """
    frequency = Counter(data)
    sorted_items = sorted(frequency.items(), key=lambda item: -item[1])
    table = {item[0]: idx for idx, item in enumerate(sorted_items)}
    return table


def generate_heading_and_variations():
    """
    Generate 25-bit headings, assuming that headings should be in the range 0-33554431 (25-bit).
    """
    headings_and_variations = []
    max_headings = 2**25  # Total possible headings: 33554432 (0 to 33554431)
    
    for heading in range(max_headings):
        heading_bits = f"{heading:025b}"  # Convert heading to 25-bit binary format
        headings_and_variations.append(heading_bits)
    
    return headings_and_variations


def compress_with_table(input_filename, output_filename):
    """
    Compress the file using an opposite table and 25-bit headings, then zlib compression.
    Mark with 0 for compressed, 1 for uncompressed.
    """
    try:
        # Read input file
        with open(input_filename, 'rb') as infile:
            data = infile.read()

        if not data:
            print("Input file is empty. No data to compress.")
            return

        # Create the opposite table
        table = create_opposite_table(data)

        # Generate headings and variations for the data
        headings = generate_heading_and_variations()

        # Initialize the output with the table and compressed data
        output_data = bytearray()

        # Write the table first (key-value pairs as bytes)
        table_size = len(table)
        output_data.extend(table_size.to_bytes(2, 'big'))  # Write table size (2 bytes)
        for original, compressed in table.items():
            output_data.extend(bytes([original, compressed]))

        # Compress the data using the table and 25-bit headings
        compressed_data = bytearray()
        for byte in data:
            compressed_data.append(table[byte])

        # Apply zlib compression
        zlib_compressed_data = paq.compress(bytes(compressed_data))  # Convert bytearray to bytes

        # Check if zlib compression is effective
        if len(zlib_compressed_data) < len(data):
            # If compressed, add 0 flag
            output_data.append(0)
            output_data.extend(zlib_compressed_data)
        else:
            # If no compression, add 1 flag
            output_data.append(1)
            output_data.extend(compressed_data)

        # Save the compressed data
        with open(output_filename, 'wb') as outfile:
            outfile.write(output_data)

        print(f"Data compressed successfully into {output_filename}.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"Error during compression: {e}")


def decompress_with_table(input_filename, output_filename):
    """
    Decompress the file using an opposite table, 25-bit headings, and zlib decompression.
    Handle 0 and 1 marking.
    """
    try:
        with open(input_filename, 'rb') as infile:
            # Read the table size
            table_size = int.from_bytes(infile.read(2), 'big')

            # Read the table
            table = {}
            for _ in range(table_size):
                original = infile.read(1)[0]
                compressed = infile.read(1)[0]
                table[compressed] = original

            # Read the flag (0 for compressed, 1 for uncompressed)
            compress_flag = infile.read(1)[0]

            # Read the remaining data
            compressed_data = infile.read()

        if not compressed_data:
            print("Compressed file is empty. No data to decompress.")
            return

        # Decompress based on flag
        if compress_flag == 0:
            # Decompress using zlib
            decompressed_data = paq.decompress(compressed_data)
        else:
            # Use uncompressed data as is
            decompressed_data = compressed_data

        # Reverse the compression using the opposite table
        decompressed_data_final = bytearray()
        for byte in decompressed_data:
            decompressed_data_final.append(table[byte])

        # Save the decompressed data
        with open(output_filename, 'wb') as outfile:
            outfile.write(decompressed_data_final)

        print(f"Data decompressed successfully into {output_filename}.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"Error during decompression: {e}")


def main():
    while True:
        print("Choose an option:")
        print("1: Compress a File")
        print("2: Decompress a File")
        print("3: Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_file = input("Enter the name of the input file: ")
            output_file = input("Enter the name of the output file (e.g., output.b): ")
            compress_with_table(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the input file to decompress: ")
            output_file = input("Enter the name of the output file (e.g., output_decompressed.txt): ")
            decompress_with_table(input_file, output_file)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()