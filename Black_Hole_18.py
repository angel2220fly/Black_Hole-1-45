import os
import struct
import random
import paq

print("Created by Jurijus Pacalovas.")

def generate_headings_and_chunks():
    """Generates data file with 17-bit headings and 256 positions (256 bits each) in a 256-byte chunk."""
    file_name = input("Enter the name of the file to save the output (e.g., table4.txt): ").strip()
    if os.path.exists(file_name):
        print(f"The file '{file_name}' already exists. Skipping generation.")
        return True  # Indicate success (file already exists)

    try:
        with open(file_name, "w") as file:
            max_headings = 2**17  # 17-bit headings (0 to 2^17-1)
            chunk_size = 256  # Number of positions in the chunk

            random.seed(42)  # for reproducibility

            for heading in range(max_headings):
                heading_bits = f"{heading:017b}"  # 17-bit heading

                # Create a chunk of 256 positions (each with 256 bits, which is 32 bytes)
                chunk = [bytes([random.randint(0, 255) for _ in range(32)]) for _ in range(chunk_size)]

                # Convert each position in the chunk to binary (256 bits per position)
                chunk_bits = ''.join(''.join(f"{byte:08b}" for byte in position) for position in chunk)

                # Write the heading and the corresponding 256 positions (256 bits each)
                file.write(f"{heading_bits} {chunk_bits}\n")

        print(f"Data generated and saved to '{file_name}'.")
        return True
    except Exception as e:
        print(f"An error occurred during data generation: {e}")
        return False

def load_dictionary(dictionary_file, encoding="utf-8"):
    """Loads the dictionary, handling errors gracefully."""
    try:
        word_to_index = {}
        index_to_word = {}
        with open(dictionary_file, "r", encoding=encoding) as f:
            for index, line in enumerate(f):
                word = line.strip()
                if word:
                    word_to_index[word] = index
                    index_to_word[index] = word
        if not word_to_index:
            raise ValueError("Dictionary file is empty.")
        return word_to_index, index_to_word
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        return None, None
    except (ValueError, UnicodeDecodeError) as e:
        print(f"Error loading dictionary: {e}")
        return None, None

def compress_file(dictionary_file, input_filename, output_filename, use_paq=True, encoding="utf-8"):
    word_to_index, _ = load_dictionary(dictionary_file, encoding)
    if word_to_index is None:
        return

    try:
        with open(input_filename, 'rb') as infile:
            data = infile.read()

        # Compress data with PAQ if required
        if use_paq:
            compressed_data = paq.compress(data)
            print("Compression using PAQ successful.")
        else:
            compressed_data = data
            print("No compression (PAQ not used), raw data copied.")

        with open(output_filename, 'wb') as outfile:
            outfile.write(compressed_data)

        print(f"Compression successful. Output saved to {output_filename}")
        return True
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred during compression: {e}")
        return False

def decompress_file(dictionary_file, input_filename, output_filename, use_paq=True, encoding="utf-8"):
    _, index_to_word = load_dictionary(dictionary_file, encoding)
    if index_to_word is None:
        return

    try:
        with open(input_filename, 'rb') as infile:
            compressed_data = infile.read()

        # Decompress data with PAQ if required
        if use_paq:
            decompressed_data = paq.decompress(compressed_data)
            print("Decompression using PAQ successful.")
        else:
            decompressed_data = compressed_data
            print("No decompression (PAQ not used), raw data copied.")

        # Write decompressed data to output file
        with open(output_filename, 'wb') as outfile:
            outfile.write(decompressed_data)

        print(f"Decompression successful. Raw decompressed data saved to {output_filename}")
        return True
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred during decompression: {e}")
        return False

def main():
    # Ask user about PAQ usage at the start
    use_paq = input("Would you like to use PAQ compression? (yes/no): ").strip().lower()
    use_paq = True if use_paq == 'yes' else False
    dictionary_file = "Dictionary.txt"
    encoding = "utf-8"

    while True:
        print("\nChoose an option:")
        print("1: Generate data file with 17-bit headings and 256 positions (256 bits each) in a 256-byte chunk")
        print("2: Compress the data file with or without PAQ")
        print("3: Decompress and save raw decompressed data")
        print("4: Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            if not generate_headings_and_chunks():
                print("Data generation failed.")

        elif choice == '2':
            input_file = input("Enter the name of the input file (e.g., table4.txt): ")
            output_file = input_file+".b"

            if not compress_file(dictionary_file, input_file, output_file, use_paq, encoding):
                print("Compression failed.")

        elif choice == '3':
            input_file = input("Enter the name of the compressed file to decompress (e.g., table4.paq): ")
            output_file = input_file[:-2]

            if not decompress_file(dictionary_file, input_file, output_file, use_paq, encoding):
                print("Decompression failed.")

        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()