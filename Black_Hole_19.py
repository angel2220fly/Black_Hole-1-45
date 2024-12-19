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
        output_file = input_file + ".b"
        compress_file(input_file, output_file)
    elif choice == '2':
        input_file = input("Enter the compressed file: ")
        output_file = input_file[:-2]  # Remove ".paq" extension
        decompress_file(input_file, output_file)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()