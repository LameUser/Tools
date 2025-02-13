import re
import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
edge_options = Options()
edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--window-size=1920,1080')
edge_options.add_argument("--user-data-dir=C:\\Users\\gopal\\AppData\\Local\\Microsoft\\Edge\\User Data")
edge_options.add_argument("--profile-directory=Default")
edge_driver_path = r"D:\\Tools\\edgedriver\\edgedriver.exe"

# Delete the DevToolsActivePort file if it exists
devtools_port_path = os.path.join("C:\\Users\\gopal\\AppData\\Local\\Microsoft\\Edge\\User Data\\DevToolsActivePort")
if os.path.exists(devtools_port_path):
    os.remove(devtools_port_path)

service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# Open Telegram Web
driver.get('https://web.telegram.org/')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
time.sleep(5)  # Ensure it's fully loaded

# Function to parse Telegram IDs and links from a file
def parse_ids(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    ids = re.findall(r'@\w+|https?://t\.me/\S+', content)
    links = []

    for id in ids:
        if id.startswith('@'):
            links.append(f"https://web.telegram.org/k/#@{id[1:]}")
        elif id.startswith('http'):
            id_part = id.split('/')[-1]
            links.append(f"https://web.telegram.org/k/#@{id_part}")

    return ids, links

# Function to take screenshot
def capture_screenshot(username, link, output_dir):
    driver.get(link)
    
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'sidebar-header.topbar.has-avatar')))
    except:
        print(f"Failed to load chat for {link}")
        return

    time.sleep(5)  # Allow time for elements to load

    # Take Screenshot
    screenshot_path = os.path.join(output_dir, f"{username}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

# Main function
def main(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    usernames, links = parse_ids(input_file)
    for username, link in zip(usernames, links):
        try:
            capture_screenshot(username, link, output_dir)
        except Exception as e:
            print(f"Failed to process {link}: {e}")

    driver.quit()

# Usage
if __name__ == "__main__":
    input_file = r"D:\\Desktop\\TelegramID\\Tele_output.txt"
    output_dir = r"D:\\Desktop\\TelegramID\\Screenshots"
    main(input_file, output_dir)
