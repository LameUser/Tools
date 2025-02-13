def split_ids_and_save(input_file, output_file):
    try:
        # Open the input file with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        separated_lines = []
        for line in lines:
            # Split the line by comma and strip whitespace
            parts = [part.strip() for part in line.split(',')]
            separated_lines.extend(parts)

        # Write the separated lines into the output file with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as file:
            for item in separated_lines:
                if item:  # Ensure no empty lines are added
                    file.write(item + '\n')

        print(f"IDs and URLs have been separated and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "D:\\Desktop\\TelegramID\\Telegram_IDs.txt"  # Replace with the name of your input file
output_file = "D:\\Desktop\\TelegramID\\Tele_output.txt"  # Replace with the desired output file name
split_ids_and_save(input_file, output_file)
