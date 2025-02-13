# Split IDs and Save Script
==========================

This Python script is designed to read an input file containing comma-separated IDs and URLs, split them into individual components, and save the separated values into an output file. It ensures that each ID or URL is written on a new line in the output file.

## Features:
---------
- Reads an input file with UTF-8 encoding.
- Splits comma-separated values from each line.
- Removes extra whitespace around each ID/URL.
- Writes each separated ID/URL into the output file, ensuring no empty lines are added.
- Handles errors gracefully and prints any encountered issues.

## Requirements:
-------------
- Python 3.x
- UTF-8 encoded text files for both input and output

## Script Overview:
----------------
The `split_ids_and_save` function performs the following tasks:
1. **Input File**: Reads the content of the input file.
2. **Splitting**: Splits each line into parts by commas, strips any unnecessary whitespace, and collects them.
3. **Output File**: Writes each split item (ID or URL) into a new line in the output file.
4. **Error Handling**: Prints any error messages if an exception occurs.

## Usage:
------
1. **Download and Prepare Files**:
   - Ensure you have a text file (`input_file`) with comma-separated IDs and URLs.
   - Create an empty output file (`output_file`) where the script will save the separated values.

2. **Modify File Paths**:
   - Update the `input_file` and `output_file` paths in the script to point to the correct files on your system.

   Example:
   ```python
   input_file = "D:\\Desktop\\TelegramID\\Telegram_IDs.txt"
   output_file = "D:\\Desktop\\TelegramID\\Tele_output.txt"
   ```
## Run the Script:
--------------
Use this command to run the script
` python break_id `
