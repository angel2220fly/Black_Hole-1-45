import os
import struct
print("Created by Jurijus Pacalovas.")
print("Black_Hole_17")
print("This software is for compression of words.")

try:
    import paq
except ImportError:
    print("Error: The 'paq' library is not installed. Please install it using 'pip install paq8px'.")
    exit()

def load_dictionary(dictionary_file, encoding="utf-8"):
    """Loads the dictionary, handling potential errors more gracefully."""
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

def compress_file(dictionary_file, input_file, output_file, encoding="utf-8"):
    word_to_index, _ = load_dictionary(dictionary_file, encoding)
    if word_to_index is None:
        return

    try:
        with open(input_file, "r", encoding=encoding) as infile, open(output_file, "wb") as outfile:
            text = infile.read()
            lines = text.splitlines()
            encoded_data = bytearray()
            for line in lines:
                words = line.split()
                for idx, word in enumerate(words):
                    if word in word_to_index:
                        # Encode dictionary word (00)
                        encoded_data.append(0x00)
                        index = word_to_index[word]
                        encoded_data.extend(struct.pack(">I", index))
                    else:
                        # Encode non-dictionary word (01)
                        encoded_data.append(0x01)
                        try:
                            encoded_data.extend(word.encode('utf-8'))  # Safely encode the word
                        except UnicodeEncodeError as e:
                            print(f"Error encoding word '{word}': {e}")
                            continue
                        encoded_data.append(0x00)  # End of non-dictionary word
                    
                    # Add space (0x03) if not the last word
                    if idx < len(words) - 1:
                        encoded_data.append(0x03)  # Space between words
                
                encoded_data.append(0x02)  # End of line (0x02 represents a newline, binary 10)
            
            compressed_data = paq.compress(bytes(encoded_data))
            outfile.write(compressed_data)
            print(f"File compressed and saved as '{output_file}'")
    except (FileNotFoundError, IOError) as e:
        print(f"Error compressing file: {e}")

def decompress_file(dictionary_file, input_file, output_file, encoding="utf-8"):
    _, index_to_word = load_dictionary(dictionary_file, encoding)
    if index_to_word is None:
        return

    try:
        with open(input_file, "rb") as infile, open(output_file, "w", encoding=encoding) as outfile:
            compressed_data = infile.read()
            decompressed_data = paq.decompress(compressed_data)
            decoded_text = ""
            i = 0
            while i < len(decompressed_data):
                flag = decompressed_data[i]
                i += 1
                if flag == 0x00:  # Dictionary word
                    index = struct.unpack(">I", decompressed_data[i:i+4])[0]
                    decoded_text += index_to_word.get(index, "<unknown>")
                    i += 4
                elif flag == 0x01:  # Non-dictionary word
                    word = ""
                    while i < len(decompressed_data) and decompressed_data[i] != 0x00:
                        word += chr(decompressed_data[i])
                        i += 1
                    decoded_text += word
                    i += 1  # Skip the 0x00
                elif flag == 0x02:  # End of line (0x02 represents a newline, binary 10)
                    decoded_text += "\n"
                elif flag == 0x03:  # Space (0x03 represents space, binary 11)
                    decoded_text += " "

            outfile.write(decoded_text)
            print(f"File decompressed and saved as '{output_file}'")
    except (FileNotFoundError, IOError) as e:
        print(f"Error decompressing file: {e}")

def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice: ")
    dictionary_file = "Dictionary.txt"
    encoding = "utf-8"

    if choice == '1':
        input_file = input("Enter the input file to compress: ")
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return

        output_file = input_file + ".b"
        compress_file(dictionary_file, input_file, output_file, encoding)
    elif choice == '2':
        input_file = input("Enter the compressed file: ")
        if not os.path.exists(input_file):
            print(f"Error: Compressed file '{input_file}' not found.")
            return

        output_file = input_file[:-2]
        decompress_file(dictionary_file, input_file, output_file, encoding)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

import heapq
from collections import Counter
import struct
import os
print("Created by Jurijus Pacalovas.")
print("This software for compression words.")

# Huffman Node
class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    """Build Huffman tree from frequencies."""
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(tree, prefix="", codes=None):
    """Generate Huffman codes."""
    if codes is None:
        codes = {}
    if tree.char is not None:
        codes[tree.char] = prefix
    else:
        generate_huffman_codes(tree.left, prefix + "0", codes)
        generate_huffman_codes(tree.right, prefix + "1", codes)
    return codes


def huffman_encode(data, codes):
    """Encode data using Huffman codes."""
    return ''.join(codes[word] for word in data.split())


def huffman_decode(encoded_data, tree):
    """Decode data using the Huffman tree."""
    decoded_data = []
    current_node = tree
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree
    return ' '.join(decoded_data)


def compress_with_paq(data):
    """Compress data using the `paq` library."""
    try:
        import paq
        compressed_data = paq.compress(data.encode('utf-8'))
        return compressed_data
    except ImportError:
        print("Error: The 'paq' library is not installed. Install it using 'pip install paq8px'.")
        exit()


def decompress_with_paq(data):
    """Decompress data using the `paq` library."""
    try:
        import paq
        decompressed_data = paq.decompress(data).decode('utf-8')
        return decompressed_data
    except ImportError:
        print("Error: The 'paq' library is not installed. Install it using 'pip install paq8px'.")
        exit()


def compress_file(input_file, output_file):
    """Compress a file using Huffman coding and paq."""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = infile.read()

        # Frequency analysis
        word_frequencies = Counter(data.split())
        tree = build_huffman_tree(word_frequencies)
        codes = generate_huffman_codes(tree)

        # Encode data with Huffman
        encoded_data = huffman_encode(data, codes)

        # Compress with paq
        compressed_data = compress_with_paq(encoded_data)

        # Save compressed data and Huffman tree
        with open(output_file, 'wb') as outfile:
            outfile.write(compressed_data)

        with open("huffman_tree.pkl", "wb") as tree_file:
            import pickle
            pickle.dump(tree, tree_file)

        print(f"File compressed and saved as '{output_file}'")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


def decompress_file(input_file, output_file):
    """Decompress a file using Huffman coding and paq."""
    try:
        with open("huffman_tree.pkl", "rb") as tree_file:
            import pickle
            tree = pickle.load(tree_file)

        with open(input_file, 'rb') as infile:
            compressed_data = infile.read()

        # Decompress with paq
        encoded_data = decompress_with_paq(compressed_data)

        # Decode data with Huffman
        decoded_data = huffman_decode(encoded_data, tree)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(decoded_data)

        print(f"File decompressed and saved as '{output_file}'")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error during decompression: {e}")


def main():
    """Main function for user interaction."""
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice: ")

    if choice == '1':
        input_file = input("Enter the input file to compress: ")
        output_file = input_file + ".b2"
        compress_file(input_file, output_file)
    elif choice == '2':
        input_file = input("Enter the compressed file: ")
        output_file = input_file[:-3]  # Remove ".paq" extension
        decompress_file(input_file, output_file)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()