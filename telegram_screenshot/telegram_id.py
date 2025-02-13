import re
import pandas as pd

def extract_telegram_ids():
    # Prompt user for file paths and column name
    input_file = input("Please enter the input Excel file path: ")
    output_file = input("Please enter the output Excel file path: ")
    feedback_column = input("What is the name of the column where telegram IDs are stored? ")

    try:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(input_file)
    except Exception as e:
        print(f"Error reading the input file: {e}")
        return

    if feedback_column not in df.columns:
        print(f"Column '{feedback_column}' not found in the Excel file.")
        return

    # Updated regex pattern to capture all variations of Telegram IDs
    pattern = r'(https?://t\.me/\S+|t\.me/\S+|@\w+)'

    # Extract matches and store them in a new column
    df['Telegram_IDs'] = df[feedback_column].apply(lambda x: 
        ", ".join(re.findall(pattern, str(x))) if pd.notnull(x) else '')

    # Save the extracted Telegram IDs to a new Excel file
    df_with_ids = df[df['Telegram_IDs'] != '']  # Filter rows with non-empty Telegram IDs

    try:
        df_with_ids.to_excel(output_file, index=False)
        print(f"Extracted Telegram IDs have been saved to {output_file}")
    except Exception as e:
        print(f"Error writing the output file: {e}")

# Run the function
extract_telegram_ids()