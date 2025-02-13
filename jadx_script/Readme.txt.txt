# APK Decompilation and Keyword Search Script
===========================================

## This Python script automates the process of:
- **Decompiling an APK** file using JADX.
- **Searching for specific keywords and patterns** in decompiled Java/XML files.
- **Storing the search results in an Excel file** for easy analysis.

## Features:
---------
- **Decompiles APK files** into readable Java and XML files.
- **Searches for predefined keywords and regex patterns** in the decompiled source code.
- **Saves the extracted data** in an Excel file for easy review.
- **Automated process** requiring minimal user input.

## Requirements:
-------------
- **Python 3.x**
- **JADX (Java Decompiler)** – Download from: https://github.com/skylot/jadx/releases
- **Microsoft Excel (optional, for viewing the results)**
- **Python Packages:**
  Install required Python libraries using:
  ```bash
  pip install openpyxl
  ```

## Setup:
---------
1. Download and Install JADX:
- Download the latest release from the official JADX GitHub page.
- Extract the archive and locate jadx-gui.exe or jadx.exe.

2. Modify File Paths in the Script:
- Update the `jadx_path` variable with the correct path to your `j`adx-gui.exe`:
    ` jadx_path = r"D:\\Downloads\\jadx-gui-1.5.1-with-jre-win\\jadx-gui-1.5.1.exe" `
- Update the apk_path variable with the APK file path you want to analyze:
    ` apk_path = r"D:\\Desktop\\I4C\\hash_rename_APKs\\hash_rename\\sweet_money.apk" `
- Update the output_dir variable with the folder where decompiled files will be saved:
    ` output_dir = r"D:\\Desktop\\I4C\\hash_rename_APKs\\hash_rename\\decompiled" `
- Update the output_excel_path variable where the search results will be stored:
    ` output_excel_path = r"D:\\Desktop\\I4C\\hash_rename_APKs\\hash_rename\\jadx_search_results.xlsx" `

3. Install Required Python Packages:
- Run the following command in your terminal:
    ```bash
        pip install openpyxl```

4. Run the Script:
- Open a terminal or command prompt and execute:
    ```bash
    python script_name.py```

## Usage:

1. Start the Script:

- The script will decompile the specified APK using JADX.
- It will then scan the decompiled files for specific keywords and regex patterns.

2. Keyword and Regex Search:

- The script searches for the following keywords in Java/XML files:
    ```bash
        "package"
        "uses-permission"
        "http://"
        "wss://"
        "firebaseio.com"
    ```
3. The script also searches for the following regex pattern:
    `Indian phone numbers (+91-XXXXXXXXXX)`

4. Save and Review Results:

- The search results will be saved in an Excel file at the specified output path.
- The Excel file will contain:
- File Path: Location of the matched file.
- Line Content: The line where the keyword or pattern was found.