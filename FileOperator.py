#FileOperator.py
"""
File Operations Handler (FileOperator.py)

Provides a range of functions meant for dealing with files

Features:
-Validates File and Folder Path
-Sorts Files by Type
-Reads and Writes Data to Files
-Outputs Data From Files
"""

__author__ = "Maximus Barraza (Github: X86-Point5)"
__version__ = "1.0.0"
__date__ = "2025-05-14"

#used for operating system interactions such as path manipulation, listing
#directories and folder manipulation
import os

#used for moving files and folders in hard memory
import shutil

#used for managing csv files
import csv



def get_folder_path():
    """Prompts the user until a valid directory path is entered.

    Args:
        None

    Returns:
        str or None: The validated, full path to an existing directory,
                     or None if the user enters an empty string to exit.
    Raises:
        None: Handles invalid path errors internally by re-prompting.
              (External interrupts like KeyboardInterrupt can still occur).
    """

    #Loop continuously, prompting the user for a folder path.
    #The loop exits ONLY when a valid, existing directory path is entered
    #and returned by the function, OR if the user enters nothing.
    while True:

        #retrieves the name of a folder path from the user removing trailing
        #whitespace and surrounding quotes
        folder_path = input("\n\tEnter the path for the folder or nothing to exit: ").strip().strip('"')

        #in the case the user entered nothing
        if not folder_path:
            return None

        #checks if the name entered is a folder path
        valid_path = os.path.isdir(folder_path)

        if not valid_path:
            #informs the user of the error in finding the folder path
            print(f"\n\tERROR: \"{folder_path}\" is not valid or existing path.")

        else:
            #exits the loop by returning the string name of the folder path
            return folder_path
   



def get_file(folder_path = ""):    
    """Prompts the user to enter a filename and validates if it exists
    and is readable. The filename can be relative to an optional base folder.

    The function will continuously prompt the user until a valid, readable
    file path is entered.

    Args:
        folder_path (str, optional): The base directory path to prepend to the
            user-entered filename. Defaults to "" (meaning the filename
            will be relative to the current working directory or an
            absolute path if the user enters one).

    Returns:
        str or None: The full, validated path to an existing and readable file,
            or None if the user enters an empty string to quit.
    Raises:
        None: Handles file access errors (FileNotFoundError, PermissionError,
              IsADirectoryError, OSError, general Exception) internally by
              printing an error message and re-prompting the user.
              (External interrupts like KeyboardInterrupt can still occur
              during the input() call).
    """

    #Loops continuously prompting user for a file.
    #The loop exits only when a valid file name is entered
    #and returned, OR if the user enters nothing.
    while True:

        #retrieves the file name from the user and deletes surrounding quotes
        #and white space.
        file_name = input("\n\tEnter the name of the file or nothing to exit: ").strip().strip('"')

        #incase the user just presses enter
        if not file_name:
            return None

        #connects the file to folder_path
        file_name = os.path.join(folder_path, file_name)

        #Attempts to validate the file by checking the typical file prone
        #errors that might occur for file operations.
        try:

            #The two errors to occurs in this operation are that the file does
            #not exist or that file can not be read. However other errors can
            #occur when attempting to open a file.
            with open(file_name, "r", encoding="utf-8") as f:

                #returns the file_name if no errors were generated
                return file_name

        except FileNotFoundError:

            #occurs if the name of the file does not exist
            print(f"\tERROR - File could not be found")
        except PermissionError:

            #occurs if the file is not allowed to be read
            print(f"\tERROR - File could not be accessed")
        except Exception as e:

            #other errors that might occur when opening a file
            print(f"\tERROR - File could not be handled")




