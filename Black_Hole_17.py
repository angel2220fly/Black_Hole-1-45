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

            # Compress using PAQ
            compressed_data = paq.compress(bytes(encoded_data))
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
            print(f"Compressed file size: {len(compressed_data)} bytes")  # Debug: Print the size of compressed data

            # Decompress using PAQ
            try:
                decompressed_data = paq.decompress(compressed_data)
            except Exception as e:
                print(f"Error during decompression: {e}")
                return

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
                elif flag == 0x10:  # New line
                    decoded_text.extend(b"\n")

            # Debug: Print decompressed data size before last byte removal
            print(f"Decompressed data size before removing last byte: {len(decoded_text)} bytes")

            # Remove the last byte (if any)
            if len(decoded_text) > 0:
                decoded_text = decoded_text[:-1]

            # Debug: Print decompressed data size after last byte removal
            print(f"Decompressed data size after removing last byte: {len(decoded_text)} bytes")

            # Write decompressed data to file
            outfile.write(decoded_text)
            print(f"File decompressed and saved as '{output_file}'")
    except (FileNotFoundError, IOError) as e:
        print(f"Error decompressing file: {e}")

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