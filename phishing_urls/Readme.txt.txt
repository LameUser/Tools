Google Search Filtering & URL Extraction Tool
=============================================

This Python script performs a **Google search** using a predefined query, filters the results based on **whitelisted domains**, and saves the **filtered URLs** to an Excel file.

----------------------------------------

Features:
---------
✔ Uses Google search to find URLs based on a **custom Google Dork query**.  
✔ Filters **non-whitelisted domains** to exclude unwanted results.  
✔ Saves results **automatically** in an **Excel (.xlsx) file**.  
✔ Adds **randomized time delays** between searches to avoid detection by Google.  

----------------------------------------

Requirements:
-------------
- Python 3.x
- Required Python libraries:
 ` pip install google-search-results openpyxl `
- **Stable Internet Connection** (since the script fetches data from Google).

----------------------------------------

How to Use:
-----------
1. **Modify the search query**:
 - The script uses a **Google Dork** query to filter results from `.gov.in` domains and identify suspicious redirections.
 - Update the query in the script as needed:
   ```python
   query = ("porn | gaming | telegram | gambling | money | investment | stocks | crypto "
            "site:*.gov.in AND (inurl:.com | inurl:.net | inurl:.xyz | inurl:.ru | inurl:.tk | "
            "inurl:.ml | inurl:.cf | inurl:.ga | inurl:.gq | inurl:.info | inurl:.top | inurl:.biz | "
            "inurl:.pw | inurl:.cn | inurl:.co | inurl:.io)")
   ```

2. **Update the whitelist (if needed)**:
 - If you want to exclude certain domains from filtering, add them to `whitelisted_domains`:
   ```python
   whitelisted_domains = ["gov.in", "nic.in"]
   ```

3. **Run the script**:
    ` python google_search_filter.py `


4. **Check the output**:
- The script saves **filtered URLs** in an Excel file:
  ```
  D:\Desktop\RedirectGOV\filtered_urls.xlsx
  ```
- The first column of the Excel sheet contains all the **filtered URLs**.

Example Output:
---------------
 ```
 Starting Google search... Fetched URL: https://gov.in/suspicious-link Added to filtered list: https://gov.in/suspicious-link 
 Total URLs fetched: 95 Data saved to D:\Desktop\RedirectGOV\filtered_urls.xlsx
 ```

----------------------------------------

Troubleshooting:
----------------
❌ **Issue:** Getting `Error during search`  
✅ **Solution:**  
   - Ensure you have a **stable internet connection**.  
   - Google may have **blocked your requests**. Increase the delay in:
     ```python
     time.sleep(random.uniform(5, 10))
     ```
   - Try reducing `max_results` to avoid bot detection.

❌ **Issue:** No URLs are being fetched  
✅ **Solution:**  
   - Ensure the **query is correct and relevant**.
   - Try running the script **at a different time** (Google may temporarily block automated searches).

----------------------------------------

Customization:
--------------
- Modify the **Google Dork query** for different categories of searches.
- Adjust the **sleep interval** to avoid bot detection.
- Add more **filtering logic** for specific URLs.

----------------------------------------

Credits:
--------
Developed using:
- `google-search-results` for performing searches.
- `openpyxl` for saving results to Excel.
