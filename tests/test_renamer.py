import os
import pytest
from src.renamer import Renamer

INPUT_DIR = 'files_input'
OUTPUT_DIR = 'files_output'

@pytest.fixture(autouse=True)
def setup_and_cleanup():
    # Ensure both input and output directories exist
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clean directories before and after each test
    yield
    for folder in [OUTPUT_DIR]:
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))


def test_clear_output_directory():
    # Create a dummy file in the output directory
    dummy_file = os.path.join(OUTPUT_DIR, "temp.txt")
    with open(dummy_file, "w") as f:
        f.write("dummy content")

    assert os.path.exists(dummy_file)

    # Initialize Renamer, which clears the output folder
    renamer = Renamer()
    assert not os.listdir(OUTPUT_DIR)  # Output folder should be empty


def test_rename_files_with_match():
    # Create files in the input directory
    filenames = ["photo_001.jpg", "photo_002.jpg", "image.jpg"]
    for name in filenames:
        with open(os.path.join(INPUT_DIR, name), "w") as f:
            f.write("dummy content")

    renamer = Renamer()
    renamed = renamer.rename_files(r"photo", "img")

    # Check renamed output
    expected = [("photo_001.jpg", "img_001.jpg"), ("photo_002.jpg", "img_002.jpg")]
    assert sorted(renamed) == sorted(expected)

    # Verify renamed files exist in the output directory
    output_files = os.listdir(OUTPUT_DIR)
    assert "img_001.jpg" in output_files
    assert "img_002.jpg" in output_files
    assert "image.jpg" not in output_files


def test_rename_files_with_no_match():
    # Create a file that should not be renamed
    filename = "document.txt"
    with open(os.path.join(INPUT_DIR, filename), "w") as f:
        f.write("no match here")

    renamer = Renamer()
    renamed = renamer.rename_files(r"none_file", "img")

    # No files should be renamed
    assert renamed == []
    assert not os.listdir(OUTPUT_DIR)


def test_rename_files_with_regex_groups():
    # Create a file to test regex capture group renaming
    filename = "img123.png"
    with open(os.path.join(INPUT_DIR, filename), "w") as f:
        f.write("test content")

    renamer = Renamer()
    renamed = renamer.rename_files(r"img(\d+)", r"image_\1")

    assert renamed == [("img123.png", "image_123.png")]
    assert os.path.exists(os.path.join(OUTPUT_DIR, "image_123.png"))
