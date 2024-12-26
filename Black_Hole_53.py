import os
import struct
import random
import paq
from mpmath import mp

print("Created by Jurijus Pacalovas.")
print("Black_Hole_53")

# Symbol and space mapping (5-bit representation)
symbol_map = {
    " ": 0b00001,
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

reverse_symbol_map = {v: k for k, v in symbol_map.items()}

# Generate digits of pi
def generate_pi_digits(digits):
    if digits < 1:
        raise ValueError("The number of digits must be at least 1.")
    mp.dps = digits + 1
    pi_value = str(mp.pi)[2:]
    return pi_value

# Reverse bits 2-15
def reverse_bits(byte):
    mask = 0b01111110
    relevant_bits = (byte & mask) >> 1
    reversed_bits = int('{:06b}'.format(relevant_bits)[::-1], 2)
    return (byte & ~mask) | (reversed_bits << 1)

def reverse_bits_in_data(data):
    return bytes(reverse_bits(byte) for byte in data)

# XOR encoding with Pi digits
def encode_with_pi(data, pi_digits):
    pi_sequence = [int(d) for d in pi_digits[:len(data)]]
    return bytes([b ^ p for b, p in zip(data, pi_sequence)])

# Convert binary to base 256
def binary_to_base256(binary_string):
    if len(binary_string) % 8 != 0:
        raise ValueError("The binary string length must be a multiple of 8.")
    
    byte_chunks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    base256_values = [int(chunk, 2) for chunk in byte_chunks]
    
    return base256_values

# Compress and encode using paq and binary to base 256
def compress_with_zlib_and_encode(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    try:
        # Load dictionary for compression
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

        # Open the input file and read data
        with open(input_filename, "r", encoding=encoding) as infile:
            data = infile.read()

        compressed_data = bytearray()
        words = data.split(" ")

        # Process words and apply dictionary compression
        for word in words:
            normalized_word = word.lower()
            if normalized_word in word_to_index:
                index = word_to_index[normalized_word]
                compressed_data.append(0x00)  # Dictionary flag
                compressed_data.extend(struct.pack(">I", index))  # 4-byte index
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

        # PAQ compression
        final_compressed_data = paq.compress(bytes(compressed_data))

        # Write compressed data to the output file
        with open(output_filename, "wb") as outfile:
            outfile.write(final_compressed_data)
            print(f"Compressed and encoded file saved to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred during compression: {e}")

# Decode and decompress using paq and binary to base 256
def decode_with_zlib_and_pi(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    try:
        # Load dictionary for decompression
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

        # Read the encoded data
        with open(input_filename, "rb") as infile:
            encoded_data = infile.read()

        # Decompress data using paq
        decompressed_data = paq.decompress(encoded_data)

        decoded_data = bytearray()
        i = 0
        while i < len(decompressed_data):
            flag = decompressed_data[i]
            i += 1
            if flag == 0x00:  # Dictionary word
                if i + 4 <= len(decompressed_data):  # Ensure 4 bytes for index
                    index = struct.unpack(">I", decompressed_data[i:i+4])[0]  # 4-byte index
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

        # Write decompressed data to the output file
        with open(output_filename, "w", encoding=encoding) as outfile:
            outfile.write(decoded_data.decode(encoding))
            print(f"Extracted file saved to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred during extraction: {e}")

def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decode a file")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            input_file = input("Enter the name of the file to compress: ").strip()
            output_file = input_file + ".b"
            compress_with_zlib_and_encode(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the file to extract: ").strip()
            output_file = input_file[:-2]  # Remove '.b' extension
            decode_with_zlib_and_pi(input_file, output_file)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()