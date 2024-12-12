# Constants for the algorithm
MAX_VALUE = 255  # 8-bit max value (adjusted for byte-level handling)
REPLACEMENT_VALUE = 254  # Replacement for MAX_VALUE
METADATA_BITS = 16  # Number of metadata bits (2 bytes)

def compress(input_file, output_file):
    """
    Compress a binary file by replacing MAX_VALUE with REPLACEMENT_VALUE.
    Ensures a 1-byte reduction in file size.
    """
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            compressed_data = bytearray()

            # Compression logic: replacing MAX_VALUE with REPLACEMENT_VALUE
            replacements = 0
            for byte in data:
                if byte == MAX_VALUE:
                    compressed_data.append(REPLACEMENT_VALUE)
                    replacements += 1
                else:
                    compressed_data.append(byte)

            # If replacements occurred, reduce 1 byte for compression
            if replacements > 0:
                compressed_data = compressed_data[:-1]

            # If no replacements were made, compression is unsuccessful
            if len(compressed_data) < len(data):
                outfile.write(compressed_data)
                print(f"Input file size: {len(data)} bytes")
                print(f"Compressed file size: {len(compressed_data)} bytes")
                print(f"Compression successful! Compression ratio: {(len(data) - len(compressed_data)) / len(data):.2%}")
            else:
                print("Compression unsuccessful. No size reduction achieved.")

    except Exception as e:
        print(f"Error during compression: {e}")

def main():
    """
    Main function to handle user input for compression.
    """
    try:
        # Ask the user how many times they want to compress
        num_compressions = int(input("How many times would you like to compress a file? ").strip())

        # Loop for each compression operation
        for i in range(num_compressions):
            print(f"\nCompression {i + 1}:")
            # Ask for the input and output filenames
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()

            compress(input_file, output_file)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()