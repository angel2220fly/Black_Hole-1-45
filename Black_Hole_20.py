import heapq
from collections import Counter
import pickle
import struct
import paq
import os

print("Created by Jurijus Pacalovas.")
print("This software compresses a file using multiple methods and keeps only the smallest compressed file after PAQ compression.")

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

# Huffman Compression
def compress_file_huffman(input_file, output_file):
    try:
        with open(input_file, 'rb') as infile:  # Read in binary mode
            data = infile.read()

        # Count frequencies of bytes
        frequencies = Counter(data)
        tree = build_huffman_tree(frequencies)
        codes = generate_huffman_codes(tree)
        encoded_data = huffman_encode(data, codes)

        # Apply PAQ Compression
        compressed_data = paq.compress(encoded_data.encode('utf-8'))

        # Save compressed file and Huffman tree
        with open(output_file, 'wb') as outfile:
            outfile.write(compressed_data)
        with open(output_file + ".tree", 'wb') as tree_file:
            pickle.dump(tree, tree_file)

        print(f".M1 file compressed and saved as '{output_file}'")
        print(f"Compressed file size (M1): {os.path.getsize(output_file)} bytes")
        return os.path.getsize(output_file)
    except Exception as e:
        print(f"Error during .M1 compression: {e}")
        return float('inf')

# Word Replacement Compression
def compress_file_word(input_file, output_file, dictionary_file):
    try:
        # Load dictionary
        word_to_index = {}
        with open(dictionary_file, "r", encoding="utf-8") as dict_file:
            for index, word in enumerate(dict_file):
                word = word.strip()
                if word:
                    word_to_index[word] = index

        # Read input file in binary mode
        with open(input_file, "rb") as infile:
            text = infile.read()
            encoded_data = bytearray()
            for word in text.split():
                if word in word_to_index:
                    encoded_data.append(0x00)
                    encoded_data.extend(struct.pack(">I", word_to_index[word]))
                else:
                    encoded_data.append(0x01)
                    encoded_data.extend(word)
                    encoded_data.append(0x00)
            compressed_data = paq.compress(bytes(encoded_data))

        # Save compressed file
        with open(output_file, "wb") as outfile:
            outfile.write(compressed_data)

        print(f".b file compressed and saved as '{output_file}'")
        print(f"Compressed file size (b): {os.path.getsize(output_file)} bytes")
        return os.path.getsize(output_file)
    except Exception as e:
        print(f"Error during .b compression: {e}")
        return float('inf')

# Main Function
def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        input_file = input("Enter the input file to compress: ").strip()
        dictionary_file = "Dictionary.txt"
        output_file_base = input("Enter the base name for the output files: ").strip()

        # Perform compression using both methods
        size_m1 = compress_file_huffman(input_file, output_file_base + ".M1")
        size_b = compress_file_word(input_file, output_file_base + ".b", dictionary_file)

        # Keep only the smallest file after PAQ compression
        if size_m1 < size_b:
            os.remove(output_file_base + ".b")
            print(f"The smallest compressed file is: {output_file_base}.M1 ({size_m1} bytes)")
        else:
            os.remove(output_file_base + ".M1")
            os.remove(output_file_base + ".M1.tree")
            print(f"The smallest compressed file is: {output_file_base}.b ({size_b} bytes)")

    elif choice == '2':
        input_file = input("Enter the compressed file to decompress: ").strip()
        output_file = input("Enter the output file name: ").strip()

        # Decompress using the chosen method
        if input_file.endswith(".M1"):
            decompress_file_huffman(input_file, output_file)
        elif input_file.endswith(".b"):
            decompress_file_word(input_file, output_file, dictionary_file)
        else:
            print("Invalid compressed file format.")
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()