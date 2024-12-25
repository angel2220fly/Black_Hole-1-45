import os
import struct
import mimetypes
import paq
from mpmath import mp

print("Created by Jurijus Pacalovas.")
print("Black_Hole_53")

# Reverse bits 2, 3, 4, 5, 6, 7
def reverse_bits(byte):
    # Isolate bits 2 to 7 (shift left and right to clear others)
    mask = 0b01111110  # Bits 2 to 7
    relevant_bits = (byte & mask) >> 1

    # Reverse these bits
    reversed_bits = int('{:06b}'.format(relevant_bits)[::-1], 2)

    # Clear bits 2 to 7 in the original byte and replace them with the reversed bits
    byte = (byte & ~mask) | (reversed_bits << 1)
    return byte

# Reverse all relevant bits in the data
def reverse_bits_in_data(data):
    return bytes(reverse_bits(byte) for byte in data)

# Generate digits of pi
def generate_pi_digits(digits):
    if digits < 1:
        raise ValueError("The number of digits must be at least 1.")
    mp.dps = digits + 1
    pi_value = str(mp.pi)[2:]
    return pi_value

# XOR with Pi digits
def encode_with_pi(data, pi_digits):
    pi_sequence = [int(d) for d in pi_digits[:len(data)]]
    return bytes([b ^ p for b, p in zip(data, pi_sequence)])

# Compress with PAQ, reverse bits, and encode with Pi
def compress_with_paq_and_encode(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as infile:
            data = infile.read()

        # Reverse bits 2-7 before compression
        data = reverse_bits_in_data(data)

        # Compress using PAQ
        compressed_data = paq.compress(data)

        # Generate Pi digits for XOR encoding
        pi_digits = generate_pi_digits(len(compressed_data))
        encoded_data = encode_with_pi(compressed_data, pi_digits)

        # Reverse bits 2-7 after Pi encoding
        encoded_data = reverse_bits_in_data(encoded_data)

        # Save the final output
        with open(output_filename, "wb") as outfile:
            outfile.write(encoded_data)
            print(f"Compressed and encoded file saved to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred during compression: {e}")

# Decode with Pi, reverse bits, and decompress with PAQ
def decode_with_paq_and_pi(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as infile:
            encoded_data = infile.read()

        # Reverse bits 2-7 before Pi decoding
        encoded_data = reverse_bits_in_data(encoded_data)

        # Generate Pi digits for XOR decoding
        pi_digits = generate_pi_digits(len(encoded_data))
        decoded_data = encode_with_pi(encoded_data, pi_digits)

        # Decompress using PAQ
        decompressed_data = paq.decompress(decoded_data)

        if decompressed_data is None:
            print(f"Error: Decompression failed for '{input_filename}'.")
            return

        # Reverse bits 2-7 after decompression
        decompressed_data = reverse_bits_in_data(decompressed_data)

        # Save the final output
        with open(output_filename, "wb") as outfile:
            outfile.write(decompressed_data)
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
            compress_with_paq_and_encode(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the file to extract: ").strip()
            output_file = input_file[:-2]
            decode_with_paq_and_pi(input_file, output_file)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()