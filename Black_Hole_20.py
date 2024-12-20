import os
import heapq
from collections import Counter
import pickle
from paq import compress as paq_compress, decompress as paq_decompress

print("Created by Jurijus Pacalovas.")
print("This software supports multiple compression methods, including Huffman coding, PAQ, and replacement-based compression.")

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

# Compression Methods
def compress_file(input_file, output_file, method="huffman"):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = infile.read()

        if method == "huffman":
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

        elif method == "replacement":
            # Simple replacement-based compression
            MAX_VALUE = 255
            REPLACEMENT_VALUE = 254
            compressed_data = bytearray()
            replacements = 0
            for byte in data.encode('utf-8'):
                if byte == MAX_VALUE:
                    compressed_data.append(REPLACEMENT_VALUE)
                    replacements += 1
                else:
                    compressed_data.append(byte)

            if replacements > 0:
                compressed_data = compressed_data[:-1]  # Reduce by 1 byte

            # Save compressed data
            with open(output_file, 'wb') as outfile:
                outfile.write(compressed_data)

            print(f"File compressed using replacement-based method and saved as '{output_file}'")

        else:
            print("Invalid compression method.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error during compression: {e}")

def decompress_file(input_file, output_file, method="huffman"):
    try:
        if method == "huffman":
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

        elif method == "replacement":
            MAX_VALUE = 255
            REPLACEMENT_VALUE = 254

            with open(input_file, 'rb') as infile:
                compressed_data = infile.read()

            decompressed_data = bytearray()
            for byte in compressed_data:
                if byte == REPLACEMENT_VALUE:
                    decompressed_data.append(MAX_VALUE)
                else:
                    decompressed_data.append(byte)

            with open(output_file, 'wb') as outfile:
                outfile.write(decompressed_data)

            print(f"File decompressed using replacement-based method and saved as '{output_file}'")

        else:
            print("Invalid decompression method.")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error during decompression: {e}")

# Main Function
def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        input_file = input("Enter the input file to compress: ").strip()
        output_file = input("Enter the output file name: ").strip()

        print("Choose a compression method:")
        print("1. Huffman")
        print("2. Replacement-based")
        method_choice = input("Enter your choice: ").strip()

        if method_choice == '1':
            compress_file(input_file, output_file, method="huffman")
        elif method_choice == '2':
            compress_file(input_file, output_file, method="replacement")
        else:
            print("Invalid compression method. Please choose 1 or 2.")

    elif choice == '2':
        input_file = input("Enter the compressed file to decompress: ").strip()
        output_file = input("Enter the output file name: ").strip()

        print("Choose a decompression method:")
        print("1. Huffman")
        print("2. Replacement-based")
        method_choice = input("Enter your choice: ").strip()

        if method_choice == '1':
            decompress_file(input_file, output_file, method="huffman")
        elif method_choice == '2':
            decompress_file(input_file, output_file, method="replacement")
        else:
            print("Invalid decompression method. Please choose 1 or 2.")

    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()