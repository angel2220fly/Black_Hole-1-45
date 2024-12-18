import os
import paq

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

def compress_file(dictionary_file, input_file, output_file):
    """Compresses the file."""
    word_to_index, _ = load_dictionary(dictionary_file)
    if word_to_index is None:
        return

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "wb") as outfile:
            data = infile.read()
            binary_data = ""

            words = data.split()
            for word in words:
                if word in word_to_index:
                    index = word_to_index[word]
                    binary_data += bin(index)[2:].zfill(20)  # 20-bit word index
                    binary_data += "10"  # Space marker
                else:
                    for char in word:
                        if char == '\n':
                            binary_data += "0000000000000000" # 16-bit newline (consistent length)
                        else:
                            binary_data += bin(ord(char))[2:].zfill(8) # 8-bit character code

            byte_data = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder="big")
            compressed_data = paq.compress(byte_data)
            outfile.write(compressed_data)
            print(f"File compressed and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error: Unable to compress file. Details: {e}")


def decompress_file(dictionary_file, input_file, output_file):
    """Decompresses the file."""
    _, index_to_word = load_dictionary(dictionary_file)
    if index_to_word is None:
        return

    try:
        with open(input_file, "rb") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            compressed_data = infile.read()
            decompressed_data = paq.decompress(compressed_data)
            binary_data = bin(int.from_bytes(decompressed_data, byteorder="big"))[2:]
            binary_data = binary_data.zfill(len(decompressed_data) * 8)

            decompressed_text = ""
            i = 0
            while i < len(binary_data):
                if binary_data[i:i+16] == "0000000000000000": # Newline
                    decompressed_text += "\n"
                    i += 16
                elif binary_data[i:i+2] == "10":  #Space
                    decompressed_text += " "
                    i += 2
                else:  # Word index or character
                    try:
                        index = int(binary_data[i:i+20], 2)
                        if index in index_to_word:
                            decompressed_text += index_to_word[index] + " "
                            i += 20
                        else: # Handle invalid index (likely a character)
                            char_code = int(binary_data[i:i+8], 2)
                            decompressed_text += chr(char_code)
                            i += 8
                    except ValueError:
                        print(f"Error: Invalid code at position {i}.")
                        break

            outfile.write(decompressed_text.strip())
            print(f"File decompressed and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: Compressed file '{input_file}' not found.")
    except Exception as e:
        print(f"Error: Unable to decompress file. Details: {e}")

def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice: ")

    if choice == '1':  # Compression
        dictionary_file =  "Dictionary.txt"
        input_file = input("Enter the name of the input file to compress: ")
        output_file = input_file+".b"
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