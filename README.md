# ✏️ Python Renamer

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-renamer?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-renamer?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-renamer?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-renamer?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-renamer?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created solely for educational purposes.
> It is not intended for production use or handling sensitive files.


## ℹ️ About

**Python Renamer** is a simple yet efficient tool for batch renaming files using regular expressions. It scans the `files_input` folder, applies renaming rules, and outputs the renamed files into `files_output`.

This project is designed to demonstrate concepts like file manipulation, regex processing, automation, and unit testing in Python.


## 🚀 Features

* 🔁 **Batch Renaming**: Rename multiple files based on regex patterns.
* 🧪 **Unit Testing with Pytest**: Ensures correctness of logic and operations.
* 📁 **Input/Output Separation**: Keeps original files untouched by writing results to a separate folder.
* ✨ **Regex Support**: Flexible renaming using Python’s `re` module.
* 🧼 **Clean Output**: Automatically clears output folder before each run.


## 🛠️ Technologies Used

* **Python 3.x**
* **`re` (regex)**: For pattern matching and renaming logic.
* **`shutil` / `os`**: For file and folder handling.
* **`pytest`**: For unit testing.


## ⚙️ How to Run the Project

### Prerequisites

Make sure you have **Python 3.x** installed.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/alexandrekatsuura/python-renamer
cd python-renamer
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate    # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```


## ▶️ Usage

1. Place the files you want to rename into the `files_input/` folder.

2. Edit the renaming logic or run it with a regex pattern and replacement. For example:

```bash
python src/main.py
```

3. Renamed files will be saved to the `files_output/` folder.


## ✅ Running the Tests

To run all unit tests using `pytest`, make sure you are in the root directory:

```bash
pytest -v
```

This will execute all test cases defined in the `tests/` directory.


## 📁 Project Structure

```bash
python-renamer/
├── src/
│   ├── main.py             # Main execution logic
│   └── renamer.py          # Core logic for file renaming
├── tests/
│   └── test_renamer.py     # Unit tests for the renamer
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```


## 📄 License

This project is licensed under the [MIT License](LICENSE).
