import os
import sys

def compress_binary(input_filename, output_filename):
    """Compress repeated zero bytes from a binary file."""
    try:
        # Open the input file in binary mode
        with open(input_filename, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        sys.exit(1)

    compressed_data = bytearray()
    length = len(data)
    i = 0

    while i < length:
        count = 0

        # Count consecutive zero bytes
        while i < length and data[i] == 0 and count < 255:
            count += 1
            i += 1

        if count > 4:
            # Save the zero byte (0), the count, and the position (2 bytes)
            compressed_data.append(0)
            compressed_data.append(count)
            position = (i - count)
            compressed_data.extend(position.to_bytes(2, 'big'))
        else:
            # Write each byte directly if not more than 4 zeros
            if count > 0:
                compressed_data.extend([0] * count)
            else:
                compressed_data.append(data[i])
                i += 1

    # Write the compressed data to the output file
    with open(output_filename, 'wb') as f:
        f.write(compressed_data)

    print("Compression completed.")

def decompress_binary(input_filename, output_filename):
    """Decompress binary data and save it."""
    try:
        with open(input_filename, 'rb') as f:
            compressed_data = f.read()
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        sys.exit(1)

    decompressed_data = bytearray()
    i = 0

    while i < len(compressed_data):
        byte = compressed_data[i]

        if byte == 0 and i + 1 < len(compressed_data) and compressed_data[i + 1] > 4:
            count = compressed_data[i + 1]
            position = int.from_bytes(compressed_data[i + 2:i + 4], 'big')
            decompressed_data.extend([0] * count)
            i += 4  # Move to the next bytes
        else:
            decompressed_data.append(byte)
            i += 1

    # Save the decompressed binary data to the output file
    with open(output_filename, 'wb') as f:
        f.write(decompressed_data)

    print("Decompression completed.")

if __name__ == "__main__":
    print("Black_Hole_50.py Created by Jurijus Pacalovas")

    action = input("Choose action (1=Compress Binary, 2=Decompress Binary): ").strip()
    input_file = input("Enter input file name: ").strip()

    # Determine output file name based on input
    if action == "1":
        output_file = input_file + ".b"
    elif action == "2":
        output_file = os.path.splitext(input_file)[0] + ""
    else:
        print("Invalid option. Please select 1 or 2.")
        sys.exit()

    if action == "1":
        compress_binary(input_file, output_file)
    elif action == "2":
        decompress_binary(input_file, output_file)