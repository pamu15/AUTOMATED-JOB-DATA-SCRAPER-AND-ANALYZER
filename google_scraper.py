import time
from datetime import datetime
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# -------------------------------
# Function: Scrape Google Results
# -------------------------------
def google_search_scraper(driver, query, pages=3):
    data = []

    for page in range(pages):
        print(f"Scraping page {page+1} for query: {query}")

        driver.get(f"https://www.google.com/search?q={query}&start={page*10}")
        time.sleep(5)

        results = driver.find_elements(By.CSS_SELECTOR, "div.g")

        for r in results:
            try:
                title = r.find_element(By.CSS_SELECTOR, "h3").text
                link = r.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                # Description (snippet)
                try:
                    description = r.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                except:
                    description = "N/A"

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                data.append({
                    "Query": query,
                    "Title": title,
                    "Link": link,
                    "Description": description,
                    "Scraped_At": timestamp
                })

            except:
                continue

    return data


# -------------------------------
# Main Execution
# -------------------------------
def main():
    # Queries (you can add more)
    queries = [
        "Python developer jobs",
        "Data analyst jobs",
        "Power BI developer jobs"
    ]

    # Start browser
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)

    all_data = []

    # Loop through queries
    for query in queries:
        results = google_search_scraper(driver, query, pages=3)
        all_data.extend(results)

    driver.quit()

    # -------------------------------
    # Convert to DataFrame
    # -------------------------------
    df = pd.DataFrame(all_data)

    # Remove duplicates
    df.drop_duplicates(subset="Link", inplace=True)

    # -------------------------------
    # Save to Excel (multi-sheet)
    # -------------------------------
    filename = f"google_jobs_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"

    with pd.ExcelWriter(filename) as writer:
        for query in queries:
            df_query = df[df["Query"] == query]
            sheet_name = query[:30]  # Excel sheet name limit
            df_query.to_excel(writer, sheet_name=sheet_name, index=False)

        # All data sheet
        df.to_excel(writer, sheet_name="All_Data", index=False)

    print(f"\n✅ Data saved successfully: {filename}")


# -------------------------------
# Run Script
# -------------------------------
if __name__ == "__main__":
    main()