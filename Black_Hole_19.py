import os
import struct
import random
import paq

print("Created by Jurijus Pacalovas.")
print("Black_Hole_19")
print("This software compresses any data, focusing on dictionary-based words.")

# Function to load the dictionary from the file
def load_dictionary(dictionary_file, encoding="utf-8"):
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

# Function to generate the table data for compression
def generate_headings_and_chunks():
    file_name = input("Enter the name of the file to save the output (e.g., table4.txt): ").strip()
    if not file_name.endswith(".txt"):
        print("Error: Only '.txt' files are allowed.")
        return False

    if os.path.exists(file_name):
        print(f"The file '{file_name}' already exists. Skipping generation.")
        return True

    try:
        with open(file_name, "w") as file:
            max_headings = 2**17
            chunk_size = 256
            random.seed(42)

            for heading in range(max_headings):
                heading_bits = f"{heading:017b}"
                chunk = [bytes([random.randint(0, 255) for _ in range(32)]) for _ in range(chunk_size)]
                chunk_bits = ''.join(''.join(f"{byte:08b}" for byte in position) for position in chunk)
                file.write(f"{heading_bits} {chunk_bits}\n")

        print(f"Data generated and saved to '{file_name}'.")
        return True
    except Exception as e:
        print(f"An error occurred during data generation: {e}")
        return False

# Function to compress the file
def compress_file_with_both_algorithms(dictionary_file, input_filename, output_filename, encoding="utf-8"):
    if not input_filename.endswith(".txt"):
        print("Error: Only '.txt' files are allowed for input.")
        return

    word_to_index, _ = load_dictionary(dictionary_file, encoding)
    if word_to_index is None:
        return

    try:
        with open(input_filename, 'rb') as infile:
            data = infile.read()

        encoded_data = bytearray()
        words = data.split(b" ")

        for word in words:
            try:
                decoded_word = word.decode(encoding)
                if decoded_word in word_to_index:
                    index = word_to_index[decoded_word]
                    if index > 3:
                        encoded_data.append(0x00)
                        encoded_data.extend(struct.pack(">I", index))
                    else:
                        encoded_data.append(0x01)
                        encoded_data.extend(word)
                        encoded_data.append(0x20)
                else:
                    encoded_data.append(0x01)
                    encoded_data.extend(word)
                    encoded_data.append(0x20)
            except UnicodeDecodeError:
                encoded_data.append(0x01)
                encoded_data.extend(word)
                encoded_data.append(0x20)

        compressed_data = paq.compress(bytes(encoded_data))

        with open(output_filename, "wb") as outfile:
            outfile.write(compressed_data)
            print(f"File compressed and saved as '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred during compression: {e}")

# Function to decompress the file
def decompress_file_with_both_algorithms(dictionary_file, input_filename, output_filename, encoding="utf-8"):
    if not output_filename.endswith(".txt"):
        print("Error: Decompressed output must be a '.txt' file.")
        return

    _, index_to_word = load_dictionary(dictionary_file, encoding)
    if index_to_word is None:
        return

    try:
        with open(input_filename, 'rb') as infile:
            compressed_data = infile.read()

        decompressed_data = paq.decompress(compressed_data)
        decoded_text = bytearray()
        i = 0

        while i < len(decompressed_data):
            flag = decompressed_data[i]
            i += 1

            if flag == 0x00:
                index = struct.unpack(">I", decompressed_data[i:i+4])[0]
                word = index_to_word.get(index, "<unknown>").encode(encoding)
                decoded_text.extend(word + b" ")
                i += 4
            elif flag == 0x01:
                word = bytearray()
                while i < len(decompressed_data) and decompressed_data[i] != 0x20:
                    word.append(decompressed_data[i])
                    i += 1
                decoded_text.extend(word + b" ")
                i += 1

        if len(decoded_text) > 0:
            decoded_text = decoded_text[:-1]

        with open(output_filename, 'wb') as outfile:
            outfile.write(decoded_text)
            print(f"File decompressed and saved as '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: Compressed file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred during decompression: {e}")

# Main function
def main():
    print("Choose an option:")
    print("1. Generate data file")
    print("2. Compress a file")
    print("3. Decompress a file")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        if not generate_headings_and_chunks():
            print("Data generation failed.")
    elif choice == '2':
        input_file = input("Enter the name of the input file (e.g., table4.txt): ")
        output_file = input("Enter the name of the output file (e.g., table4.b): ")
        compress_file_with_both_algorithms("Dictionary.txt", input_file, output_file)
    elif choice == '3':
        input_file = input("Enter the name of the compressed file to decompress (e.g., table4.b): ")
        output_file = input("Enter the name of the output file (e.g., table4_decompressed.txt): ")
        decompress_file_with_both_algorithms("Dictionary.txt", input_file, output_file)
    elif choice == '4':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
