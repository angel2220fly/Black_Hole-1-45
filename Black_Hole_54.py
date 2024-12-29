import heapq
import struct
import paq
import os
print("Created by Jurijus Pacalovas.")
print("Black_Hole_54")

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self, text=None, frequency=None):
        self.text = text
        self.frequency = frequency if frequency else self.calculate_frequency()
        self.heap = self.build_heap()
        self.huffman_tree = self.build_huffman_tree()
        self.codes = self.generate_codes()

    def calculate_frequency(self):
        frequency = {}
        for i in range(256):
            frequency[i] = 0
        for char in self.text:
            frequency[ord(char)] += 1
        return frequency

    def build_heap(self):
        heap = []
        for char, freq in self.frequency.items():
            if freq > 0:  # Only include characters that appear in the text
                node = Node(char, freq)
                heapq.heappush(heap, node)
        return heap

    def build_huffman_tree(self):
        while len(self.heap) > 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)
            combined_freq = left.freq + right.freq
            new_node = Node(None, combined_freq)
            new_node.left = left
            new_node.right = right
            heapq.heappush(self.heap, new_node)
        return self.heap[0]

    def generate_codes(self):
        codes = {}
        def traverse_tree(node, current_code):
            if node is None:
                return
            if node.char is not None:
                codes[node.char] = current_code
                return
            if node.left:
                traverse_tree(node.left, current_code + "0")
            if node.right:
                traverse_tree(node.right, current_code + "1")
        traverse_tree(self.huffman_tree, "")
        return codes

    def encode(self):
        encoded_string = "".join(self.codes[ord(char)] for char in self.text)
        return encoded_string

    def decode(self, encoded_string):
        decoded_string = ""
        current_code = ""
        current_node = self.huffman_tree
        for bit in encoded_string:
            current_code += bit
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node is not None and current_node.char is not None:
                decoded_string += chr(current_node.char)
                current_node = self.huffman_tree
        return decoded_string

    def generate_ternary_codes(self):
        codes = {}
        def traverse_tree(node, current_code):
            if node is None:
                return
            if node.char is not None:
                codes[node.char] = self.decimal_to_ternary(int(current_code, 2))
                return
            if node.left:
                traverse_tree(node.left, current_code + "0")
            if node.right:
                traverse_tree(node.right, current_code + "1")
        traverse_tree(self.huffman_tree, "")
        return codes

    def decimal_to_ternary(self, n):
        if n == 0:
            return "0"
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return "".join(reversed(nums))

    def encode_ternary(self):
        self.codes = self.generate_ternary_codes()
        encoded_string = "".join(self.codes[ord(char)] for char in self.text)
        return encoded_string

def save_frequency(frequency, frequency_filename):
    with open(frequency_filename, "wb") as freq_file:
        for byte in range(256):
            freq_file.write(struct.pack('B', frequency[byte]))

def load_frequency(frequency_filename):
    frequency = {}
    with open(frequency_filename, "rb") as freq_file:
        for byte in range(256):
            frequency[byte] = struct.unpack('B', freq_file.read(1))[0]
    return frequency

def compress_with_zlib(data):
    return paq.compress(data)

def decompress_with_zlib(compressed_data):
    return paq.decompress(compressed_data)

def main():
    print("Select operation:")
    print("1. Compress file")
    print("2. Extract file")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        input_filename = input("Enter the input file name to compress: ")
        output_filename = input_filename+".b"
        frequency_filename = "frequency.bin"

        try:
            # Read the input file
            with open(input_filename, "r", encoding="latin-1") as file:
                text = file.read()

            # Use Huffman coding to compress the text
            huffman_coder = HuffmanCoding(text)
            encoded_string = huffman_coder.encode()

            # Convert the encoded string to base 256 representation
            encoded_bytes = [int(encoded_string[i:i+8], 2) for i in range(0, len(encoded_string), 8)]
            encoded_data = bytes(encoded_bytes)

            # Save the frequency data to a separate file for decompression
            save_frequency(huffman_coder.frequency, frequency_filename)

            # Compress the encoded data and frequency file using zlib
            compressed_data = compress_with_zlib(encoded_data)
            with open(output_filename, "wb") as file:
                file.write(compressed_data)

            # Compress the frequency data
            with open(frequency_filename, "rb") as file:
                frequency_data = file.read()
            compressed_frequency = compress_with_zlib(frequency_data)

            # Save the compressed frequency data
            with open(frequency_filename, "wb") as file:
                file.write(compressed_frequency)

            print(f"File compressed successfully and saved as {output_filename}")
            print(f"Frequency data compressed and saved to {frequency_filename}")

        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == '2':
        input_filename = input("Enter the input file name to extract: ")
        output_filename = input_filename[:-2]
        frequency_filename = "frequency.bin"

        try:
            # Read the compressed file and the frequency file
            with open(input_filename, "rb") as file:
                compressed_data = file.read()

            # Decompress the data using zlib
            decompressed_data = decompress_with_zlib(compressed_data)

            # Load the compressed frequency data and decompress it
            with open(frequency_filename, "rb") as file:
                compressed_frequency = file.read()
            decompressed_frequency = decompress_with_zlib(compressed_frequency)

            # Save the decompressed frequency data to a file
            with open(frequency_filename, "wb") as file:
                file.write(decompressed_frequency)

            # Load the frequency data from the decompressed file
            frequency_data = load_frequency(frequency_filename)

            # Decode the decompressed binary data
            compressed_binary = ''.join(f"{byte:08b}" for byte in decompressed_data)

            # Rebuild the Huffman coding tree using the frequency data
            huffman_coder = HuffmanCoding(frequency=frequency_data)
            decompressed_text = huffman_coder.decode(compressed_binary)

            # Write the decompressed text to the output file
            with open(output_filename, "w", encoding="latin-1") as file:
                file.write(decompressed_text)

            print(f"File extracted successfully and saved as {output_filename}")

        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid choice! Please choose 1 or 2.")

if __name__ == "__main__":
    main()