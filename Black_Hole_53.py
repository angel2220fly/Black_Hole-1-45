import os
import struct
import mimetypes
import paq
from mpmath import mp
print("Created by Jurijus Pacalovas.")
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

# Function to generate digits of pi
def generate_pi_digits(digits):
    if digits < 1:
        raise ValueError("The number of digits must be at least 1.")
    mp.dps = digits + 1  # Set the precision
    pi_value = str(mp.pi)[2:]  # Remove the "3."
    return pi_value

# Function to encode data with Pi digits (XOR operation)
def encode_with_pi(data, pi_digits):
    pi_sequence = [int(d) for d in pi_digits[:len(data)]]
    encoded_data = bytes([b ^ p for b, p in zip(data, pi_sequence)])
    return encoded_data

# Function to compress file using PAQ and then encode with Pi digits
def compress_with_paq_and_encode_with_pi(input_filename, output_filename, pi_digits=None, dictionary_file="Dictionary.txt", encoding="utf-8"):
    try:
        # Read the input file and compress
        mime_type, _ = mimetypes.guess_type(input_filename)
        with open(input_filename, "rb") as infile:
            data = infile.read()

        # PAQ Compression (if the file is not text)
        compressed_data = paq.compress(data)

        if pi_digits is None:
            pi_digits = generate_pi_digits(len(compressed_data))  # Generate Pi digits

        # Encode the compressed data with Pi digits (XOR operation)
        encoded_data = encode_with_pi(compressed_data, pi_digits)

        # Save the final encoded data
        with open(output_filename, "wb") as outfile:
            outfile.write(encoded_data)
            print(f"Compressed and encoded file saved to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to decode data with Pi digits and then decompress using PAQ
def decode_with_pi_and_decompress(input_filename, output_filename, pi_digits=None):
    try:
        with open(input_filename, "rb") as infile:
            encoded_data = infile.read()

        if pi_digits is None:
            pi_digits = generate_pi_digits(len(encoded_data))  # Generate Pi digits

        # Decode the data using Pi digits (reverse XOR operation)
        decoded_data = encode_with_pi(encoded_data, pi_digits)

        # Decompress the data using PAQ
        decompressed_data = paq.decompress(decoded_data)

        if decompressed_data is None:
            print(f"Error: Decompression failed for '{input_filename}'")
            return

        # Save the decompressed data to the output file
        with open(output_filename, "wb") as outfile:
            outfile.write(decompressed_data)
            print(f"Extracted file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during decoding and decompression: {e}")

def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decode a file")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            input_file = input("Enter the name of the file to compress: ").strip()
            output_file = input_file + ".b"  # Output filename with .b extension
            compress_with_paq_and_encode_with_pi(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the file to extract: ").strip()
            output_file = input_file[:-2]  # Remove the ".b" extension
            decode_with_pi_and_decompress(input_file, output_file)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()