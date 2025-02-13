PDF to Excel Converter LOCALLY
======================

This Python script extracts tables from a PDF file and saves them as an Excel file **LOCALLY**. It uses `Camelot` to read tables from PDFs and provides a user-friendly GUI using `Tkinter`.

Features:
---------
- Extracts tables from PDFs using `Camelot`
- Converts extracted tables into an Excel file (`.xlsx`)
- Auto-detects headers from tables
- User-friendly GUI for file selection and conversion
- Displays success and error messages

Requirements:
-------------
- Python 3.x
- Required Python libraries:
    ```
     pip install camelot-py[pdf] pandas openpyxl tkinter `

- `Ghostscript` must be installed for `Camelot` to work properly.
- Install on **Windows**: https://www.ghostscript.com/download/gsdnld.html
- Install on **Linux (Ubuntu/Debian)**:
  ```
  sudo apt install ghostscript
  ```

How to Use:
-----------
1. **Run the script**:
  ```
  python script.py
  ```
2. **Select a PDF file** containing tables.
3. **Choose an output location** for the Excel file.
4. Click **"Convert to Excel"** to extract tables and save them.

Example:
--------
- **Input PDF**: `data.pdf` (containing tables)
- **Output Excel**: `output.xlsx`
- The extracted tables will be saved in `output.xlsx` with auto-detected headers.

Troubleshooting:
----------------
- If **no tables are found**, ensure the PDF has structured tables and try using the `stream` method.
- If you get an error related to `ghostscript`, install it manually.
- If the extracted table structure is incorrect, verify the PDF format.

Customization:
--------------
- Change `flavor="stream"` to `flavor="lattice"` in `camelot.read_pdf()` for scanned PDFs with lines.
- Modify the `header` handling if tables don’t have proper headers.

Credits:
--------
Developed using:
- `Camelot` for PDF table extraction
- `Pandas` for data manipulation
- `Tkinter` for GUI interaction