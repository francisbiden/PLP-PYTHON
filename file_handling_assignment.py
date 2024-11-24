# File: file_handling_assignment.py

# Task 1: File Creation and Writing
try:
    with open("my_file.txt", "w") as file:
        # Writing three lines of text, including a mix of strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("This file contains both text and numbers: 12345.\n")
        file.write("Python is great for file handling!\n")
    print("File 'my_file.txt' has been created and written to successfully.")
except (PermissionError, FileNotFoundError) as e:
    print(f"Error writing to file: {e}")
finally:
    print("File creation task complete.")

# Task 2: Reading and Displaying File Content
try:
    with open("my_file.txt", "r") as file:
        # Reading and displaying the content of the file
        content = file.read()
        print("\nContent of 'my_file.txt':")
        print(content)
except FileNotFoundError as e:
    print(f"Error reading the file: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
finally:
    print("File reading task complete.")

# Task 3: Appending Additional Content
try:
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text
        file.write("Appending this line to the file.\n")
        file.write("Here's another line with numbers: 67890.\n")
        file.write("File handling in Python is easy and efficient!\n")
    print("\nNew content has been appended to 'my_file.txt'.")
except (PermissionError, FileNotFoundError) as e:
    print(f"Error appending to the file: {e}")
finally:
    print("File appending task complete.")