def list_items(folder_path):
    """Lists out all the items with in a folder path to the console or prints
    that operation could not be done due to a problem with processing

    Args:
        folder_path(str): An exisiting folder path

    Returns:
        None: Prints out the items with in the folder path to the console

    Raises:
        None

    """

    #Attempts to validate the folder by checking if a list of files can be
    #generated from the name of the path 
    try:
        
        #Generates a list of items and can raise an error if the folder does
        #not exist, or an ambiguous error
        items = os.listdir(folder_path)

        
        if not items:

            #incase the folder is empty
            print(f"\n\t{folder_path} is empty")
        else:
            
            #starting header for the items in the folder 
            print(f"\n\t----- Contents of {folder_path} -----")

            #prints out the name of each item in the folder
            for item_name in items:
                print(f"\t{item_name}")

            #ending header for the items in the folder
            print(f"\n\t-----    End of {folder_path}   -----")

    except FileNotFoundError:

        #If the folder could not be found
        print(f"\n\tFolder {folder_path} not found")
    except Exception as e:

        #If any other errors occured when opening the folder path
        print(f"\n\tAn error {e} occurred")




def get_item_type(folder_path, item_name):
    """Determines the type of the item given based on its name and the path
    to the folder that was given

    Args:
        folder_path(str): The path for the folder item_name resides in
        item_name(str): The name of the item
    Returns:
        tuple[str, str | None]: A tuple where the first element is the item type
            ('File', 'Folder', or 'Improper File') and the second element
            is the lowercase file extension (e.g., '.txt') if it's a file
            with an extension, otherwise None.
    Raises:
        None
    """
    
    #Attempts to join, validate, and extract the extension from a item. If any
    #errors are generated then the item gets labled as improper.
    try:

        #connects the name of item to the path of the folder
        item_path = os.path.join(folder_path, item_name)

        if os.path.isfile(item_path):

            #if the item is a file
            extension = os.path.splitext(item_path)

            #returns the type as a file and the lowercased extension
            return ("File", extension[1].lower())

        elif os.path.isdir(item_path):
            #if the item is a folder returns the type as a folder with
            #no extension
            return ("Folder", None)

    except Exception as e:
        #if the item is problematic returns the type as improper file with
        #no extension
        return ("Improper File", None)




def list_items_by_type(folder_path):
    """Lists all of the items from a folder to the console and outputs their
    extension and type. If any errors occur during processing they are printed
    to the console. 

    Args:
        folder_path(str): The full path of the folder

    Returns:
        None: Prints to the console

    Raises: 
        None: Handles all errors internally
    """

    
    #Attempts to list out all of the items in a folder along with their type
    #and given extension. Generating a list of items from an ambiguous
    #directory can cause multiple errors which are handled in the try-block
    try:

        #Attempts to get all of the items from the folder path as a list
        #and can generate exceptions such as "FileNotFoundError" and
        #"PermissionError" when trying to access
        items = os.listdir(folder_path)

        if not items:
            #incase the folder is empty
            print(f"\n\t{folder_path} is empty")

        else:

            #outputs the starting header for the contents
            print(f"\n\t----- Contents of {folder_path} With Type ------")

            #iterates over all of the items in the folder
            for item_name in items:

                #prints the item name
                print(f"\t{item_name}")

                #gets a tuple that contains the type and extension of the item
                item_type = get_item_type(folder_path, item_name)

                #outputs the type
                print(f"\tType: {item_type[0]}")

                #outputs the extension
                print(f"\tExtension: {item_type[1]}")

                #intermediate line
                print()
            
            #ending header for the folder contents
            print(f"\n\t-----         End of {folder_path}        ------")
            
    except FileNotFoundError:

        #incase the file could not be found
        print(f"\n\tFolder {folder_path} not found")

    except PermissionError:

        #incase the file could not be accessed
        print(f"\n\tFolder {folder_path} could not be accessed")

    except Exception as e:

        #incase any ambiguous errors occur
        print(f"\n\tAn error {e} occurred")

        


