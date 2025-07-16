import os
import re
import shutil

class Renamer:
    def __init__(self):
        """
        Initializes class settings
        """
        self._clear_files_output()

    def _clear_files_output(self, folder_path = 'files_output'):
        """
        Deletes all files and subdirectories inside a specified folder.

        Parameters:
        - folder_path (str): Absolute or relative path to the folder to be cleaned.

        This function removes all files and directories (recursively) inside the given folder.
        The folder itself is not deleted—only its contents are removed.

        ⚠️ Warning: This operation is destructive and irreversible. Use with caution!
        """
        for file in os.listdir(folder_path):
            path_file = os.path.join(folder_path, file)
            if os.path.isfile(path_file):
                os.remove(path_file)

    def rename_files(self, pattern, replacement) -> list:
        """
        Renames files in bulk within a directory based on a pattern.

        This function iterates through all files in the 'files_input' folder and renames those
        whose names match a regular expression pattern, exporting them to the 'files_output' folder.

        Args:
            pattern (str): The regex pattern to search for in the filenames.
                           Example: r"photo" to find 'photo', r"^(.*)" to capture the entire name.
            replacement (str): The replacement string for the matched pattern.
                               May include regex capture groups (e.g., r"new_\1").

        Returns:
            list: A list of tuples (old_name, new_name) of the files that were renamed.
        """
        path_input = 'files_input'
        path_output = 'files_output'
        renamed_files = []
        try:
            # List all files and directories in the given path
            for filename in os.listdir(path_input):
                old_path = os.path.join(path_input, filename)
                
                # Check if the current item is a file (not a subdirectory)
                if os.path.isfile(old_path):
                    # Apply the regex to find and replace the pattern in the filename
                    new_filename = re.sub(pattern, replacement, filename)
                    
                    # If the new name is different from the original, proceed with renaming (or simulation)
                    if new_filename != filename:
                        new_path = os.path.join(path_output, new_filename)
                        shutil.copy(old_path, new_path)
                        print(f"Renamed: '{filename}' to '{new_filename}'")
                        renamed_files.append((filename, new_filename))
        
        except FileNotFoundError:
            # Catch error if the specified directory does not exist
            print(f"Error: The directory '{path_input}' was not found.")
        except Exception as e:
            # Catch any other unexpected error during the process
            print(f"An unexpected error occurred: {e}")
        
        return renamed_files
