# Constants for the algorithm
MAX_VALUE = 255  # 8-bit max value (adjusted for byte-level handling)
REPLACEMENT_VALUE = 254  # Replacement for MAX_VALUE

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

def extract(input_file, output_file):
    """
    Extract a binary file by reversing the compression process.
    """
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            extracted_data = bytearray()

            # Extraction logic: replacing REPLACEMENT_VALUE with MAX_VALUE
            for byte in data:
                if byte == REPLACEMENT_VALUE:
                    extracted_data.append(MAX_VALUE)
                else:
                    extracted_data.append(byte)

            # Add back the removed byte to restore original size
            extracted_data.append(MAX_VALUE)

            # Write extracted data
            outfile.write(extracted_data)
            print(f"Compressed file size: {len(data)} bytes")
            print(f"Extracted file size: {len(extracted_data)} bytes")
            print("Extraction successful!")

    except Exception as e:
        print(f"Error during extraction: {e}")

def main():
    """
    Main function to handle user input for compression or extraction, with repeat functionality.
    """
    try:
        print("Choose an option:")
        print("1. Compress a file")
        print("2. Extract a file")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice in ['1', '2']:
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()
            times = int(input("How many times do you want to repeat the operation? ").strip())

            if times <= 0:
                print("The number of times must be greater than zero.")
                return

            for i in range(times):
                print(f"\nOperation {i + 1} of {times}:")
                if choice == '1':
                    compress(input_file, output_file)
                elif choice == '2':
                    extract(input_file, output_file)

        else:
            print("Invalid choice. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the repetitions.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()