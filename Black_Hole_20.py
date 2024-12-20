import os
import heapq
from collections import Counter
import pickle
from paq import compress as paq_compress, decompress as paq_decompress

print("Created by Jurijus Pacalovas.")
print("This software supports Huffman coding for compression and decompression.")

# Huffman Node
class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

# Huffman Encoding
def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    return heap[0]

def generate_huffman_codes(tree, prefix="", codes=None):
    if codes is None:
        codes = {}
    if tree.char is not None:
        codes[tree.char] = prefix
    else:
        generate_huffman_codes(tree.left, prefix + "0", codes)
        generate_huffman_codes(tree.right, prefix + "1", codes)
    return codes

def huffman_encode(data, codes):
    return ''.join(codes[word] for word in data.split())

def huffman_decode(encoded_data, tree):
    decoded_data = []
    current_node = tree
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree
    return ' '.join(decoded_data)

# Compression
def compress_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = infile.read()

        # Frequency analysis and Huffman encoding
        word_frequencies = Counter(data.split())
        tree = build_huffman_tree(word_frequencies)
        codes = generate_huffman_codes(tree)
        encoded_data = huffman_encode(data, codes)

        # Further compress with PAQ
        compressed_data = paq_compress(encoded_data.encode('utf-8'))

        # Save compressed data and Huffman tree
        with open(output_file, 'wb') as outfile:
            outfile.write(compressed_data)

        with open(output_file + ".tree", 'wb') as tree_file:
            pickle.dump(tree, tree_file)

        print(f"File compressed using Huffman coding and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error during compression: {e}")

# Decompression
def decompress_file(input_file, output_file):
    try:
        # Load Huffman tree
        with open(input_file + ".tree", 'rb') as tree_file:
            tree = pickle.load(tree_file)

        with open(input_file, 'rb') as infile:
            compressed_data = infile.read()

        # Decompress with PAQ
        encoded_data = paq_decompress(compressed_data).decode('utf-8')

        # Decode data using Huffman tree
        decoded_data = huffman_decode(encoded_data, tree)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(decoded_data)

        print(f"File decompressed using Huffman coding and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error during decompression: {e}")

# Main Function
def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice (1 or 2): ").strip()

    input_file = input("Enter the input file name: ").strip()
    output_file = input("Enter the output file name: ").strip()

    if choice == '1':  # Compress
        compress_file(input_file, output_file + ".b")

    elif choice == '2':  # Decompress
        decompress_file(input_file, output_file)

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()