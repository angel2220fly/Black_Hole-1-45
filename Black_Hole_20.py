import os
import paq

# Constants for the algorithm
MAX_VALUE = 255  # 8-bit max value (adjusted for byte-level handling)
REPLACEMENT_VALUE = 254  # Replacement for MAX_VALUE

def method_1_compress(input_file, output_file):
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

            outfile.write(compressed_data)
            return len(compressed_data)

    except Exception as e:
        print(f"Error during Method_1 compression: {e}")
        return float('inf')

def method_2_compress(input_file, output_file):
    """
    Compress a binary file by replacing MAX_VALUE with REPLACEMENT_VALUE (same as Method_1).
    """
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            compressed_data = bytearray()

            # Compression logic: replacing MAX_VALUE with REPLACEMENT_VALUE
            for byte in data:
                if byte == MAX_VALUE:
                    compressed_data.append(REPLACEMENT_VALUE)
                else:
                    compressed_data.append(byte)

            outfile.write(compressed_data)
            return len(compressed_data)

    except Exception as e:
        print(f"Error during Method_2 compression: {e}")
        return float('inf')

def method_3_compress(input_file, output_file):
    """
    Compress a binary file using zlib compression.
    """
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            compressed_data = zlib.compress(data)

            # Write compressed data to the output file
            outfile.write(compressed_data)
            return len(compressed_data)

    except Exception as e:
        print(f"Error during Method_3 compression (zlib): {e}")
        return float('inf')

def method_4_compress(input_file, output_file):
    """
    Compress a binary file using zlib compression (instead of gzip).
    """
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            compressed_data = paq.compress(data)

            # Write compressed data to the output file
            outfile.write(compressed_data)
            return len(compressed_data)

    except Exception as e:
        print(f"Error during Method_4 compression (zlib): {e}")
        return float('inf')

def extract(input_file, output_file):
    """
    Extract a binary file by reversing the compression process depending on the file name.
    """
    try:
        # Determine method based on the input file name
        if '_method1' in input_file:
            method = "Method_1"
        elif '_method2' in input_file:
            method = "Method_2"
        elif '_method3' in input_file:
            method = "Method_3"
        elif '_method4' in input_file:
            method = "Method_4"
        else:
            print("Unknown compression method in the file name.")
            return

        # Open the compressed file
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            extracted_data = bytearray()

            if method == "Method_1" or method == "Method_2":
                # Replacing REPLACEMENT_VALUE with MAX_VALUE for Methods 1 & 2
                for byte in data:
                    if byte == REPLACEMENT_VALUE:
                        extracted_data.append(MAX_VALUE)
                    else:
                        extracted_data.append(byte)
                # Add back the removed byte to restore original size
                extracted_data.append(MAX_VALUE)
            elif method == "Method_3" or method == "Method_4":
                # Decompress using zlib for Methods 3 & 4
                extracted_data = paq.decompress(data)

            # Write extracted data
            outfile.write(extracted_data)
            print(f"Extracted file size: {len(extracted_data)} bytes")

    except Exception as e:
        print(f"Error during extraction: {e}")

def main():
    """
    Main function to handle user input for compression or extraction.
    """
    try:
        print("Choose an option:")
        print("1. Compress a file")
        print("2. Extract a file")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            print("Enter the input file name for compression:")
            input_file = input().strip()
            
            # Get the output file name for compressed file
            output_file = input("Enter the output file name for the compressed file: ").strip()
            
            # Compress with all four methods and store the sizes
            sizes = {}
            
            # Method_1
            method_1_output = output_file + "_method1"
            sizes['Method_1'] = method_1_compress(input_file, method_1_output)
            
            # Method_2
            method_2_output = output_file + "_method2"
            sizes['Method_2'] = method_2_compress(input_file, method_2_output)
            
            # Method_3
            method_3_output = output_file + "_method3"
            sizes['Method_3'] = method_3_compress(input_file, method_3_output)
            
            # Method_4
            method_4_output = output_file + "_method4"
            sizes['Method_4'] = method_4_compress(input_file, method_4_output)

            # Choose the best compression method (smallest file size)
            best_method = min(sizes, key=sizes.get)
            best_output = output_file + f"_{best_method.lower()}"
            print(f"The best method is {best_method} with compressed size: {sizes[best_method]} bytes.")
            
            # Copy the best method's output file as the final compressed file
            os.rename(globals()[f"{best_method.lower()}_output"], best_output)
            print(f"Final compressed file: {best_output}")

        elif choice == '2':
            input_file = input("Enter the compressed file name for extraction: ").strip()
            output_file = input("Enter the output file name for the extracted file: ").strip()
            
            # Extract the file based on method used in the file name
            extract(input_file, output_file)

        else:
            print("Invalid choice. Please choose 1 or 2.")

    except Exception as e:
        print(f"Error during main execution: {e}")

if __name__ == "__main__":
    main()