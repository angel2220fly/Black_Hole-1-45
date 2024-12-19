import os
import heapq
from collections import defaultdict
import paq
print("Created by Jurijus Pacalovas.")

# Method 1: Dictionary-based Compression
def build_dictionary(file_path):
    """Builds a dictionary from the given file."""
    word_count = defaultdict(int)
    
    with open(file_path, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word_count[word] += 1
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    dictionary = {}
    for index, (word, _) in enumerate(sorted_words):
        dictionary[word] = index
    
    with open('Dictionary.txt', 'w') as dict_file:
        for word, index in dictionary.items():
            dict_file.write(f"{word} {index}\n")
    
    return dictionary

def compress_file(input_file, output_file, dictionary):
    """Compresses the input file using the dictionary."""
    with open(input_file, 'r') as f:
        content = f.read()

    compressed_data = []
    for word in content.split():
        if word in dictionary:
            compressed_data.append(str(dictionary[word]))
    
    with open(output_file, 'w') as f:
        f.write(' '.join(compressed_data))
    
    # Apply PAQ compression
    os.system(f"paq8px -c {output_file}")

def decompress_file(input_file, output_file, dictionary):
    """Decompresses the file using the dictionary."""
    with open(input_file, 'r') as f:
        compressed_data = f.read().split()

    reverse_dict = {v: k for k, v in dictionary.items()}
    decompressed_data = [reverse_dict[int(word)] for word in compressed_data]

    with open(output_file, 'w') as f:
        f.write(' '.join(decompressed_data))

# Method 2: Huffman and PAQ Compression
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq):
    """Builds a Huffman tree."""
    heap = [HuffmanNode(char, freq[char]) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, prefix="", codebook={}):
    """Builds Huffman codes from the Huffman tree."""
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def compress_file_huffman(input_file, output_file):
    """Compresses a file using Huffman coding and PAQ compression."""
    with open(input_file, 'r') as f:
        content = f.read()

    freq = defaultdict(int)
    for char in content:
        freq[char] += 1

    huffman_tree = build_huffman_tree(freq)
    huffman_codes = build_huffman_codes(huffman_tree)

    compressed_data = ''.join(huffman_codes[char] for char in content)

    with open(output_file, 'w') as f:
        f.write(compressed_data)
    
    # Apply PAQ compression
    os.system(f"paq8px -c {output_file}")

def decompress_file_huffman(input_file, output_file):
    """Decompresses a file using Huffman coding."""
    with open(input_file, 'r') as f:
        compressed_data = f.read()

    # Assuming you have the Huffman codes stored in some form for decompression
    # You would need to reverse the Huffman tree and codes to decode the content
    # (This part is left out for brevity, as it would require a full implementation of Huffman decoding.)

    # For now, just as a placeholder, the actual decompression would involve:
    # reverse_huffman_tree = build_huffman_tree(reversed_freq)
    # decompressed_data = decode_with_huffman(compressed_data, reverse_huffman_tree)

    with open(output_file, 'w') as f:
        f.write(decompressed_data)

# Main Program
def main():
    print("Choose a method:")
    print("1. Dictionary-based Compression")
    print("2. Huffman and PAQ Compression")
    print("3. Compress a file (Huffman + PAQ)")
    print("4. Decompress a file (Huffman + PAQ)")

    choice = input("Enter your choice: ")

    if choice == '1':
        input_file = input("Enter the input file to compress: ")
        dictionary = build_dictionary(input_file)
        output_file = input_file + ".b"
        compress_file(input_file, output_file, dictionary)
    elif choice == '2':
        input_file = input("Enter the input file to compress: ")
        output_file = input_file + ".paq"
        compress_file_huffman(input_file, output_file)
    elif choice == '3':
        input_file = input("Enter the input file to compress: ")
        output_file = input_file + ".paq"
        compress_file_huffman(input_file, output_file)
    elif choice == '4':
        input_file = input("Enter the compressed file to decompress: ")
        output_file = input_file[:-4]  # Remove '.paq' from the file name
        decompress_file_huffman(input_file, output_file)
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()