import random
import paq
import os

print("Created by Jurijus Pacalovas.")

def generate_headings_and_chunks():
    """Generates data file with 17-bit headings and 256 positions (256 bits each) in a 256-byte chunk."""
    file_name = input("Enter the name of the file to save the output (e.g., table4.txt): ").strip()
    if os.path.exists(file_name):
        print(f"The file '{file_name}' already exists. Skipping generation.")
        return True  # Indicate success (file already exists)

    try:
        with open(file_name, "w") as file:
            max_headings = 2**17  # 17-bit headings (0 to 2^17-1)
            chunk_size = 256  # Number of positions in the chunk

            random.seed(42)  # for reproducibility

            for heading in range(max_headings):
                heading_bits = f"{heading:017b}"  # 17-bit heading

                # Create a chunk of 256 positions (each with 256 bits, which is 32 bytes)
                chunk = [bytes([random.randint(0, 255) for _ in range(32)]) for _ in range(chunk_size)]

                # Convert each position in the chunk to binary (256 bits per position)
                chunk_bits = ''.join(''.join(f"{byte:08b}" for byte in position) for position in chunk)

                # Write the heading and the corresponding 256 positions (256 bits each)
                file.write(f"{heading_bits} {chunk_bits}\n")

        print(f"Data generated and saved to '{file_name}'.")
        return True
    except Exception as e:
        print(f"An error occurred during data generation: {e}")
        return False


def compress_file(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as infile:
            data = infile.read()

        # Ask user if they want to use PAQ for compression
        use_paq = input("Do you want to use PAQ for compression? Enter 1 for YES or 0 for NO: ").strip()

        # Check if PAQ is to be used
        if use_paq == '1':
            compressed_data = paq.compress(data)
            print("Compression using PAQ successful.")
            compressed = 1  # Mark as PAQ compressed
        elif use_paq == '0':
            compressed_data = data  # No compression (just copy the data)
            print("No compression (PAQ not used), raw data copied.")
            compressed = 0  # No PAQ compression
        else:
            print("Invalid input. No compression applied.")
            return 0  # Invalid input, no compression

        # Write compressed data to output file
        with open(output_filename, 'wb') as outfile:
            outfile.write(compressed_data)

        print(f"Compression successful. Output saved to {output_filename}")
        return compressed
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return 0  # Indicate failure
    except Exception as e:
        print(f"An error occurred during compression: {e}")
        return 0  # Indicate failure


def decompress_and_save_raw_data(input_filename, output_filename):
    try:
        # Automatically decide to use PAQ for decompression if the file has a .paq extension
        if input_filename.endswith('.paq'):
            with open(input_filename, 'rb') as infile:
                compressed_data = infile.read()  # Read the entire compressed data

            # Decompress the data using PAQ
            decompressed_data = paq.decompress(compressed_data)
            print("Decompression using PAQ successful.")

            # Save the raw decompressed data to the output file
            with open(output_filename, 'wb') as outfile:
                outfile.write(decompressed_data)

            print(f"Decompression successful. Raw decompressed data saved to {output_filename}")
            return 1  # Indicate PAQ decompression was used
        else:
            print(f"Error: The file '{input_filename}' is not a PAQ-compressed file.")
            return 0  # Indicate failure
    except Exception as e:
        print(f"An error occurred during decompression: {e}")
        return 0  # Indicate failure


def main():
    while True:
        print("\nChoose an option:")
        print("1: Generate data file with 17-bit headings and 256 positions (256 bits each) in a 256-byte chunk")
        print("2: Compress the data file with or without PAQ")
        print("3: Decompress and save raw decompressed data")
        print("4: Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            if not generate_headings_and_chunks():
                print("Data generation failed.")

        elif choice == '2':
            input_file = input("Enter the name of the input file (e.g., table4.txt): ")
            output_file = input("Enter the name of the output file (e.g., table4.paq or table4_no_paq.txt): ")

            # Ask user to compress using PAQ or not
            compression_result = compress_file(input_file, output_file)
            if compression_result == 1:
                print("File was compressed using PAQ.")
            elif compression_result == 0:
                print("Compression failed or PAQ was not used.")

        elif choice == '3':
            input_file = input("Enter the name of the compressed file to decompress (e.g., table4.paq): ")
            output_file = input("Enter the name of the output file for decompression (e.g., table4_decompressed.bin): ")

            # Automatically use PAQ for decompression
            decompression_result = decompress_and_save_raw_data(input_file, output_file)
            if decompression_result == 1:
                print("File was decompressed using PAQ.")
            elif decompression_result == 0:
                print("Decompression failed or PAQ was not used.")

        elif choice == '4':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()