def group_items(folder_path):
    """Constructs a dictionary from a folder path where each category is an 
    item type and returns None if the folder could not be operated on

    Args:
        folder_path(str): The path of the folder 

    Returns:
        dict[str, list[str]] or None: A dictionary where keys are category names
            (e.g., 'Folder', '.txt', 'No Extension', 'Improper File') and
            values are lists of item names (str) belonging to that category.
            Returns None if an error occurs (e.g., folder not found,
            permission issues).

    Raises:
        None: All errors handled internally
    """

    #dictionary for holding the string names of items in a folder and storing
    #them by type
    sorted_types = {}

    #Attempts to create a list of items from an ambiguous folder path. If the
    #folder can not be accessed in any way then nothing can be sorted therefore,
    #None is returned.
    try:

        #Tries to store the names of all of the items in the folder to a list
        #and can generate errors from doing so
        items = os.listdir(folder_path)

        #Loops through each and every item in the list
        for item_name in items:

            #gets the item and extension of the item in the folder
            item_type, extension = get_item_type(folder_path, item_name)

            #initializes the category to None, for an unknown value
            category = None


            if not item_type == "File":
                #incase the item type is not a file sets the category to that
                #item's type
                category = item_type

            else:
                #if the item is a file
                if extension:
                    #sets the category to the item's extension if it has one
                    category = extension
                else:
                    #sets the category to "No Extension" if the item does not
                    #have an extension
                    category = "No Extension"

            if category not in sorted_types:
                #if the item belongs in a new category
                sorted_types[category] = [item_name]
            else:
                #if the item belongs in an existing category
                sorted_types[category].append(item_name)
        return sorted_types

    except Exception as e:
        #if any problems occured then nothing should be returned
        return None





def output_items_by_group(folder_path):
    """Outputs each possible group for all of the items in a folder based on
    the item type of each item in the folder. If any errors occur when 
    processing the folder then it is printed to the console.

        Args:
            folder_path(str): The path to the folder containing the groupable
            items

        Returns: 
            None: Only prints to the console
    
        Raises:
            None: No operations generate errors
    """

    #dictionary to store the items by type
    grouped_items = group_items(folder_path)

    #incase the dictionary could not be generated
    if not grouped_items:
        #outputs the problem and ends the function
        print(f"\n\tThe items in {folder_path} could not be grouped")
        return

    #prints the header for the item groups in the folder
    print(f"\n\t----- Items in {folder_path} by Group\n")
    
    #goes through all categories in the dictionary
    for category in grouped_items:

        #outputs the category name
        print(f"\n\t{category}:")

        #goes through all items in the category
        for item in grouped_items[category]:

            #outputs the file names
            print(f"\t\t{item}")


def create_bucket_folders(folder_path):
    """
    Creates subfolders within the specified folder_path based on item categories
    derived from `group_items`. It then returns a dictionary mapping the
    names of these created/ensured subfolders to the lists of items
    belonging to those original categories.

    The function first groups items using `group_items`. For each category
    that is not 'Folder', it determines a target subfolder name (e.g.,
    uppercasing file extensions, using "DOT_" prefix for single-character
    extensions, or using names like "No Extension" directly). It then ensures
    these subfolders exist using `os.makedirs(exist_ok=True)`.

    Args:
        folder_path (str): The full path to the main folder where subfolders
                           will be created.

    Returns:
        dict[str, list[str]] or None:
            On success, a dictionary where keys are the names of the
            created/ensured subfolders (e.g., 'TXT', 'DOT_C', 'No Extension')
            and values are the lists of item names (str) that belong to the
            original category corresponding to that subfolder.
            Returns None if `group_items` fails, if no groups are found,
            or if a critical error occurs during folder creation.

    Raises:
        None: Handles errors from `group_items` or `os.makedirs`
              internally by printing an error message and returning None.
              (External interrupts like KeyboardInterrupt can still occur).
    """

    #gets a dictionary of all of the items sorted by type
    grouped_items = group_items(folder_path)

    #incase getting a dictionary failed no folder dictionary should be
    #generated since no folders will be created
    if not grouped_items:
        return None

    #initializes the dictionary containing the folder names with the files that
    #should be in them
    return_dictionary = {}

    #The most likely error to occur here is a permission error when creating
    #directories with in a folder however other erros could occur
    try:

        #loops for every category in the dictionary of items sorted by type
        for category in grouped_items:

            if category == "Improper File":
                #if there are improper files a folder for them is made
                os.makedirs(os.path.join(folder_path, category), exist_ok = True)

                #puts all of the file names that would belong in "Improper File"
                #folder in said category
                return_dictionary[category] = grouped_items[category]

            elif category == "No Extension":
                #if there are files with no extension then a folder for them is made
                os.makedirs(os.path.join(folder_path, category), exist_ok = True)
                
                #puts all of the files in a dictionary for files with no extension
                return_dictionary[category] = grouped_items[category]

            elif not category == "Folder":
                #if the file is not one of the outsider cases

                #the name of the folder is the extension with out the "."
                folder_name = category[1:].upper()

                #incase the extension is single like a ".h" then the folder
                #is named "DOT_H"
                if len(folder_name) == 1:
                    folder_name = "DOT_" + folder_name

                #creates a directory for all of the files with the extension
                os.makedirs(os.path.join(folder_path, folder_name), exist_ok = True)

                #puts all of the file names in a dictionary for files with the
                #given extension
                return_dictionary[folder_name] = grouped_items[category]

        #returns the complete dictionary of the files and the folders they
        #belong in
        return return_dictionary

    #Incase creating a folder generated an error then the error is printed
    except Exception as e:
        print("\n\tERROR - Creating folders could not be done")
        print(f"\n\tERROR - {e}")

        #None is returned to signal operation failure
        return None


