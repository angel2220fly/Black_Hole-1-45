import paq
from collections import Counter
import secrets
import os
import zlib

def create_opposite_table(data):
    """Creates an opposite table mapping frequently occurring bytes to shorter values."""
    frequency = Counter(data)
    sorted_items = sorted(frequency.items(), key=lambda item: -item[1])
    table = {item[0]: idx for idx, item in enumerate(sorted_items)}
    return table

def compress_with_table(input_filename, output_filename, random_table_filename="table1.bin"):
    """Compresses the file using an opposite table and a random 8-bit substitution table."""
    try:
        with open(input_filename, 'rb') as infile:
            data = infile.read()

        if not data:
            print("Input file is empty. No data to compress.")
            return

        table = create_opposite_table(data)

        # Load or generate the random 8-bit substitution table
        if not os.path.exists(random_table_filename):
            generate_8bit_random_table(random_table_filename)
        with open(random_table_filename, 'rb') as rf:
            random_table = list(rf.read())


        compressed_data = bytearray()
        for byte in data:
            substituted_byte = random_table[byte] #Substitute using the random table
            compressed_data.append(table.get(substituted_byte, substituted_byte)) #Apply frequency table


        zlib_compressed_data = paq.compress(bytes(compressed_data))

        with open(output_filename, 'wb') as outfile:
            table_size = len(table)
            outfile.write(table_size.to_bytes(4, 'big'))
            for original, compressed in table.items():
                outfile.write(original.to_bytes(1, 'big'))
                outfile.write(compressed.to_bytes(1, 'big'))
            outfile.write(zlib_compressed_data)

        print(f"Data compressed successfully into {output_filename}.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"Error during compression: {e}")

def decompress_with_table(input_filename, output_filename, random_table_filename="table1.bin"):
    """Decompresses the file."""
    try:
        with open(input_filename, 'rb') as infile:
            table_size = int.from_bytes(infile.read(4), 'big')
            table = {}
            for _ in range(table_size):
                original = infile.read(1)[0]
                compressed = infile.read(1)[0]
                table[compressed] = original
            zlib_compressed_data = infile.read()

        with open(random_table_filename, 'rb') as rf:
            random_table = list(rf.read())

        decompressed_data = paq.decompress(zlib_compressed_data)
        decompressed_data_final = bytearray()
        for byte in decompressed_data:
            original_byte = table.get(byte, byte) #Reverse frequency table
            decompressed_data_final.append(random_table.index(original_byte)) #Reverse random substitution


        with open(output_filename, 'wb') as outfile:
            outfile.write(decompressed_data_final)

        print(f"Data decompressed successfully into {output_filename}.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"Error during decompression: {e}")

def generate_8bit_random_table(filename="table1.bin"):
    """Generates a table of 256 entries, each with 8 random bits, using secrets, and saves it to a file."""
    rng = secrets.SystemRandom()
    table = [rng.randint(0, 255) for _ in range(256)]

    with open(filename, "wb") as f:
        f.write(bytes(table))

    print(f"8-bit random table generated and saved to '{filename}'.")


def main():
    while True:
        print("Choose an option:")
        print("1: Compress a File")
        print("2: Decompress a File")
        print("3: Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_file = input("Enter the name of the input file: ")
            output_file = input("Enter the name of the output file (e.g., output.paq): ")
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
