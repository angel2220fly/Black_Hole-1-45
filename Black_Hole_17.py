import os
import paq

# Function to load the dictionary from a line-by-line file
def load_dictionary(dictionary_file):
    """Loads the dictionary file into a mapping of index to word (line-by-line format)."""
    try:
        index_to_word = {}
        word_to_index = {}
        with open(dictionary_file, "r", encoding="utf-8") as f:
            for index, line in enumerate(f):
                word = line.strip()
                if word:  # Ensure the line is not empty
                    index_to_word[index] = word
                    word_to_index[word] = index
        return word_to_index, index_to_word
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        return None, None

# Function to compress a file
def compress_file(dictionary_file, input_file, output_file):
    """Compresses a text file using a dictionary and then with zlib."""
    word_to_index, _ = load_dictionary(dictionary_file)
    if word_to_index is None:
        return

    try:
        with open(input_file, "r", encoding="utf-8") as in_f, open(output_file, "wb") as out_f:
            data = in_f.read()
            binary_data = ""

            words = data.split()
            if words:
                for word in words:
                    if word in word_to_index:
                        index = word_to_index[word]
                        binary_data += f"{index:019b}"
                        binary_data += "10"  # Space marker
                    else:
                        for char in word:
                            if char == '\n':
                                binary_data += "1111111111111111" #16 bits for newline
                            else:
                                binary_data += "11" + f"{ord(char):08b}"

                # Convert binary data to bytes and compress with zlib
                byte_data = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder="big")
                compressed_data = paq.compress(byte_data)
                out_f.write(compressed_data)
                print(f"File compressed (custom method + zlib) and saved as '{output_file}'")
            else:
                print("Warning: Input file is empty or contains only whitespace.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error: Unable to compress file. Details: {e}")


# Function to decompress a file
def decompress_file(dictionary_file, input_file, output_file):
    """Decompresses a binary file using the dictionary and then with zlib."""
    _, index_to_word = load_dictionary(dictionary_file)
    if index_to_word is None:
        return

    try:
        with open(input_file, "rb") as f, open(output_file, "w", encoding="utf-8") as out_f:
            compressed_bytes = f.read()
            # Decompress with zlib first
            decompressed_bytes = paq.decompress(compressed_bytes)
            binary_data = bin(int.from_bytes(decompressed_bytes, byteorder="big"))[2:]
            binary_data = binary_data.zfill(len(decompressed_bytes) * 8) # Pad with leading zeros

            decompressed_data = ""
            i = 0
            while i < len(binary_data):
                if binary_data[i:i+2] == "10": # Space
                    decompressed_data += " "
                    i += 2
                elif binary_data[i:i+16] == "1111111111111111": # Newline
                    decompressed_data += "\n"
                    i += 16
                elif binary_data[i:i+2] == "11": # Other character
                    if i + 10 <= len(binary_data):
                        ascii_code = int(binary_data[i+2:i+10], 2)
                        decompressed_data += chr(ascii_code)
                        i += 10
                    else:
                        break
                else: #Word index
                    index = int(binary_data[i:i+19], 2)
                    if index in index_to_word:
                        decompressed_data += index_to_word[index] + " "
                    i += 19

            out_f.write(decompressed_data.strip())

        print(f"File decompressed (zlib + custom method) and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: Compressed file '{input_file}' not found.")
    except Exception as e:
        print(f"Error: Unable to decompress file. Details: {e}")

# Main function to handle user options
def main():
    print("Choose an option:")
    print("1. Compress a file (custom + zlib)")
    print("2. Decompress a file (zlib + custom)")
    choice = input("Enter your choice: ")

    if choice == '1':  # Compression with zlib
        dictionary_file = "Dictionary.txt"
        input_file = input("Enter the name of the input file to compress: ")
        output_file = input_file + ".b"
        compress_file(dictionary_file, input_file, output_file)

    elif choice == '2':  # Decompression with zlib
        dictionary_file = "Dictionary.txt"
        input_file = input("Enter the name of the compressed file (e.g., compressed.zlib): ")
        output_file = input_file[:-2]
        decompress_file(dictionary_file, input_file, output_file)

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
