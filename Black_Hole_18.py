import os
import heapq
import struct
from collections import defaultdict, Counter

try:
    import paq
except ImportError:
    print("Error: The 'paq' library is not installed. Please install it using 'pip install paq8px'.")
    exit()

print("Created by Jurijus Pacalovas.")
print("Black_Hole_18 - Dictionary + Huffman + PAQ")

# Huffman Node for the tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman tree and generate codes
def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def generate_huffman_codes(tree, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if tree is not None:
        if tree.char is not None:  # Leaf node
            codebook[tree.char] = prefix
        generate_huffman_codes(tree.left, prefix + "0", codebook)
        generate_huffman_codes(tree.right, prefix + "1", codebook)
    return codebook

# Load dictionary file
def load_dictionary(dictionary_file):
    try:
        with open(dictionary_file, "r", encoding="utf-8") as f:
            return {word.strip(): idx for idx, word in enumerate(f) if word.strip()}
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        return {}

# Compress with dictionary + Huffman + PAQ
def compress_file(dictionary_file, input_file, output_file):
    # Load dictionary
    word_to_index = load_dictionary(dictionary_file)
    if not word_to_index:
        print("Error: Dictionary is empty or not loaded.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            words = infile.read().split()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    # Replace words with dictionary indices
    compressed_indices = []
    for word in words:
        if word in word_to_index:
            compressed_indices.append(word_to_index[word])
        else:
            compressed_indices.append(-1)  # Marker for non-dictionary words

    # Huffman encoding
    frequencies = Counter(compressed_indices)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Encode the data
    huffman_encoded_data = "".join(huffman_codes[idx] for idx in compressed_indices if idx in huffman_codes)

    # Convert to bytes
    byte_data = int(huffman_encoded_data, 2).to_bytes((len(huffman_encoded_data) + 7) // 8, byteorder="big")

    # PAQ compression
    compressed_data = paq.compress(byte_data)

    # Write to output file
    with open(output_file, "wb") as outfile:
        outfile.write(compressed_data)

    print(f"File successfully compressed and saved as '{output_file}'.")

# Decompress with dictionary + Huffman + PAQ
def decompress_file(dictionary_file, input_file, output_file):
    # Load dictionary
    index_to_word = {idx: word for word, idx in load_dictionary(dictionary_file).items()}
    if not index_to_word:
        print("Error: Dictionary is empty or not loaded.")
        return

    try:
        with open(input_file, "rb") as infile:
            compressed_data = infile.read()
    except FileNotFoundError:
        print(f"Error: Compressed file '{input_file}' not found.")
        return

    # PAQ decompression
    decompressed_bytes = paq.decompress(compressed_data)

    # Convert bytes to binary string
    binary_data = bin(int.from_bytes(decompressed_bytes, byteorder="big"))[2:].zfill(len(decompressed_bytes) * 8)

    # Decode Huffman
    decoded_indices = []
    huffman_tree = build_huffman_tree(Counter(index_to_word.keys()))  # Rebuild tree
    current_node = huffman_tree
    for bit in binary_data:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node.char is not None:  # Leaf node
            decoded_indices.append(current_node.char)
            current_node = huffman_tree

    # Convert indices to words
    decoded_words = [index_to_word.get(idx, "<unknown>") for idx in decoded_indices]

    # Write decompressed data to output file
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(" ".join(decoded_words))

    print(f"File successfully decompressed and saved as '{output_file}'.")

# Main function
def main():
    dictionary_file = "Dictionary.txt"

    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice: ")

    if choice == "1":
        input_file = input("Enter the input file to compress: ")
        output_file = input_file + ".b"
        compress_file(dictionary_file, input_file, output_file)
    elif choice == "2":
        input_file = input("Enter the compressed file: ")
        output_file = input_file.replace(".b", "_decompressed.txt")
        decompress_file(dictionary_file, input_file, output_file)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()