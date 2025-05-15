# FileOperator.py

**Author:** Maximus Barraza (Github: X86-Point5)
**Version:** 1.0.0
**Date:** 2025-05-14

## Description

`FileOperator.py` is a Python script that provides a collection of utility functions for performing various file and folder operations. This script is designed to simplify common tasks such as validating paths, sorting files, reading from and writing to files, and organizing files into categorized subdirectories.

## Features

This script offers the following functionalities:

* **Path Validation:**
    * Prompts the user to enter and validate directory paths.
    * Prompts the user to enter and validate file paths, ensuring they exist and are readable.
* **File and Folder Listing:**
    * Lists all items (files and folders) within a specified directory.
    * Lists items along with their type (File, Folder, Improper File) and extension.
* **File Organization:**
    * Groups items in a directory by their type or extension.
    * Outputs a list of items grouped by these categories.
    * Creates subfolders (bucket folders) based on item categories (e.g., "TXT", "PDF", "No Extension", "Improper File").
    * Moves files from a source folder into the appropriate categorized subfolders.
* **File Renaming:**
    * Renames files within a folder by removing leading/trailing whitespace and replacing spaces with underscores.
    * Handles potential naming conflicts by appending numerical suffixes if a file with the new name already exists.
* **File Content Handling:**
    * Validates if a file can be opened for reading with UTF-8 encoding.
    * Reads a file line by line, strips whitespace, and returns a list of non-empty lines.
    * Writes a list of strings to a file, with each string on a new line.
* **CSV File Operations:**
    * Reads a CSV file and returns its contents as a dictionary where keys are column headers and values are lists of column data.
    * Writes a dictionary of lists to a CSV file, allowing specification of headers.

## Requirements

* Python 3.x
* The following Python standard libraries are used:
    * `os`: For operating system interactions like path manipulation, listing directories, and folder manipulation.
    * `shutil`: For moving files and folders.
    * `csv`: For managing CSV files.

## How to Use

1.  **Ensure Python is Installed:** Make sure you have Python 3.x installed on your system.
2.  **Save the Script:** Save the `FileOperator.py` script to your desired location.
3.  **Import in Your Project:** You can import the `FileOperator` module into your own Python scripts to use its functions:

    ```python
    import FileOperator

    # Example: Get a valid folder path from the user
    folder = FileOperator.get_folder_path()
    if folder:
        print(f"Selected folder: {folder}")
        FileOperator.list_items(folder)

    # Example: Organize files in a folder
    # Make sure to handle potential errors or user cancellation
    target_folder = FileOperator.get_folder_path()
    if target_folder:
        FileOperator.assign_folders(target_folder)
        print(f"Files in {target_folder} have been organized.")
    ```
4.  **Run Functions Directly:** Some functions might be suitable to be called directly if the script is executed, though the current structure is primarily as a library of functions.

## Functions Overview

Here's a brief overview of the main functions available in `FileOperator.py`:

* `get_folder_path()`: Prompts the user for a valid directory path.
* `get_file(folder_path="")`: Prompts the user for a valid and readable file path.
* `list_items(folder_path)`: Lists items in a folder.
* `get_item_type(folder_path, item_name)`: Determines if an item is a file or folder and gets its extension.
* `list_items_by_type(folder_path)`: Lists items with their type and extension.
* `group_items(folder_path)`: Groups items in a folder by type/extension into a dictionary.
* `output_items_by_group(folder_path)`: Prints items grouped by type/extension.
* `create_bucket_folders(folder_path)`: Creates subfolders for different item categories.
* `assign_folders(folder_path)`: Moves files into their respective category subfolders.
* `rename_files(folder_path)`: Renames files by cleaning names and handling duplicates.
* `valid_read_file(file_name)`: Checks if a file can be read.
* `file_segement_lines(file_name)`: Reads non-empty lines from a file into a list.
* `string_list_to_file(string_list, file_name)`: Writes a list of strings to a file.
* `get_csv_dictionary(file_name)`: Reads a CSV file into a dictionary of lists.
* `dictionary_to_csv(data_dict, file_name, headers)`: Writes a dictionary of lists to a CSV file.

For detailed information on arguments, return values, and error handling for each function, please refer to the docstrings within the `FileOperator.py` script.

## Contributing

Currently, contributions are not actively sought, but suggestions or bug reports can be directed to the author.

## License

This software is dedicated to the public domain. You are free to use, modify, and distribute this code as you see fit, without any restrictions.
