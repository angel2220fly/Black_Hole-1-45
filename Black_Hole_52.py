def compress(input_file, output_file):
    """
    Compress a UTF-8 text or binary file using Base-256 for repeated characters.
    """
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            i = 0

            while i < len(data):
                char = data[i:i+1]  # Read one byte
                count = 1

                # Count consecutive identical bytes
                while i + 1 < len(data) and data[i] == data[i + 1]:
                    count += 1
                    i += 1

                # Write the character
                outfile.write(char)

                # Write the count as 3 bytes (Base-256)
                outfile.write(count.to_bytes(3, byteorder='big'))

                i += 1

        print(f"Compression completed. Output saved to: {output_file}")
    except Exception as e:
        print(f"Error during compression: {e}")


def extract(input_file, output_file):
    """
    Decompress a file created by the compress function.
    """
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            i = 0

            while i < len(data):
                # Read the character (1 byte)
                char = data[i:i+1]
                i += 1

                # Read the count (3 bytes)
                count = int.from_bytes(data[i:i+3], byteorder='big')
                i += 3

                # Write the repeated characters to the output
                outfile.write(char * count)

        print(f"Decompression completed. Output saved to: {output_file}")
    except Exception as e:
        print(f"Error during extraction: {e}")


# User interaction
print("Binary UTF-8 Base-256 Compression/Extraction Tool")
choice = input("Enter 'compress' to compress or 'extract' to decompress: ").strip().lower()

if choice == 'compress':
    input_file = input("Enter the name of the input file (with extension): ")
    output_file = input("Enter the name of the compressed output file (with extension): ")
    compress(input_file, output_file)
elif choice == 'extract':
    input_file = input("Enter the name of the compressed file (with extension): ")
    output_file = input("Enter the name of the decompressed output file (with extension): ")
    extract(input_file, output_file)
else:
    print("Invalid option. Please choose 'compress' or 'extract'.")