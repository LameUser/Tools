# Facebook Ads Library ID Screenshot and Data Extraction Script
==================================================================

This Python script uses Selenium and Edge WebDriver to:
- Extract unique "Library ID" values from a specified Facebook Ads library page.
- Capture screenshots of the ads associated with these Library IDs.
- Save the extracted data and screenshots to a specified folder.
- Generate a table containing the Library ID and the URL for each ID, and save it as an Excel file.

## Features:
---------
- Extracts unique "Library ID" values from a given Facebook Ads page.
- Captures screenshots of the corresponding ads.
- Generates a list of URLs for each Library ID.
- Saves the extracted data in an Excel file.
- Takes "human-like" random delays between actions to avoid bot detection.

## Requirements:
-------------
- Python 3.x
- Selenium (`pip install selenium`)
- pandas (`pip install pandas`)
- Microsoft Edge WebDriver (download from: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Setup:
------
1. **Download and Install Microsoft Edge WebDriver**:
   - Download Edge WebDriver from the official website based on your Edge version.
   - Set the path to `edgedriver.exe` in the script (the script currently uses `D:\\Tools\\edgedriver\\edgedriver.exe`).

2. **Modify Folder Path**:
   - Update the `folder_path` variable in the script to specify where you want to save the screenshots and Excel file.

3. **Install Required Python Libraries**:
   - Install the necessary libraries with the following commands:
     ```bash
     pip install selenium
     pip install pandas
     ```

4. **Run the Script**:
   - Run the script in your Python environment by executing the following command:
     ```bash
     python script_name.py
     ```

## Usage:
------
1. **Start the Script**:
   - The script will prompt you to enter the Facebook Ads link (the URL of the Ads library you want to scrape).
   - It will also ask for the folder path where you want to save the screenshots and Excel file.

2. **Web Scraping**:
   - The script will load the provided Facebook Ads link in a headless Edge browser.
   - It will extract the unique Library IDs associated with each ad and capture screenshots of the ads.
   
3. **Save Data**:
   - The script will save the Library ID, Library ID URL, and screenshot files in the specified folder.
   - It will also generate an Excel file containing the Library ID and URL for each ad in the Facebook Ads library.

4. **Results**:
   - You will find the screenshots saved in the specified folder.
   - The Excel file `facebook_ads_library_ids.xlsx` will be created in the specified folder, containing the following columns:
     - **S.No.**: Serial number of the Library ID.
     - **Library ID**: The unique Library ID for each ad.
     - **Library ID URL**: The URL for each Library ID.

## Example Input:
---------------
   - Enter the Facebook Ads link: https://www.facebook.com/ads/library/?id=12345678
   - Enter the folder path where you want to save the output: D:\AdsScreenshots

## Example Output:
----------------
   - Screenshots will be saved as `.png` files in the specified folder (e.g., `123456.png`).
   - An Excel file named `facebook_ads_library_ids.xlsx` will be saved in the specified folder with the following columns:


### Error Handling:
---------------
   - If there is an error (e.g., no elements found, failed to capture screenshot), an error message will be printed in the console.
   - If the specified folder path does not exist, the script will create it automatically.

### Customization:
--------------
   - Modify the `folder_path` and `facebook_ads_link` variables to match your requirements.
   - Update the path to `edgedriver.exe` based on where you have it installed.

### Note:
-----
   - The script runs in "headless" mode, meaning it does not display the browser window while scraping. This makes it faster and less likely to be detected by Facebook's anti-bot systems.
