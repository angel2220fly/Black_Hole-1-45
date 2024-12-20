import heapq
from collections import Counter
import pickle
import os

print("Created by Jurijus Pacalovas.")
print("This software compresses a file using Huffman coding and keeps the smallest compressed file after PAQ compression.")

# Huffman Node
class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

# Huffman Functions
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
    return ''.join(codes[char] for char in data)

def huffman_decode(encoded_data, tree):
    decoded_data = []
    current_node = tree
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree
    return bytes(decoded_data)

# Huffman Compression
def compress_file_huffman(input_file, output_file):
    try:
        with open(input_file, 'rb') as infile:  # Read in binary mode
            data = infile.read()

        # Count frequencies of bytes (0-255)
        frequencies = Counter(data)
        tree = build_huffman_tree(frequencies)
        codes = generate_huffman_codes(tree)
        encoded_data = huffman_encode(data, codes)

        # Convert the encoded data to a byte string
        encoded_data_bytes = ''.join(encoded_data)
        byte_data = bytearray()
        for i in range(0, len(encoded_data_bytes), 8):
            byte_data.append(int(encoded_data_bytes[i:i+8], 2))

        # Save compressed file and Huffman tree
        with open(output_file, 'wb') as outfile:
            outfile.write(byte_data)
        with open(output_file + ".tree", 'wb') as tree_file:
            pickle.dump(tree, tree_file)

        print(f".M1 file compressed and saved as '{output_file}'")
        print(f"Compressed file size (M1): {os.path.getsize(output_file)} bytes")
        return os.path.getsize(output_file)
    except Exception as e:
        print(f"Error during .M1 compression: {e}")
        return float('inf')

# Huffman Decompression
def decompress_file_huffman(input_file, output_file):
    try:
        with open(input_file + ".tree", 'rb') as tree_file:
            tree = pickle.load(tree_file)

        with open(input_file, 'rb') as infile:
            compressed_data = infile.read()

        # Convert byte data back to binary string
        binary_data = ''.join(format(byte, '08b') for byte in compressed_data)

        decoded_data = huffman_decode(binary_data, tree)

        with open(output_file, 'wb') as outfile:
            outfile.write(decoded_data)

        print(f"File decompressed using Huffman coding and saved as '{output_file}'")

    except Exception as e:
        print(f"Error during Huffman decompression: {e}")

# Main Function
def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        input_file = input("Enter the input file to compress: ").strip()
        output_file_base = input("Enter the base name for the output files: ").strip()

        # Perform compression using Huffman method
        size_m1 = compress_file_huffman(input_file, output_file_base + ".M1")

        print(f"Compressed file size (M1): {size_m1} bytes")

    elif choice == '2':
        input_file = input("Enter the compressed file to decompress: ").strip()
        output_file = input("Enter the output file name: ").strip()

        # Decompress using Huffman method
        if input_file.endswith(".M1"):
            decompress_file_huffman(input_file, output_file)
        else:
            print("Invalid compressed file format. Make sure the file ends with .M1")
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()