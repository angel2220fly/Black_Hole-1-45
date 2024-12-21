import os
import struct
import random
import paq

# 1. Generate Table4 File
def generate_table4(file_name="table4.txt"):
    """
    Generates a file with 17-bit headings and 256 positions (256 bits each) in a 256-byte chunk.
    """
    max_headings = 2**17  # 17-bit headings (0 to 2^17-1)
    chunk_size = 256  # Number of positions in the chunk

    try:
        with open(file_name, "w") as file:
            print("Generating table4 data...")
            random.seed(42)  # For reproducibility

            for heading in range(max_headings):
                heading_bits = f"{heading:017b}"  # Convert heading to 17-bit binary

                # Create a chunk of 256 positions (each with 256 bits, which is 32 bytes)
                chunk = [bytes([random.randint(0, 255) for _ in range(32)]) for _ in range(chunk_size)]

                # Convert each position in the chunk to binary (256 bits per position)
                chunk_bits = ''.join(''.join(f"{byte:08b}" for byte in position) for position in chunk)

                # Write the heading and the corresponding 256 positions
                file.write(f"{heading_bits} {chunk_bits}\n")

                # Optional: Limit the number of rows for testing
                if heading >= 1023:  # Generate only 1024 rows for faster testing
                    break

        print(f"Table4 data generated and saved to '{file_name}'.")
    except Exception as e:
        print(f"An error occurred during data generation: {e}")

# 2. Compression Function
def compress_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    """
    Compresses a file using dictionary-based compression and PAQ.
    """
    # Check if the input file exists and has a .txt extension
    if not os.path.isfile(input_filename) or not input_filename.endswith(".txt"):
        print(f"Error: The file '{input_filename}' is not a valid .txt file or does not exist.")
        return

    # Load dictionary
    def load_dictionary(dictionary_file):
        word_to_index = {}
        try:
            with open(dictionary_file, "r", encoding=encoding) as f:
                for index, line in enumerate(f):
                    word = line.strip().lower()  # Normalize to lowercase
                    word_to_index[word] = index
            return word_to_index
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            return None

    word_to_index = load_dictionary(dictionary_file)
    if word_to_index is None:
        return

    try:
        with open(input_filename, "rb") as infile:
            data = infile.read()

        # Split data into words
        words = data.split(b" ")  # Splits by space
        compressed_data = bytearray()

        for word in words:
            try:
                decoded_word = word.decode(encoding)
                normalized_word = decoded_word.lower()

                if normalized_word in word_to_index:
                    index = word_to_index[normalized_word]
                    # Determine case flag
                    if decoded_word.islower():
                        case_flag = 0x01  # All lowercase
                    elif decoded_word.isupper():
                        case_flag = 0x02  # All uppercase
                    elif decoded_word.istitle():
                        case_flag = 0x03  # First letter capitalized
                    else:
                        case_flag = 0x00  # Mixed case or non-dictionary word
                    compressed_data.append(0x00)  # Dictionary flag
                    compressed_data.append(case_flag)  # Case flag
                    compressed_data.extend(struct.pack(">I", index))
                else:
                    compressed_data.append(0x01)  # Non-dictionary word
                    compressed_data.extend(word)
                    compressed_data.append(0x20)  # Add space
            except UnicodeDecodeError:
                compressed_data.append(0x01)
                compressed_data.extend(word)
                compressed_data.append(0x20)  # Add space

        # PAQ compression
        final_compressed_data = paq.compress(bytes(compressed_data))

        with open(output_filename, "wb") as outfile:
            outfile.write(final_compressed_data)
            print(f"Compressed file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during compression: {e}")

# 3. Extraction Function
def extract_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    """
    Extracts a compressed file using PAQ decompression and dictionary decoding.
    """
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

        # PAQ decompression
        decompressed_data = paq.decompress(compressed_data)

        # Dictionary decoding
        decoded_data = bytearray()
        i = 0
        while i < len(decompressed_data):
            flag = decompressed_data[i]
            i += 1
            if flag == 0x00:  # Dictionary word
                case_flag = decompressed_data[i]  # Case flag
                i += 1
                index = struct.unpack(">I", decompressed_data[i:i+4])[0]
                word = index_to_word.get(index, "<unknown>")
                if case_flag == 0x01:
                    word = word.lower()
                elif case_flag == 0x02:
                    word = word.upper()
                elif case_flag == 0x03:
                    word = word.capitalize()
                decoded_data.extend(word.encode(encoding) + b" ")
                i += 4
            elif flag == 0x01:  # Non-dictionary word
                word = bytearray()
                while i < len(decompressed_data) and decompressed_data[i] != 0x20:
                    word.append(decompressed_data[i])
                    i += 1
                decoded_data.extend(word + b" ")
                i += 1

        # Save extracted data
        with open(output_filename, "wb") as outfile:
            outfile.write(decoded_data)
            print(f"Extracted file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during extraction: {e}")

# Main Menu
def main():
    print("Choose an option:")
    print("1. Generate table4 file")
    print("2. Compress a file")
    print("3. Extract a file")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1/2/3/4): ").strip()
        if choice == '1':
            generate_table4()
        elif choice == '2':
            input_file = input("Enter the name of the file to compress (e.g., table4.txt): ").strip()
            output_file = input("Enter the name of the compressed file (e.g., table4.b): ").strip()
            compress_file(input_file, output_file)
        elif choice == '3':
            input_file = input("Enter the name of the file to extract (e.g., table4.b): ").strip()
            output_file = input("Enter the name of the extracted file (e.g., table4_extracted.txt): ").strip()
            extract_file(input_file, output_file)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()