Telegram ID Extractor & Screenshot Tool
========================================

This tool consists of **two Python scripts** that work together to extract Telegram IDs from an Excel sheet and take screenshots. 

**Important:**  
Run the **Telegram ID Extractor script first**, then run the **Screenshot Taker script**.

----------------------------------------

Features:
---------
✔ Extracts Telegram IDs from an Excel file.  
✔ Saves extracted IDs in a structured format.  
✔ Uses the extracted IDs to take screenshots automatically.  
✔ Saves screenshots in a specified folder.  

----------------------------------------

Requirements:
-------------
- Python 3.x
- Required Python libraries:
 ` pip install pandas openpyxl selenium pillow `
- WebDriver (Chrome or Edge) for Selenium (Download from https://chromedriver.chromium.org/downloads)

----------------------------------------

How to Use:
-----------
### Step 1: **Extract Telegram IDs**
1. Place your input Excel file (e.g., `input.xlsx`) in the script directory.
2. Run the **Telegram ID Extractor** script:
 ` python tele_Screenshot.py `
3. The script extracts Telegram IDs and saves them in a new file (`telegram_ids.txt`).

### Step 2: **Take Screenshots**
1. Ensure `telegram_ids.txt` exists after running the first script.
2. Run the **Screenshot Taker** script:
 ` python telegram_ids.py `
3. The script will open Telegram profiles and take screenshots automatically.
4. Screenshots will be saved in the **"screenshots/"** directory.

----------------------------------------

File Structure:
---------------

📂 Tool Directory  ├── 📄 telegram_id_extractor.py (Extracts Telegram IDs) 
                    ├── 📄 screenshot_taker.py (Takes screenshots) 
                    ├── 📂 screenshots (Folder where screenshots are saved) 
                                            ├── 📄 telegram_ids.txt (Extracted IDs from the Excel sheet)
                                            ├── 📄 input.xlsx (Excel sheet with raw data) 
                                            ├── 📄 README.txt (This file)


----------------------------------------

Troubleshooting:
----------------
❌ **Issue:** No Telegram IDs found in `telegram_ids.txt`.  
✅ **Solution:** Ensure the input Excel file has a column with Telegram IDs.

❌ **Issue:** Screenshot script not working.  
✅ **Solution:** Check WebDriver compatibility with your Chrome/Edge version.

❌ **Issue:** Screenshots are not saving.  
✅ **Solution:** Ensure the **"screenshots"** folder exists, or create it manually.

----------------------------------------

Customization:
--------------
- Modify `telegram_id.py` if your Telegram IDs are in a different column.
- Adjust `tele_Screenshot.py` settings (e.g., delay time, output folder) as needed.

----------------------------------------

Credits:
--------
Developed using:
- `pandas` and `openpyxl` for Excel data processing.
- `selenium` for automated screenshot capturing.
- `pillow` for image processing.