def assign_folders(folder_path):
    """Moves files from a specified base folder into categorized subfolders.

    This function first calls `create_bucket_folders` to determine the
    destination subfolder for each file (based on its type/extension) and
    to ensure these subfolders exist. It then iterates through the map
    returned by `create_bucket_folders` (which maps destination subfolder
    names to lists of original filenames) and moves each original file
    from the `folder_path` into its corresponding created subfolder.

    Errors during individual file moves (e.g., permission issues, file
    not found at the time of move) are caught, printed to the console,
    and the function attempts to continue with other files.

    Args:
        folder_path (str): The full path to the main folder containing the
                           source files that need to be moved and where the
                           destination subfolders (buckets) have been or will
                           be created.

    Returns:
        None: This function performs file system operations and prints status
              or error messages directly to the console.

    Raises:
        None: Handles errors from `create_bucket_folders` (by returning early
              if it fails) and individual file move operations internally by
              printing messages. (External interrupts like KeyboardInterrupt
              can still occur).
    """

    #retreives the files to move from the create_bucket_folders function
    #as a dictionary
    files_to_move = create_bucket_folders(folder_path)

    #if there are no files to move then the function stops executing
    if not files_to_move:
        print("\n\tERROR - No files to move")
        return

    #loops through each category with in the dictionary
    for category in files_to_move:

        #loops through each file in the category
        for file in files_to_move[category]:

            #generates the file path for the new location of the file
            new_file_path = os.path.join(folder_path, category, file)

            #generates the file path for the current location of the file
            old_file_path = os.path.join(folder_path, file)

            #attempts to move the file from its old location to its new location
            try:
                #can generate a permission error
                shutil.move(old_file_path, new_file_path)

            except Exception as e:
                #incase the specific file could not be moved
                print(f"\n\tERROR: Could not move {file} due to {e}")




def rename_files(folder_path):
    """
    Renames files within a specified folder by removing leading/trailing whitespace
    and replacing spaces with underscores. If a file with the new name already
    exists, it appends a numerical suffix (e.g., "_2", "_3") to ensure uniqueness.

    Args:
        folder_path (str): The absolute or relative path to the folder
                           containing the files to be renamed.

    Returns:
        bool: True if the operation completes (or attempts to complete) for all
              files, False if the initial listing of files in the folder_path
              fails (e.g., path does not exist or is not a directory).
              Note: Individual file renaming errors within the loop are caught
              and allow the function to continue with other files, but the
              function will still return True in such cases.

    Raises:
        None: All errors handled internally
    """

    #initializes the list of files
    files = []

    #Attempts to get the list of files from the folder path. If a list of files
    #throws an error then the function returns false to signal failure
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        return False

    #loops through the entire list of files
    for file in files:

        #generates the current path of the item in files
        old_path = os.path.join(folder_path, file)

        #checks if the item is a file
        if os.path.isfile(old_path):

            #takes out any blank spaces on the ends of the file name
            new_name = file.strip()

            #replaces all of the blankspaces to underscores
            if ' ' in new_name:
                new_name = new_name.replace(' ', '_')

            #checks if the new name is seperate from the old name
            if new_name != file:

                #generates a new path for file
                new_path = os.path.join(folder_path, new_name)

                #counts the amount of attempts to generate a new file
                attempt = 1

                #runs until a non-existent name is generated
                while True:

                    #saves the name of the extension
                    ext = os.path.splitext(new_path)[1]

                    if attempt < 2:

                        #if it is the first attempt renaming a file
                        try:
                            #attempts to rename the file
                            os.rename(old_path, new_path)
                            break

                        except FileExistsError:
                            #if the file name already exists increases the
                            #amount of attempts
                            attempt += 1

                            #splices the path of the attempted name
                            new_path = os.path.splitext(new_path)[0]

                            #inserts the "_2" tag at the end of the file
                            new_path += "_2"

                            #appends the extension bag to the file name
                            new_path += ext

                        except Exception as e:
                            #does not attempt to try any more operations
                            #on the file if the name of the file can not 
                            #be changed
                            break
                    else:
                        #on repeat attempts of renaming 
                        try:
                            os.rename(old_path, new_path)
                            #if file renaming succeeds
                            break
                        except FileExistsError:
                            #if name on the file still does not work

                            #splices the extension from the new file path
                            new_path = os.path.splitext(new_path)[0]

                            #generates the old addon for the file path
                            old_addon = f"_{attempt}"

                            #takes the old addon off of the spliced file path
                            new_path = new_path[:(len(new_path)-len(old_addon))]

                            #increments the total amount of attempts
                            attempt += 1

                            #appends the addon to path of the file
                            new_path += f"_{attempt}"

                            #adds the extension back to the file
                            new_path += ext

    #returns true to signal operation success
    return True




