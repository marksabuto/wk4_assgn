with open('input.txt', 'w') as f:
    lines = [
        'Line 1: Hello Mars!\n',
        'Line 2: We come in peace.\n',
        'Line 3: Preparing rover...\n',
        'Line 4: Sampling soil...\n',
        'Line 5: Mission success!\n'
    ]
    f.writelines(lines)

def file_processor():
    """Read a file, modify its content, and write to a new file with error handling."""
    
    # Get input filename from user with error handling
    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            # Try to open the file for reading
            with open(input_filename, 'r') as input_file:
                content = input_file.read()
            break  # Exit loop if file was successfully read
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{input_filename}'. Please try another file.")
        except IsADirectoryError:
            print(f"Error: '{input_filename}' is a directory, not a file. Please enter a valid filename.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Get output filename from user with validation
    while True:
        output_filename = input("Enter the name of the output file: ")
        if output_filename.strip() == "":
            print("Output filename cannot be empty. Please try again.")
            continue
        
        try:
            # Try to open the file for writing to check permissions
            with open(output_filename, 'w') as test_file:
                break
        except PermissionError:
            print(f"Error: You don't have permission to write to '{output_filename}'. Please try another filename.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    # Write the modified content to the new file
    try:
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"Success! Modified content has been written to '{output_filename}'.")
    except Exception as e:
        print(f"Failed to write to output file: {e}")

if __name__ == "__main__":
    file_processor()