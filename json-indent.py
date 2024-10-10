import json
import os

# Subroutine to format and indent a .JSON file
def format_json():
    # Ask the user for the file path
    file_path = input("Please enter the path to your .JSON file: ").strip().strip('"').strip("'")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("ERROR: The specified path is not valid.")
        return
    
    # Check if the file is a .JSON file
    if not file_path.lower().endswith('.json'):
        print("ERROR: The specified file is not a .JSON file.")

    # Attempt to read and format the .JSON file
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Define the output path for the formatted file
        formatted_file_path = "FORMATTED_" + os.path.basename(file_path)

        # Apply the correct indentation
        with open(formatted_file_path, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"The formatted .JSON file has been saved to: {formatted_file_path}.")
    
    # Exception handling
    except json.JSONDecodeError:
        print("ERROR: The file is incorrectly formatted.")
    
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")

# Run the function
format_json()