def valid_read_file(file_name):
    """
    Validates if a file can be opened for reading with UTF-8 encoding.

    This function attempts to open the specified file in read-only mode ('r')
    using 'utf-8' encoding. It does not read the file's content but checks
    for its existence, readability, and that it can be initiated for reading
    with UTF-8 encoding. All potential exceptions during this process are
    handled internally, and the function will return False in such cases.

    Args:
        file_name (str): The path to the file to be validated.

    Returns:
        bool: True if the file can be successfully opened for reading.
              False if any error occurs during the attempt to open the file.

    Raises:
        None: This function handles all exceptions internally and does not
              raise any exceptions to the caller.
    """

    #Attempts to open the file for reading
    try:
        #Only tries to open the file
        with open(file_name, "r", encoding="utf-8") as f:
            pass
        #Returns true if the file be read
        return True
    except Exception as e:
        #Returns false if any errors on the file can be read
        return False



def file_segement_lines(file_name):
    """
    Reads a file line by line, strips leading/trailing whitespace from each line,
    and returns a list containing only non-empty lines.

    The function attempts to open and read the specified file using UTF-8 encoding.
    If any error occurs during file opening or reading (e.g., file not found,
    permission issues, encoding errors), the function will handle the error
    internally and return the list of lines collected up to the point of the
    error, or an empty list if the error occurred before any lines were read.

    Args:
        file_name (str): The path to the file to be read.

    Returns:
        list[str]: A list of strings, where each string is a non-empty line
                   from the file with leading/trailing whitespace removed.
                   If an error occurs, this list may be empty or partially
                   populated with lines read before the error.

    Raises:
        None: This function handles all exceptions internally and does not
              raise any exceptions to the caller.
    """

    #initializes the list for each string
    segmented_lines = []

    #Attempts to open the file and read line by line
    try:
        #If any errors are generated then the empty list is returned
        with open(file_name, "r", encoding="utf-8") as f:

            #Iterates through all lines in the file
            for line in f:
                
                #removes the empty space off the ends of a line
                new_string = line.strip()

                #ensures that only strings with actual information are added
                if len(new_string) > 0:
                    segmented_lines.append(new_string)

    except Exception as e:
        #If any errors in file processing occured the string list will return
        #as it was before any errors occured
        pass

    #returns the list of all of the lines in the file
    return segmented_lines




