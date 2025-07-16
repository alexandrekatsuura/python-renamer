import os
from renamer import Renamer

class Main:
    def __init__(self):
        """
        Initializes the class settings
        _renamer (Renamer): class responsible for renaming files
        """
        self._renamer = Renamer()

    def run(self, pattern: str, replacement: str):
        """
        Executes the expected behavior during initial execution
        """
        print(f"\nRenaming '{pattern}' to '{replacement}'")
        self._renamer.rename_files(pattern, replacement)


if __name__ == "__main__":
    main = Main()
    # This block is executed only when the script is run directly
    print("\n--- Example Usage of the File Renamer ---")
    
    # Test 1: Rename 'picture' to 'image'
    main.run(r"picture", "image")

    # Test 2: Rename 'video' to 'clip' (Real Execution)
    main.run(r"video", "clip")

    # Test 3: Add prefix 'new_' to all files (Dry Run)
    main.run(r"^(.*)$", r"new_\1")

    # Test 4: Remove numbers from the end of .jpg files (Real Execution)
    main.run(r"_\d+\.jpg$", ".jpg")
