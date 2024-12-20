import os
import heapq
from collections import Counter
import pickle
import struct
import paq

print("Created by Jurijus Pacalovas.")
print("This software supports multiple compression methods, including Huffman coding with PAQ, replacement-based compression, and word-based compression.")

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

# Word-based Compression Functions
def load_dictionary(dictionary_file, encoding="utf-8"):
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
                        encoded_data.append(0x00)
                        index = word_to_index[word]
                        encoded_data.extend(struct.pack(">I", index))
                    else:
                        encoded_data.append(0x01)
                        try:
                            encoded_data.extend(word.encode('utf-8'))
                        except UnicodeEncodeError as e:
                            print(f"Error encoding word '{word}': {e}")
                            continue
                        encoded_data.append(0x00)
                    if idx < len(words) - 1:
                        encoded_data.append(0x03)
                
                encoded_data.append(0x02)
            
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
                if flag == 0x00:
                    index = struct.unpack(">I", decompressed_data[i:i+4])[0]
                    decoded_text += index_to_word.get(index, "<unknown>")
                    i += 4
                elif flag == 0x01:
                    word = ""
                    while i < len(decompressed_data) and decompressed_data[i] != 0x00:
                        word += chr(decompressed_data[i])
                        i += 1
                    decoded_text += word
                    i += 1
                elif flag == 0x02:
                    decoded_text += "\n"
                elif flag == 0x03:
                    decoded_text += " "

            outfile.write(decoded_text)
            print(f"File decompressed and saved as '{output_file}'")
    except (FileNotFoundError, IOError) as e:
        print(f"Error decompressing file: {e}")

# Compression Methods
def compress_file_huffman(input_file, output_file, method="huffman"):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = infile.read()

        if method == "huffman":
            word_frequencies = Counter(data.split())
            tree = build_huffman_tree(word_frequencies)
            codes = generate_huffman_codes(tree)
            encoded_data = huffman_encode(data, codes)

            compressed_data = paq.compress(encoded_data.encode('utf-8'))

            with open(output_file, 'wb') as outfile:
                outfile.write(compressed_data)

            with open(output_file + ".tree", 'wb') as tree_file:
                pickle.dump(tree, tree_file)

            print(f"File compressed using Huffman coding and saved as '{output_file}'")
        else:
            print("Invalid compression method.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error during compression: {e}")

def decompress_file_huffman(input_file, output_file, method="huffman"):
    try:
        if method == "huffman":
            with open(input_file + ".tree", 'rb') as tree_file:
                tree = pickle.load(tree_file)

            with open(input_file, 'rb') as infile:
                compressed_data = infile.read()

            encoded_data = paq.decompress(compressed_data).decode('utf-8')

            decoded_data = huffman_decode(encoded_data, tree)

            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write(decoded_data)

            print(f"File decompressed using Huffman coding and saved as '{output_file}'")

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
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        input_file = input("Enter the input file to compress: ").strip()
        output_file_base = input("Enter the base name for the output file: ").strip()
        dictionary_file = "Dictionary.txt"

        # Perform compression using Huffman and replacement methods
        compress_file_huffman(input_file, output_file_base + ".M1", method="huffman")
        compress_file(dictionary_file, input_file, output_file_base + ".b", encoding="utf-8")
    elif choice == '2':
        input_file = input("Enter the compressed file to decompress: ").strip()
        output_file = input("Enter the output file name: ").strip()
        dictionary_file = "Dictionary.txt"

        # Decompress using the chosen method
        if input_file.endswith(".M1"):
            decompress_file_huffman(input_file, output_file, method="huffman")
        elif input_file.endswith(".b"):
            decompress_file(dictionary_file, input_file, output_file, encoding="utf-8")
        else:
            print("Invalid compressed file format.")
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()