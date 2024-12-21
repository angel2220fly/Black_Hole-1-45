import os
import struct
import random
import paq

print("Created by Jurijus Pacalovas.")
print("Black_Hole_18")
print("This software compresses any data, focusing on dictionary-based words.")

# Function to load the dictionary from the file
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

# Function to compress the file using both dictionary-based compression and PAQ
def compress_file_with_both_algorithms(dictionary_file, input_filename, output_filename, encoding="utf-8"):
    word_to_index, _ = load_dictionary(dictionary_file, encoding)
    if word_to_index is None:
        return

    try:
        with open(input_filename, 'r', encoding=encoding) as infile:
            data = infile.read()

        # Step 1: Dictionary-based compression
        encoded_data = bytearray()
        words = data.split(" ")  # Split text data by spaces

        for word in words:
            if word in word_to_index:
                # Encode dictionary word (00)
                encoded_data.append(0x00)
                index = word_to_index[word]
                encoded_data.extend(struct.pack(">I", index))
            else:
                # Encode non-dictionary word (01)
                encoded_data.append(0x01)
                encoded_data.extend(word.encode(encoding))
                encoded_data.append(0x20)  # Add space as delimiter

        # Step 2: PAQ Compression
        compressed_data = paq.compress(bytes(encoded_data))

        # Save the final compressed data to file
        with open(output_filename, "wb") as outfile:
            outfile.write(compressed_data)
            print(f"File compressed using both dictionary-based compression and PAQ, saved as '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred during compression: {e}")

# Function to decompress the file using both PAQ decompression and dictionary decoding
def decompress_file_with_both_algorithms(dictionary_file, input_filename, output_filename, encoding="utf-8"):
    _, index_to_word = load_dictionary(dictionary_file, encoding)
    if index_to_word is None:
        return

    try:
        with open(input_filename, 'rb') as infile:
            compressed_data = infile.read()

        # Step 1: Decompress using PAQ
        decompressed_data = paq.decompress(compressed_data)

        # Step 2: Dictionary-based decompression
        decoded_text = bytearray()
        i = 0

        while i < len(decompressed_data):
            flag = decompressed_data[i]
            i += 1

            if flag == 0x00:  # Dictionary word
                index = struct.unpack(">I", decompressed_data[i:i+4])[0]
                word = index_to_word.get(index, "<unknown>").encode(encoding)
                decoded_text.extend(word + b" ")
                i += 4
            elif flag == 0x01:  # Non-dictionary word
                word = bytearray()
                while i < len(decompressed_data) and decompressed_data[i] != 0x20:
                    word.append(decompressed_data[i])
                    i += 1
                decoded_text.extend(word + b" ")
                i += 1  # Skip the 0x20 space delimiter

        # Remove the last byte (if any)
        if len(decoded_text) > 0:
            decoded_text = decoded_text[:-1]

        # Save the decompressed data to the output file
        with open(output_filename, 'w', encoding=encoding) as outfile:
            outfile.write(decoded_text.decode(encoding))
            print(f"File decompressed using both PAQ and dictionary-based decompression, saved as '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: Compressed file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred during decompression: {e}")

# Main function to interact with the user
def main():
    print("Choose an option:")
    print("1. Compress the data file with both dictionary-based compression and PAQ")
    print("2. Decompress and save the raw decompressed data")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        input_file = input("Enter the name of the input file (e.g., text.txt): ")
        output_file = input_file + ".b"
        compress_file_with_both_algorithms("Dictionary.txt", input_file, output_file)
    elif choice == '2':
        input_file = input("Enter the name of the compressed file to decompress (e.g., text.txt.b): ")
        output_file = input_file[:-2]
        decompress_file_with_both_algorithms("Dictionary.txt", input_file, output_file)
    elif choice == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
