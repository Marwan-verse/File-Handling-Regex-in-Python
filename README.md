# File-Handling-Regex-in-Python

Overview
This project demonstrates basic file handling operations and regular expressions in Python. It also includes examples of working with sets and a sample poem for file writing.

File Structure
fileHandle.py
Shows how to read, write, and append to text files in Python. It uses the with open() statement for safe file operations and demonstrates overwriting, appending, and reading file contents. It also writes a random poem to the file.

unique_search.py
Demonstrates how to use Python sets to find unique IP addresses from a list with duplicates. Shows the efficiency of sets for uniqueness and membership checks.

filename.txt
Contains the latest content written by fileHandle.py, which may be overwritten during script execution.

random_poem.txt
Stores a short, randomly generated poem.

regexBasics.py
Provides examples of Python regular expressions using the re module. Includes patterns for matching words, digits, IP addresses, and extracting usernames from log lines.

How to Run
To test file handling, run:
```bash
python3 _file_handling_folder/fileHandle.py
```
To see unique IP extraction, run:
```bash
python3 _file_handling_folder/unique_search.py
```
For regex examples, run:
```bash
python3 _Regex_Basics/regexBasics.py
```
