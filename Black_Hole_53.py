import os
import struct
import random
import paq

print("Created by Jurijus Pacalavas.")
print("Black_Hole_53")

# Symbol and space mapping (5-bit representation)
symbol_map = {
    " ": 0b00001,  # Space
    ".": 0b00010,
    ",": 0b00011,
    "?": 0b00100,
    "!": 0b00101,
    "-": 0b00110,
    "'": 0b00111,
    '"': 0b01000,
    ":": 0b01001,
    ";": 0b01010,
    "(": 0b01011,
    ")": 0b01100,
    "[": 0b01101,
    "]": 0b01110,
    "{": 0b01111,
    "}": 0b10000,
    "/": 0b10001,
    "\\": 0b10010,
    "@": 0b10011,
    "#": 0b10100,
    "$": 0b10101,
    "%": 0b10110,
    "^": 0b10111,
    "&": 0b11000,
    "*": 0b11001,
    "+": 0b11010,
    "=": 0b11011,
    "<": 0b11100,
    ">": 0b11101,
    "|": 0b11110,
    "~": 0b11111
}

# Reverse map for decoding
reverse_symbol_map = {v: k for k, v in symbol_map.items()}

# Function to count zeros in 5-bit values
def count_zeros_in_bin_values():
    zero_counts = {}
    for symbol, value in symbol_map.items():
        # Count zeros in the 5-bit binary value
        zero_count = bin(value).count('0')
        zero_counts[symbol] = zero_count
    return zero_counts

# Display the zero counts for each symbol
zero_counts = count_zeros_in_bin_values()
for symbol, count in zero_counts.items():
    pass  # Optional: Display or use as needed

# Compression Function for text files
def compress_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    file_extension = input_filename.split('.')[-1]
    
    if file_extension == 'txt':
        # Compress .txt files using dictionary and PAQ
        compress_text_file(input_filename, output_filename, dictionary_file, encoding)
    else:
        # Compress non-txt files using binary and PAQ
        compress_binary_file(input_filename, output_filename)

def compress_text_file(input_filename, output_filename, dictionary_file, encoding="utf-8"):
    if not input_filename.endswith('.txt'):
        print("Error: Only .txt files can be compressed.")
        return

    def load_dictionary(dictionary_file):
        word_to_index = {}
        try:
            with open(dictionary_file, "r", encoding=encoding) as f:
                for index, line in enumerate(f):
                    word = line.strip().lower()
                    word_to_index[word] = index
            return word_to_index
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            return None

    word_to_index = load_dictionary(dictionary_file)
    if word_to_index is None:
        return

    try:
        with open(input_filename, "r", encoding=encoding) as infile:
            data = infile.read()

        compressed_data = bytearray()
        words = data.split(" ")

        for word in words:
            normalized_word = word.lower()
            if normalized_word in word_to_index:
                index = word_to_index[normalized_word]
                compressed_data.append(0x00)  # Dictionary flag
                compressed_data.extend(struct.pack(">I", index))
            else:
                compressed_data.append(0x01)  # Non-dictionary word
                compressed_data.extend(word.encode(encoding))

            # Encode space or symbols after the word
            if word.endswith(tuple(symbol_map.keys())):
                symbol = word[-1]
                symbol_code = symbol_map[symbol]
                compressed_data.append(0x02)  # Symbol flag
                compressed_data.append(symbol_code)
            else:
                compressed_data.append(0x02)  # Space flag
                compressed_data.append(symbol_map[" "])

        # PAQ compression of the entire compressed data
        final_compressed_data = paq.compress(bytes(compressed_data))

        with open(output_filename, "wb") as outfile:
            outfile.write(final_compressed_data)
            print(f"Compressed file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during compression: {e}")

def compress_binary_file(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as infile:
            data = infile.read()

        # Apply PAQ compression
        compressed_data = paq.compress(data)

        with open(output_filename, "wb") as outfile:
            outfile.write(compressed_data)
            print(f"Compressed file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during binary compression: {e}")

# Extraction Function
def extract_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    file_extension = output_filename.split('.')[-1]
    
    if file_extension == 'txt':
        # Extract .txt files
        extract_text_file(input_filename, output_filename, dictionary_file, encoding)
    else:
        # Extract non-txt files
        extract_binary_file(input_filename, output_filename)

def extract_text_file(input_filename, output_filename, dictionary_file, encoding="utf-8"):
    if not output_filename.endswith('.txt'):
        print("Error: Extracted file must have a .txt extension.")
        return

    def load_dictionary(dictionary_file):
        index_to_word = {}
        try:
            with open(dictionary_file, "r", encoding=encoding) as f:
                for index, line in enumerate(f):
                    word = line.strip()
                    index_to_word[index] = word
            return index_to_word
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            return None

    index_to_word = load_dictionary(dictionary_file)
    if index_to_word is None:
        return

    try:
        with open(input_filename, "rb") as infile:
            compressed_data = infile.read()

        # Decompress the data using PAQ
        decompressed_data = paq.decompress(compressed_data)

        if decompressed_data is None:
            print(f"Error: Decompression failed for '{input_filename}'")
            return

        decoded_data = bytearray()
        i = 0
        while i < len(decompressed_data):
            flag = decompressed_data[i]
            i += 1
            if flag == 0x00:  # Dictionary word
                if i + 4 <= len(decompressed_data):  # Ensure enough bytes for 4-byte index
                    index = struct.unpack(">I", decompressed_data[i:i+4])[0]
                    word = index_to_word.get(index, "<unknown>")
                    decoded_data.extend(word.encode(encoding))
                    i += 4
                else:
                    print("Error: Insufficient data for dictionary word index.")
                    break
            elif flag == 0x01:  # Non-dictionary word
                word = bytearray()
                while i < len(decompressed_data) and decompressed_data[i] != 0x02:
                    word.append(decompressed_data[i])
                    i += 1
                decoded_data.extend(word)
            elif flag == 0x02:  # Symbol or space
                symbol_code = decompressed_data[i]
                i += 1
                symbol = reverse_symbol_map.get(symbol_code, " ")
                decoded_data.extend(symbol.encode(encoding))

        with open(output_filename, "w", encoding=encoding) as outfile:
            outfile.write(decoded_data.decode(encoding))
            print(f"Extracted file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during extraction: {e}")

def extract_binary_file(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as infile:
            compressed_data = infile.read()

        # Decompress the data using PAQ
        decompressed_data = paq.decompress(compressed_data)

        if decompressed_data is None:
            print(f"Error: Decompression failed for '{input_filename}'")
            return

        with open(output_filename, "wb") as outfile:
            outfile.write(decompressed_data)
            print(f"Extracted binary file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during binary extraction: {e}")

# Main Menu
def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Extract a file")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            input_file = input("Enter the name of the file to compress (e.g., input.txt or input.bin): ").strip()
            output_file = input_file+".b"
            compress_file(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the file to extract (e.g., output.b or output.bin): ").strip()
            output_file = input_file[:-2]
            extract_file(input_file, output_file)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()