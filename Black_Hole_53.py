import os
import struct
import paq
print("Created by Jurijus Pacalovas.")
print("Black_Hole_53")

# Dictionary-based compression utilities
def load_dictionary(dictionary_file, encoding="utf-8"):
    word_to_index = {}
    try:
        with open(dictionary_file, "r", encoding=encoding) as f:
            for index, line in enumerate(f):
                word = line.strip().lower()  # Case-insensitive
                word_to_index[word] = index
        return word_to_index
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return None

# Load Pi digits from a file
def load_pi_digits(file_name="PI_10M.txt"):
    try:
        with open(file_name, "r") as file:
            pi_digits = file.read().strip()  # Read and strip any trailing whitespace
            return pi_digits
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None

# Compress with Pi (XOR operation with Pi digits)
def compress_with_pi(data, pi_digits):
    pi_sequence = [int(d) for d in pi_digits[:len(data)]]
    return bytes([b ^ p for b, p in zip(data, pi_sequence)])

# Compress text file with dictionary, Pi, and PAQ
def compress_text_file(input_filename, output_filename, dictionary_file="Dictionary.txt", pi_digits=None, encoding="utf-8"):
    word_to_index = load_dictionary(dictionary_file, encoding)
    if word_to_index is None:
        return
    
    try:
        with open(input_filename, "r", encoding=encoding) as infile:
            data = infile.read()

        compressed_data = bytearray()
        words = data.split()

        for word in words:
            normalized_word = word.lower()
            if normalized_word in word_to_index:
                index = word_to_index[normalized_word]
                compressed_data.append(0x00)  # Dictionary flag
                compressed_data.extend(struct.pack(">I", index))
            else:
                compressed_data.append(0x01)  # Non-dictionary word
                compressed_data.extend(word.encode(encoding))

            compressed_data.append(0x02)  # Space flag

        # Apply PAQ compression
        compressed_data = paq.compress(bytes(compressed_data))
        if pi_digits:
            compressed_data = compress_with_pi(compressed_data, pi_digits)

        with open(output_filename, "wb") as outfile:
            outfile.write(compressed_data)
            print(f"Compressed text file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during text compression: {e}")

# Compress binary file with Pi and PAQ
def compress_binary_file(input_filename, output_filename, pi_digits=None):
    try:
        with open(input_filename, "rb") as infile:
            data = infile.read()

        compressed_data = paq.compress(data)
        if pi_digits:
            compressed_data = compress_with_pi(compressed_data, pi_digits)

        with open(output_filename, "wb") as outfile:
            outfile.write(compressed_data)
            print(f"Compressed binary file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during binary compression: {e}")

# Extract binary file
def extract_binary_file(input_filename, output_filename, pi_digits=None):
    try:
        with open(input_filename, "rb") as infile:
            compressed_data = infile.read()

        # Reverse Pi compression
        if pi_digits:
            compressed_data = bytearray([b ^ int(pi_digits[i % len(pi_digits)]) for i, b in enumerate(compressed_data)])

        # Reverse PAQ compression
        decompressed_data = paq.decompress(bytes(compressed_data))

        with open(output_filename, "wb") as outfile:
            outfile.write(decompressed_data)
            print(f"Extracted binary file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during binary extraction: {e}")

# Extract text file
def extract_text_file(input_filename, output_filename, dictionary_file="Dictionary.txt", pi_digits=None, encoding="utf-8"):
    word_to_index = load_dictionary(dictionary_file, encoding)
    if word_to_index is None:
        return

    try:
        with open(input_filename, "rb") as infile:
            compressed_data = infile.read()

        # Reverse Pi compression
        if pi_digits:
            compressed_data = bytearray([b ^ int(pi_digits[i % len(pi_digits)]) for i, b in enumerate(compressed_data)])

        decompressed_data = paq.decompress(bytes(compressed_data))

        # Process the decompressed data
        decompressed_text = []
        i = 0
        while i < len(decompressed_data):
            if decompressed_data[i] == 0x00:  # Dictionary word
                index = struct.unpack(">I", decompressed_data[i + 1:i + 5])[0]
                for word, word_index in word_to_index.items():
                    if word_index == index:
                        decompressed_text.append(word)
                        break
                i += 5
            elif decompressed_data[i] == 0x01:  # Non-dictionary word
                start = i + 1
                while i < len(decompressed_data) and decompressed_data[i] != 0x02:
                    i += 1
                decompressed_text.append(decompressed_data[start:i].decode(encoding))
            i += 1

        with open(output_filename, "w", encoding=encoding) as outfile:
            outfile.write(' '.join(decompressed_text))
            print(f"Extracted text file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during text extraction: {e}")

# Main function
def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Extract a file")
    print("3. Exit")

    # Load Pi digits from the file
    pi_digits = load_pi_digits("PI_10M.txt")
    if not pi_digits:
        print("Exiting program due to missing Pi file.")
        return

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()

            _, ext = os.path.splitext(input_file)
            if ext.lower() in ['.txt', '.csv']:
                compress_text_file(input_file, output_file, pi_digits=pi_digits)
            else:
                compress_binary_file(input_file, output_file, pi_digits=pi_digits)
        elif choice == '2':
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()

            _, ext = os.path.splitext(input_file)
            if ext.lower() in ['.txt', '.csv']:
                extract_text_file(input_file, output_file, pi_digits=pi_digits)
            else:
                extract_binary_file(input_file, output_file, pi_digits=pi_digits)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()