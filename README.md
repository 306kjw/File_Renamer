# File Renamer

A simple GUI-based tool for batch renaming files in a folder.  
Written in Python using `tkinter`, this utility allows users to rename files with customizable naming rules such as file extension, digit count, starting number, prefix, and suffix. The tool automatically increments the number in the filename according to the specified starting number and digit format.

---

## Features

- Select target folder via GUI
- Specify:
  - File extension (e.g. png, jpg, mp4)
  - Number of digits in numbering (e.g. 1, 2, 3)
  - Starting number (e.g. 0, 1, 2)
  - Optional prefix and/or suffix to add before/after number

---

## How to Use

1. Run the script (Python) or executable (`.exe`)
2. Select a folder containing files to rename
3. Enter the desired:
   - Extension (`png`, `jpg`, etc.)
   - Number of digits (`3` → `001`)
   - Start number (`1`, `10`, etc.)
   - Optional prefix/suffix
4. Click 'Rename Files'

Example:
- Extension: `png`
- Digits: `3`
- Start: `1`
- Prefix: `img_`
- Suffix: `_v1`

Renamed files:  
`img_001_v1.png`, `img_002_v1.png`, ...

---

## Requirements

- Python 3.6+
- `tkinter` (comes pre-installed with standard Python on Windows/macOS)

If running from source:
```bash
python File_Renamer_1.0.0.py
