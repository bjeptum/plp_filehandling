# This script reads a file, modifies its content, and writes it to a new file.
# It demonstrates basic file handling in Python, including error handling.

def handle_file_errors():
    """Prompts the user for a filename and handles errors if it doesn't exist or can't be read."""
    filename = input("Please enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File '{filename}' was read successfully!")
        print(f"Content of the file:\n{content}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error: Could not read the file '{filename}'. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    handle_file_errors()
