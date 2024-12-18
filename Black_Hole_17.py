import os
import paq
import struct

def load_dictionary(dictionary_file):
    """Loads the dictionary."""
    try:
        word_to_index = {}
        index_to_word = {}
        with open(dictionary_file, "r", encoding="utf-8") as f:
            for index, line in enumerate(f):
                word = line.strip()
                if word:
                    word_to_index[word] = index
                    index_to_word[index] = word
        return word_to_index, index_to_word
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        return None, None
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return None, None


def compress_file(dictionary_file, input_file, output_file):
    """Compresses the file."""
    word_to_index, _ = load_dictionary(dictionary_file)
    if word_to_index is None:
        return

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "wb") as outfile:
            data = infile.read()
            encoded_data = bytearray()

            for char in data:
                if char.isspace():  # space or newline
                    if char == '\n':
                        encoded_data.append(0x0A)  # newline
                    else:
                        encoded_data.append(ord(' '))  # space
                else:  # other characters
                    word = ""
                    while char and not char.isspace():
                        word += char
                        try:
                            char = next(iter(data))  # consume next character
                        except StopIteration:
                            char = None
                            break  # end of file
                    if word:
                        if word in word_to_index:
                            index = word_to_index[word]
                            encoded_data.extend(struct.pack(">I", index))
                        else:
                            for c in word:
                                encoded_data.append(ord(c))  # encode characters individually

            compressed_data = paq.compress(bytes(encoded_data))
            outfile.write(compressed_data)
            print(f"File compressed and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error compressing file: {e}")



def decompress_file(dictionary_file, input_file, output_file):
    """Decompresses the file."""
    _, index_to_word = load_dictionary(dictionary_file)
    if index_to_word is None:
        return

    try:
        with open(input_file, "rb") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            compressed_data = infile.read()
            decompressed_data = paq.decompress(compressed_data)
            decoded_text = ""
            i = 0
            while i < len(decompressed_data):
                byte = decompressed_data[i]
                if byte == ord(' '):
                    decoded_text += " "
                    i += 1
                elif byte == 0x0A:
                    decoded_text += "\n"
                    i += 1
                else:
                    word = ""
                    word += chr(byte)
                    i += 1
                    while i < len(decompressed_data) and decompressed_data[i] not in (ord(' '), 0x0A):
                        word += chr(decompressed_data[i])
                        i += 1
                    if word:
                        decoded_text += word

            outfile.write(decoded_text.strip())
            print(f"File decompressed and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: Compressed file '{input_file}' not found.")
    except Exception as e:
        print(f"Error decompressing file: {e}")


def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice: ")

    if choice == '1':  # Compression
        dictionary_file = "Dictionary.txt"
        input_file = input("Enter the name of the input file to compress: ")
        output_file = input_file + ".b"
        compress_file(dictionary_file, input_file, output_file)

    elif choice == '2':  # Decompression
        dictionary_file = "Dictionary.txt"
        input_file = input("Enter the name of the compressed file: ")
        output_file = input_file[:-2]
        decompress_file(dictionary_file, input_file, output_file)

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
