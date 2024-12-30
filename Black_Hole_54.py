import heapq
import struct
import paq


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
        frequency = {i: 0 for i in range(256)}
        for char in self.text:
            frequency[ord(char)] += 1
        return frequency

    def build_heap(self):
        heap = []
        for char, freq in self.frequency.items():
            if freq > 0:
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
            traverse_tree(node.left, current_code + "0")
            traverse_tree(node.right, current_code + "1")

        traverse_tree(self.huffman_tree, "")
        return codes

    def encode(self):
        return "".join(self.codes[ord(char)] for char in self.text)

    def decode(self, encoded_string):
        decoded_string = ""
        current_node = self.huffman_tree
        for bit in encoded_string:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.char is not None:
                decoded_string += chr(current_node.char)
                current_node = self.huffman_tree
        return decoded_string


def save_encoded_data_with_frequency(encoded_string, frequency, output_filename):
    # Compress the frequency data
    freq_data = bytearray()
    for byte in range(256):
        freq_data.extend(struct.pack('I', frequency[byte]))  # Save as 4-byte unsigned integers
    compressed_freq_data = paq.compress(bytes(freq_data))  # Convert to bytes before compression

    # Write the frequency size, frequency data, and encoded data to the file
    with open(output_filename, "wb") as file:
        # Save 4 bytes for the size of the compressed frequency data
        file.write(struct.pack('I', len(compressed_freq_data)))

        # Save the compressed frequency data
        file.write(compressed_freq_data)

        # Convert the encoded string into bytes and save it
        byte_array = bytearray(int(encoded_string[i:i+8], 2) for i in range(0, len(encoded_string), 8))
        file.write(byte_array)


def load_encoded_data_with_frequency(input_filename):
    with open(input_filename, "rb") as file:
        # Read the 4-byte frequency size
        freq_size = struct.unpack('I', file.read(4))[0]

        # Read the compressed frequency data
        compressed_freq_data = file.read(freq_size)
        freq_data = paq.decompress(compressed_freq_data)

        # Load the frequency table
        frequency = {}
        for byte in range(256):
            frequency[byte] = struct.unpack('I', freq_data[byte * 4:(byte + 1) * 4])[0]

        # Read the encoded data
        byte_array = file.read()
        encoded_string = ''.join(f"{byte:08b}" for byte in byte_array)

    return frequency, encoded_string


def main():
    print("Created by Jurijus Pacalovas.")
    print("Black_Hole_54")
    print("Select operation:")
    print("1. Compress file")
    print("2. Extract file")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        input_filename = input("Enter the input file name to compress: ")
        output_filename = input_filename+".b"

        try:
            # Read the input file
            with open(input_filename, "rb") as file:
                text = file.read().decode('latin-1')

            # Use Huffman coding to compress the text
            huffman_coder = HuffmanCoding(text)
            encoded_string = huffman_coder.encode()

            # Save the encoded data along with the frequency
            save_encoded_data_with_frequency(encoded_string, huffman_coder.frequency, output_filename)

            print(f"File compressed successfully and saved as {output_filename}")

        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == '2':
        input_filename = input("Enter the input file name to extract: ")
        output_filename = input_filename[:-2]

        try:
            # Load the frequency and encoded data from the file
            frequency, encoded_string = load_encoded_data_with_frequency(input_filename)

            # Decode the data using Huffman coding
            huffman_coder = HuffmanCoding(frequency=frequency)
            decompressed_text = huffman_coder.decode(encoded_string)

            # Write the decompressed text to the output file
            with open(output_filename, "wb") as file:
                file.write(decompressed_text.encode('latin-1'))

            print(f"File extracted successfully and saved as {output_filename}")

        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()