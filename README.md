# json-indent

A python script that reads a '.json' file, formats it with proper indentation, and saves the formatted version to a new file.

# Prerequisites

- Python 3.x

# Features

- Prompts the user to input the path to their .JSON file.
- Validates the provided file path and ensures it points to a .JSON file.
- Reads the .JSON file content, correctly indents it, and saves this formatted copy of the file.
- Includes error handling with useful error messages (e.g., if an invalid file path or file is specified).

## Error handling

The script handles the following errors:

- **Invalid file path:** If the specified file path doesn't point to an existing file.
- **Non-.JSON file:** If the provided file is not a .JSON file.
- **.JSON formatting errors:** If the file content contains corrupted or otherwise invalid .JSON.
- **Other errors:** If unexpected errors occur, the error dialog will display further information about the issue.

# Usage

Clone or download the script, open your terminal, and run the script using Python.

```bash
python format_json.py
```

When prompted, enter the path to your .JSON file.

```bash
Please enter the path to your .JSON file:
```

The path can include quotes or spaces - the script is designed to handle these. It's important to make sure that the file path points to an existing .JSON file.

The script will then create a new .JSON file with proper indentation. It will be named `FORMATTED_[originalFileName].json` and will be located in the same directory as the original file.

# Licence

This project is licenced under the MIT Lincence.