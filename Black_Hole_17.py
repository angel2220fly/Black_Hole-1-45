import os
import struct

print("Created by Jurijus Pacalovas.")
print("Black_Hole_17")
print("This software compresses any data, focusing on dictionary-based words.")

try:
    import paq
except ImportError:
    print("Error: The 'paq' library is not installed. Please install it using 'pip install paq8px'.")
    exit()

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

def compress_file(dictionary_file, input_file, output_file, encoding="utf-8"):
    word_to_index, _ = load_dictionary(dictionary_file, encoding)
    if word_to_index is None:
        return

    try:
        with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
            raw_data = infile.read()
            original_size = len(raw_data)  # Measure size of the file before compression
            print(f"Original file size: {original_size} bytes")
            
            # Now encode words
            encoded_data = bytearray()
            words = raw_data.split(b" ")  # Split binary data by spaces

            for word in words:
                try:
                    decoded_word = word.decode(encoding)  # Try decoding as text
                    if decoded_word in word_to_index:
                        # Encode dictionary word (00)
                        encoded_data.append(0x00)
                        index = word_to_index[decoded_word]
                        encoded_data.extend(struct.pack(">I", index))
                    else:
                        # Encode non-dictionary word (01)
                        encoded_data.append(0x01)
                        encoded_data.extend(word)
                        encoded_data.append(0x20)  # Add space as delimiter
                except UnicodeDecodeError:
                    # Handle raw binary data for non-decodable segments
                    encoded_data.append(0x01)
                    encoded_data.extend(word)
                    encoded_data.append(0x20)  # Add space as delimiter

            # Step 2: Compress the words (encode them)
            compressed_data = paq.compress(bytes(encoded_data))
            compressed_size = len(compressed_data)  # Measure the compressed file size
            print(f"Compressed file size: {compressed_size} bytes")

            # Step 3: Save the size of the encoded (and compressed) data
            size_header = struct.pack(">I", original_size)  # Pack the original size as the header (4 bytes)
            compressed_data = size_header + compressed_data  # Prepend original size to compressed data

            # Write the final compressed data to the output file
            outfile.write(compressed_data)
            print(f"File compressed and saved as '{output_file}'")
    except (FileNotFoundError, IOError) as e:
        print(f"Error compressing file: {e}")

def decompress_file(dictionary_file, input_file, output_file, encoding="utf-8"):
    _, index_to_word = load_dictionary(dictionary_file, encoding)
    if index_to_word is None:
        return

    try:
        with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
            compressed_data = infile.read()

            # Ensure there's at least 4 bytes for the size header
            if len(compressed_data) < 4:
                print("Error: Not enough data for size header.")
                return

            # Extract the original file size from the first 4 bytes (size header)
            size_header = compressed_data[:4]
            original_size = struct.unpack(">I", size_header)[0]  # Extract the original file size from the header
            print(f"Extracted original file size: {original_size} bytes")

            # Remove the first 4 bytes (file size header)
            decompressed_data = compressed_data[4:]

            # Decompress using PAQ
            decompressed_data = paq.decompress(decompressed_data)

            # Remove the first byte (0x01) if it's present
            if decompressed_data[0] == 0x01:
                decompressed_data = decompressed_data[1:]

            # Ensure the decompressed data matches the original size
            if len(decompressed_data) != original_size:
                print(f"Warning: The decompressed data size ({len(decompressed_data)}) does not match the original size ({original_size}). Truncating.")
                decompressed_data = decompressed_data[:original_size]

            # Write the resulting data to the output file
            outfile.write(decompressed_data)
            print(f"File decompressed and saved as '{output_file}'")
    except (FileNotFoundError, IOError) as e:
        print(f"Error decompressing file: {e}")
    except struct.error as e:
        print(f"Error unpacking data: {e}")

def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice: ")
    dictionary_file = "Dictionary.txt"
    encoding = "utf-8"

    if choice == '1':
        input_file = input("Enter the input file to compress: ")
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return

        output_file = input_file + ".b"
        compress_file(dictionary_file, input_file, output_file, encoding)
    elif choice == '2':
        input_file = input("Enter the compressed file: ")
        if not os.path.exists(input_file):
            print(f"Error: Compressed file '{input_file}' not found.")
            return

        output_file = input_file[:-2]
        decompress_file(dictionary_file, input_file, output_file, encoding)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()