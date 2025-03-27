def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")
        
        with open(filename, "r") as file:
            content = file.read()
        
        modified_content = content.upper()  # Example modification: Convert text to uppercase
        
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You may not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()
