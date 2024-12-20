import heapq
import os
import struct
from collections import defaultdict
import paq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq):
    """Constructs the Huffman tree from the frequency dictionary."""
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
    """Builds the Huffman codes by traversing the Huffman tree."""
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def compress_method_2(input_file, output_file):
    """Compresses the input file using Huffman coding."""
    with open(input_file, 'rb') as f:
        content = f.read()

    # Step 1: Calculate frequency of each byte
    freq = defaultdict(int)
    for byte in content:
        freq[bytes([byte])] += 1

    # Step 2: Build Huffman tree
    huffman_tree = build_huffman_tree(freq)
    huffman_codes = build_huffman_codes(huffman_tree)

    # Step 3: Compress the data using the Huffman codes
    compressed_data = ''.join(huffman_codes[bytes([byte])] for byte in content)

    # Step 4: Write the compressed file in binary format
    with open(output_file, 'wb') as f:
        # First, write the header (the length of the codes)
        f.write(struct.pack('H', len(huffman_codes)))  # Number of codes
        for byte, code in huffman_codes.items():
            f.write(struct.pack('B', byte[0]))  # Byte value
            # Write the length of the code and then the code itself
            f.write(struct.pack('B', len(code)))
            f.write(int(code, 2).to_bytes((len(code) + 7) // 8, byteorder='big'))
        
        # Now, write the actual compressed data
        bit_stream = ''
        for byte in content:
            bit_stream += huffman_codes[bytes([byte])]
        
        # Convert bit stream to bytes and write
        padding = 8 - len(bit_stream) % 8
        bit_stream = '0' * padding + bit_stream  # Add padding
        byte_array = bytearray()
        for i in range(0, len(bit_stream), 8):
            byte_array.append(int(bit_stream[i:i+8], 2))

        f.write(bytearray(byte_array))

    print(f"File successfully compressed using Huffman coding to {output_file}")

def decompress_method_2(input_file, output_file):
    """Decompresses a file compressed with Huffman coding."""
    with open(input_file, 'rb') as f:
        # Step 1: Read the header (the length of the codes)
        num_codes = struct.unpack('H', f.read(2))[0]

        huffman_codes = {}
        reverse_codes = {}

        # Step 2: Read the codes
        for _ in range(num_codes):
            byte = struct.unpack('B', f.read(1))[0]
            code_length = struct.unpack('B', f.read(1))[0]
            code = bin(int.from_bytes(f.read((code_length + 7) // 8), byteorder='big'))[2:].zfill(code_length)
            huffman_codes[code] = bytes([byte])
            reverse_codes[bytes([byte])] = code

        # Step 3: Read the compressed data
        bit_stream = ''
        byte = f.read(1)
        while byte:
            bit_stream += bin(byte[0])[2:].zfill(8)
            byte = f.read(1)

        # Step 4: Remove padding
        padding = bit_stream[:8]
        bit_stream = bit_stream[8:]
        
        # Step 5: Decode the bit stream using the reverse codes
        current_code = ''
        result = []
        for bit in bit_stream:
            current_code += bit
            if current_code in reverse_codes:
                result.append(reverse_codes[current_code])
                current_code = ''

        # Step 6: Write the decompressed file
        with open(output_file, 'wb') as out_f:
            out_f.write(b''.join(result))

    print(f"File successfully decompressed to {output_file}")

# Method 1: Dictionary-based Compression with zlib for byte values (0-255)
def build_dictionary(file_path):
    """Builds a dictionary from the given file, assuming byte-level values (0-255)."""
    byte_count = defaultdict(int)
    
    with open(file_path, 'rb') as f:
        byte = f.read(1)
        while byte:
            byte_count[byte] += 1
            byte = f.read(1)
    
    # Sort bytes based on frequency (descending order)
    sorted_bytes = sorted(byte_count.items(), key=lambda x: x[1], reverse=True)
    
    # Assign an index to each byte value
    dictionary = {}
    for index, (byte, _) in enumerate(sorted_bytes):
        dictionary[byte] = index
    
    return dictionary

def compress_method_1(input_file, output_file):
    """Compresses the input file using dictionary-based compression and zlib for byte values (0-255)."""
    dictionary = build_dictionary(input_file)
    
    with open(input_file, 'rb') as f:
        content = f.read()

    compressed_data = []
    for byte in content:
        compressed_data.append(str(dictionary[bytes([byte])]))
    
    compressed_content = ' '.join(compressed_data)
    compressed_zlib = paq.compress(compressed_content.encode())
    
    with open(output_file, 'wb') as f:
        f.write(compressed_zlib)
    
    # Save the dictionary
    with open(output_file + ".dict", 'w') as dict_file:
        for byte, index in dictionary.items():
            dict_file.write(f"{byte[0]} {index}\n")

def decompress_method_1(input_file, output_file):
    """Decompresses a file using dictionary-based decompression and zlib for byte values (0-255)."""
    with open(input_file + ".dict", 'r') as dict_file:
        dictionary = {}
        for line in dict_file:
            byte, index = line.split()
            dictionary[int(index)] = bytes([int(byte)])
    
    reverse_dict = dictionary
    with open(input_file, 'rb') as f:
        compressed_data = f.read()

    decompressed_content = paq.decompress(compressed_data).decode()
    decompressed_data = [reverse_dict[int(code)] for code in decompressed_content.split()]
    
    with open(output_file, 'wb') as f:
        f.write(b''.join(decompressed_data))

# Main Menu
def main():
    print("Select an option:")
    print("1. Compress using Method 1 (words + zlib) and Method 2 (words + Huffman + zlib)")
    print("2. Decompress a file")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        input_file = input("Enter the input file: ")
        
        # Method 1 (Dictionary + zlib)
        output_file_1 = input_file + ".Method_1"
        compress_method_1(input_file, output_file_1)
        
        # Method 2 (Words + Huffman + zlib)
        output_file_2 = input_file + ".Method_2"
        compress_method_2(input_file, output_file_2)
        
        # Compare file sizes and delete the larger one
        size_1 = os.path.getsize(output_file_1)
        size_2 = os.path.getsize(output_file_2)
        
        if size_1 > size_2:
            os.remove(output_file_1)
            print(f"Deleted larger file: {output_file_1}")
            print(f"Smaller compressed file retained: {output_file_2}")
        else:
            os.remove(output_file_2)
            print(f"Deleted larger file: {output_file_2}")
            print(f"Smaller compressed file retained: {output_file_1}")
    
    elif choice == '2':
        compressed_file = input("Enter the compressed file: ")
        
        if compressed_file.endswith(".Method_1"):
            output_file = compressed_file.replace(".Method_1", "_decompressed.bin.txt")
            decompress_method_1(compressed_file, output_file)
            print(f"Decompressed file: {output_file}")
        
        elif compressed_file.endswith(".Method_2"):
            output_file = compressed_file.replace(".Method_2", "_decompressed.bin.txt")
            decompress_method_2(compressed_file, output_file)
            print(f"Decompressed file: {output_file}")
        
        else:
            print("Unknown compression method. Please provide a valid file.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()