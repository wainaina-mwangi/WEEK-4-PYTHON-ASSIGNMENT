# Read content from the original file
with open('original_file.txt', 'r') as infile:
    content = infile.read()

# Modify the content (example: convert all text to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open('modified_file.txt', 'w') as outfile:
    outfile.write(modified_content)

print("File has been modified and saved as 'modified_file.txt'")



#   question 2
# Function to read the content of a file with error handling
def read_file():
    # Ask the user for the filename
    filename = input("Please enter the filename: ")

    try:
        # Try to open the file in read mode
        file = open(filename, 'r')
        content = file.read()
        print("File content successfully read!")
        print(content)  # Print the content of the file
        file.close()  # Close the file after reading
    except FileNotFoundError:
        # Error if the file doesn't exist
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        # Error if the file can't be read due to permission issues
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        # Catch any other unforeseen errors
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file()


