import time
import random
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service  # Use Edge Service
from selenium.webdriver.edge.options import Options  # Use Edge Options

# Function to extract unique library IDs
def extract_library_ids(driver):
    library_data = []
    elements = driver.find_elements(By.XPATH, "//span[contains(text(),'Library ID')]")
    for element in elements:
        text = element.text
        if text.startswith("Library ID:"):
            library_id = text.split(":")[1].strip()
            parent_div = element.find_element(By.XPATH, "ancestor::div[contains(@class, '_7jvw x2izyaf x1hq5gj4 x1d52u69')]")
            library_data.append((library_id, parent_div))
    return library_data

# Function to generate library ID URLs
def generate_library_urls(library_ids):
    return [f"https://www.facebook.com/ads/library/?id={library_id}" for library_id in library_ids]

# Function to capture ad screenshots
def capture_ad_screenshots(library_data, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Take the first two screenshots and delete them
    for i, (lib_id, ad_element) in enumerate(library_data):
        try:
            screenshot_path = os.path.join(folder_path, f"{lib_id}.png")
            ad_element.screenshot(screenshot_path)
            print(f"Screenshot saved for Library ID {lib_id} at {screenshot_path}")
            
            if i < 2:  # Delete the first two screenshots (to avoid cropping)
                os.remove(screenshot_path)
                print(f"Deleted cropped screenshot for Library ID {lib_id}")
        
        except Exception as e:
            print(f"Error capturing screenshot for Library ID {lib_id}: {e}")
        
        # Introduce random human-like delays
        time.sleep(random.uniform(8, 15))
    
    # Re-capture the first two screenshots (after they were deleted)
    for i, (lib_id, ad_element) in enumerate(library_data[:2]):
        try:
            screenshot_path = os.path.join(folder_path, f"{lib_id}.png")
            ad_element.screenshot(screenshot_path)
            print(f"Re-captured Screenshot for Library ID {lib_id} at {screenshot_path}")
        except Exception as e:
            print(f"Error capturing re-screenshot for Library ID {lib_id}: {e}")
        
        # Introduce random human-like delays
        time.sleep(random.uniform(8, 15))

# Main function
def main():
    # Ask user for the Facebook Ads link
    facebook_ads_link = input("Enter the Facebook Ads link: ")

    # Ask user for the folder location to save the output
    folder_path = input("Enter the folder path where you want to save the output: ")

    # Set up Selenium WebDriver for Edge
    edge_options = Options()
    edge_options.add_argument("--headless")  # Run in headless mode
    service = Service("D:\\Tools\\edgedriver\\edgedriver.exe")  # Path to EdgeDriver
    driver = webdriver.Edge(service=service, options=edge_options)  # Use Edge WebDriver

    try:
        # Load the Facebook Ads page
        driver.get(facebook_ads_link)
        time.sleep(random.uniform(15, 25))  # Wait for a random time between 15 and 25 seconds

        # Extract unique library IDs and corresponding ad elements
        library_data = extract_library_ids(driver)
        library_ids = [item[0] for item in library_data]

        # Capture ad screenshots
        capture_ad_screenshots(library_data, folder_path)

        # Generate library ID URLs
        library_urls = generate_library_urls(library_ids)

        # Create a DataFrame
        data = {
            "S.No.": range(1, len(library_ids) + 1),
            "Library ID": library_ids,
            "Library ID URL": library_urls
        }
        df = pd.DataFrame(data)

        # Save to Excel in the specified folder
        excel_path = os.path.join(folder_path, "facebook_ads_library_ids.xlsx")
        df.to_excel(excel_path, index=False)
        print(f"Excel file 'facebook_ads_library_ids.xlsx' created successfully at {excel_path}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