def string_list_to_file(string_list, file_name):
    """
    Writes a list of strings to a file, with each string on a new line.

    This function attempts to open the specified file in write mode ('w') with
    UTF-8 encoding. If the file already exists, its contents will be overwritten.
    Each string from the input list is written to the file, followed by a
    newline character.

    Args:
        string_list (list[str]): A list of strings to be written to the file.
        file_name (str): The path to the file where the strings will be written.
                         If the file does not exist, it will be created.
                         If it exists, it will be overwritten.

    Returns:
        bool: True if all strings are successfully written to the file.
              False if any error occurs during the file opening or writing process.

    Raises:
        None: This function handles all exceptions internally (e.g., IOError,
              PermissionError) and does not raise any exceptions to the caller.
              It returns False upon encountering an error.
    """

    #Attempts to open the file for writing and clearing all of its contents
    try:
        with open(file_name, "w", encoding="utf-8") as f:

            #Adds each line from the string list to the file
            for line in string_list:
                f.write(line + "\n")

    except Exception as e:
        #returns false for operation failure
        return False

    #returns true for operation success
    return True




def get_csv_dictionary(file_name):
    """
    Reads a CSV file and returns its contents as a dictionary of lists,
    where keys are column headers and values are lists of column data.

    This function attempts to open and read the specified CSV file using
    UTF-8 encoding. It uses `csv.DictReader` to process the CSV data.
    If the CSV file is empty or headers cannot be determined, an empty
    dictionary might be returned. If a row is missing a value for a
    particular header, an empty string "" is used as a placeholder.

    Args:
        file_name (str): The path to the CSV file to be read.

    Returns:
        dict[str, list[str]]: A dictionary where each key is a column header
                              (str) from the CSV file, and its corresponding
                              value is a list of strings representing the data
                              in that column. If an error occurs during file
                              processing (e.g., file not found, permission
                              denied, malformed CSV), an empty dictionary or a
                              partially populated dictionary (if the error
                              occurs mid-processing) might be returned.

    Raises:
        None: This function handles all exceptions internally (e.g.,
              FileNotFoundError, PermissionError, csv.Error, general Exception)
              and does not raise any exceptions to the caller. It returns the
              `columns` dictionary in its current state upon encountering an error.
    """

    #initializes the list of columns from the csv file
    columns = {}

    #attempts to open the csv file for reading
    try:
        #sets the encoding for the file
        with open(file_name, "r", encoding="utf-8") as f:

            #sets a reader for the csv file
            reader = csv.DictReader(f)

            #gets the headers from the csv file
            headers = reader.fieldnames

            #sets each categories in columns dictionary to empty lists
            for header in headers:
                columns[header] = []

            #iterates over each row from the reader
            for row in reader:

                #iterates over each header from the headers list
                for header in headers:

                    #adds each string from the location (header, row#) in the csv
                    columns[header].append(row.get(header, ""))

    except Exception as e:
        #passes over if any errors occur in file handling
        pass

    #returns the full dictionary of all of the columns
    return columns




def dictionary_to_csv(data_dict, file_name, headers):
    """Writes a dictionary of lists to a CSV file.

    Overwrites `file_name` if it exists. Uses `headers[0]` from `data_dict`
    to determine row count. Only columns in `headers` are written.

    Args:
        data_dict (dict[str, list]): Dictionary with column names as keys
                                     and lists of column data as values.
        file_name (str): Path to the output CSV file.
        headers (list[str]): Ordered list of column headers for the CSV.

    Returns:
        bool: True on success, False if any error occurs.

    Raises:
        None: Handles all exceptions internally.
    """
    #Attempts to open a file for complete overwriting via a dictionary
    #If this can not be done then false is returned for operation failure.
    try:
        #opens the file with the name of file_name for a complete overwrite
        with open(file_name, "w", encoding="utf-8", newline = '') as f:

            #sets the file writer to have the headers of the dictionary data_dict
            file_writer = csv.DictWriter(f, fieldnames = headers)

            #writes the headers to the csv
            file_writer.writeheader()

            #iterates over reach row in the dictionary
            for index in range(len(data_dict[headers[0]])):

                #creates a dictionary for each grid space in the row
                row_dict = {}

                #loops over each grid space in the row
                for column in data_dict:

                    #fills in every grid space in the row assinging each space
                    #to its proper column
                    row_dict[column] = data_dict[column][index]

                #writes each row to the csv
                file_writer.writerow(row_dict)

        #returns true to signal operation success
        return True

    except Exception as e:

        #if complete file overwriting failes then false is returned to signal
        #operation failure
        return False


