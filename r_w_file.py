def read_and_modify_file(input_filename, output_filename):
    """Reads a file, modifies its content, and writes it to a new file."""
    try:
        # Open the input file to read
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: converting all text to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{input_filename}' has been read and modified successfully.")
        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "example_input.txt"  # Replace with your input file
    output_file = "modified_output.txt"  # Replace with your desired output file name

    read_and_modify_file(input_file, output_file)