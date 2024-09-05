# file_handling_assignment.py

def create_and_write_file(filename):
    """Create a file and write initial lines of text to it."""
    try:
        with open(filename, 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here's a number: 42\n")
            file.write("Another line with text.\n")
        print("File created and initial content written.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating/writing to the file: {e}")
    finally:
        print("Attempt to create and write to file completed.")

def read_and_display_file(filename):
    """Read the content of the file and display it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nContent of the file:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure the file exists before reading.")
    except PermissionError:
        print("Permission denied. You don't have permission to read the file.")
    finally:
        print("Attempt to read the file completed.")

def append_to_file(filename):
    """Append additional lines of text to the existing content of the file."""
    try:
        with open(filename, 'a') as file:
            file.write("This is an appended line of text.\n")
            file.write("Another appended line with number: 99\n")
            file.write("One more appended line.\n")
        print("Additional content appended to the file.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("Attempt to append to file completed.")

if __name__ == "__main__":
    filename = "my_file.txt"
    
    create_and_write_file(filename)
    read_and_display_file(filename)
    append_to_file(filename)
    read_and_display_file(filename)
