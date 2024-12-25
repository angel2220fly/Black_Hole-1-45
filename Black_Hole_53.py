import os
import struct
import mimetypes
import paq

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

def load_dictionary(dictionary_file, encoding="utf-8"):
    word_to_index = {}
    try:
        with open(dictionary_file, "r", encoding=encoding) as f:
            for index, line in enumerate(f):
                word = line.strip().lower()  # Case-insensitive
                word_to_index[word] = index
        return word_to_index
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        return None
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return None


def compress_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    try:
        word_to_index = load_dictionary(dictionary_file, encoding)
        if word_to_index is None:
            return

        mime_type, _ = mimetypes.guess_type(input_filename)
        if mime_type == "text/plain":
            compress_text_file(input_filename, output_filename, word_to_index, encoding)
        else:
            compress_binary_file(input_filename, output_filename)
    except Exception as e:
        print(f"An error occurred during compression: {e}")

def compress_text_file(input_filename, output_filename, word_to_index, encoding="utf-8"):
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
        print(f"Error during text compression: {e}")


def compress_binary_file(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as infile:
            data = infile.read()

        # Use PAQ compression for all other binary files
        compressed_data = paq.compress(data)

        with open(output_filename, "wb") as outfile:
            outfile.write(compressed_data)
            print(f"Compressed binary file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during binary compression: {e}")


def extract_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    try:
        mime_type, _ = mimetypes.guess_type(output_filename)  # Check output file type
        if mime_type == "text/plain":
            extract_text_file(input_filename, output_filename, dictionary_file, encoding)
        else:
            extract_binary_file(input_filename, output_filename)
    except Exception as e:
        print(f"An error occurred during extraction: {e}")


def extract_text_file(input_filename, output_filename, dictionary_file, encoding="utf-8"):
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
        print(f"Error during text extraction: {e}")


def extract_binary_file(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as infile:
            compressed_data = infile.read()

        # Decompress binary file using PAQ
        decompressed_data = paq.decompress(compressed_data)

        if decompressed_data is None:
            print(f"Error: Decompression failed for '{input_filename}'")
            return

        with open(output_filename, "wb") as outfile:
            outfile.write(decompressed_data)
            print(f"Extracted binary file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during binary extraction: {e}")


def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Extract a file")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            input_file = input("Enter the name of the file to compress: ").strip()
            output_file = input_file + ".b"
            compress_file(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the file to extract: ").strip()
            output_file = input_file[:-2]  # remove the ".b"
            extract_file(input_file, output_file)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()