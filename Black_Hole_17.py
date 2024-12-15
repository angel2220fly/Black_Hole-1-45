import paq
import os
from collections import Counter

# Function to load the dictionary from a file
def load_dictionary(dictionary_file):
    try:
        with open(dictionary_file, 'r') as f:
            lines = f.readlines()
        # Creating a dictionary where each line has a word and its code
        dictionary = {}
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 4:
                word, code = parts[0], parts[1]
                dictionary[word] = code
        return dictionary
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return {}

# Function to apply dictionary compression
def dictionary_compress(text, dictionary):
    compressed_text = ""
    for word in text.split():
        if word in dictionary:
            compressed_text += dictionary[word] + " "
        else:
            compressed_text += word + " "
    return compressed_text.strip()

# Function to apply dictionary decompression
def dictionary_decompress(text, dictionary):
    reverse_dict = {v: k for k, v in dictionary.items()}
    decompressed_text = ""
    for code in text.split():
        if code in reverse_dict:
            decompressed_text += reverse_dict[code] + " "
        else:
            decompressed_text += code + " "
    return decompressed_text.strip()

# 1. Base256 Compression (Identity compression)
def base256_compress(input_file):
    try:
        with open(input_file, 'rb') as f_in:
            data = f_in.read()
        return data
    except Exception as e:
        print(f"Error during Base256 compression: {e}")
        return None

# 2. zlib Compression
def zlib_compress(data):
    try:
        compressed_data = paq.compress(data)
        return compressed_data
    except Exception as e:
        print(f"Error during zlib compression: {e}")
        return None

# 3. Run-Length Encoding (RLE) Compression
def rle_compress(data):
    try:
        compressed_data = bytearray()
        i = 0
        while i < len(data):
            count = 1
            while i + 1 < len(data) and data[i] == data[i + 1]:
                i += 1
                count += 1
            compressed_data.append(data[i])
            compressed_data.append(count)
            i += 1
        return bytes(compressed_data)
    except Exception as e:
        print(f"Error during RLE compression: {e}")
        return None

# Combine all compression methods: Base256 -> zlib -> RLE -> Dictionary
def combine_compress(input_file, output_file, dictionary_file=None):
    try:
        # Step 1: Apply Base256 Compression (no change)
        base256_data = base256_compress(input_file)
        if base256_data is None:
            return

        # Step 2: Apply zlib Compression
        zlib_compressed_data = zlib_compress(base256_data)
        if zlib_compressed_data is None:
            return

        # Step 3: Apply RLE Compression
        rle_compressed_data = rle_compress(zlib_compressed_data)
        if rle_compressed_data is None:
            return

        # Step 4: Apply Dictionary Compression if dictionary file is provided
        if dictionary_file:
            dictionary = load_dictionary(dictionary_file)
            if not dictionary:
                return
            text = rle_compressed_data.decode('latin1')  # decoding to string for dictionary compression
            final_compressed_data = dictionary_compress(text, dictionary).encode('latin1')
        else:
            final_compressed_data = rle_compressed_data

        # Write the final compressed data to the output file
        with open(output_file, 'wb') as f_out:
            f_out.write(final_compressed_data)

        print(f"All compression methods applied. Data saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred during combined compression: {e}")

# 1. Base256 Decompression (Identity decompression)
def base256_decompress(data):
    try:
        return data  # No change in Base256 decompression
    except Exception as e:
        print(f"Error during Base256 decompression: {e}")
        return None

# 2. zlib Decompression
def zlib_decompress(data):
    try:
        decompressed_data = paq.decompress(data)
        return decompressed_data
    except Exception as e:
        print(f"Error during zlib decompression: {e}")
        return None

# 3. Run-Length Encoding (RLE) Decompression
def rle_decompress(data):
    try:
        decompressed_data = bytearray()
        i = 0
        while i < len(data):
            byte = data[i]
            count = data[i + 1]
            decompressed_data.extend([byte] * count)
            i += 2
        return bytes(decompressed_data)
    except Exception as e:
        print(f"Error during RLE decompression: {e}")
        return None

# Combine all decompression methods: Dictionary -> RLE -> zlib -> Base256
def combine_decompress(input_file, output_file, dictionary_file=None):
    try:
        with open(input_file, 'rb') as f_in:
            compressed_data = f_in.read()

        # Step 1: Apply Dictionary Decompression if dictionary file is provided
        if dictionary_file:
            dictionary = load_dictionary(dictionary_file)
            if not dictionary:
                return
            text = compressed_data.decode('latin1')  # decoding to string for dictionary decompression
            decompressed_data = dictionary_decompress(text, dictionary).encode('latin1')
        else:
            decompressed_data = compressed_data

        # Step 2: Apply RLE Decompression
        rle_decompressed_data = rle_decompress(decompressed_data)
        if rle_decompressed_data is None:
            return

        # Step 3: Apply zlib Decompression
        zlib_decompressed_data = zlib_decompress(rle_decompressed_data)
        if zlib_decompressed_data is None:
            return

        # Step 4: Apply Base256 Decompression (no change)
        final_decompressed_data = base256_decompress(zlib_decompressed_data)
        if final_decompressed_data is None:
            return

        # Write the final decompressed data to the output file
        with open(output_file, 'wb') as f_out:
            f_out.write(final_decompressed_data)

        print(f"Data decompressed and saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred during combined decompression: {e}")

# Main function to handle compression and decompression options
def main():
    while True:
        print("\nChoose an option:")
        print("1. Compress a file")
        print("2. Decompress a file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_file = input("Enter the input file path to compress (e.g., file.txt): ")
            output_file = input("Enter the output file path for compressed data (e.g., file.b): ")
            dictionary_file = input("Enter the dictionary file path (e.g., dictionary.txt) [Press Enter if not using dictionary]: ")

            if dictionary_file.strip():
                combine_compress(input_file, output_file, dictionary_file)
            else:
                combine_compress(input_file, output_file)

        elif choice == '2':
            input_file = input("Enter the input file path to decompress (e.g., file.b): ")
            output_file = input("Enter the output file path for decompressed data (e.g., file.txt): ")
            dictionary_file = input("Enter the dictionary file path (e.g., dictionary.txt) [Press Enter if not using dictionary]: ")

            if dictionary_file.strip():
                combine_decompress(input_file, output_file, dictionary_file)
            else:
                combine_decompress(input_file, output_file)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()