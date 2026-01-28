from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

url = "https://www.flipkart.com/search?q=wireless+earbuds"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(url)

wait = WebDriverWait(driver, 15)

# Close login popup
try:
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    )
    close_btn.click()
except:
    pass

# Wait for product cards
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-id]")))

products = driver.find_elements(By.XPATH, "//div[@data-id]")

print("Products scraped:", len(products))

# Save to CSV
with open("ecommerce_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    for product in products:
        # Product Name
        try:
            name = product.find_element(By.XPATH, ".//a[@title]").get_attribute("title")
        except:
            name = "N/A"

        # Price
        try:
            price = product.find_element(By.XPATH, ".//div[contains(text(),'₹')]").text
        except:
            price = "N/A"

        # Rating
        try:
            rating_div = product.find_element(By.XPATH, ".//div[contains(@class,'MKiFS6')]")
            rating = rating_div.text.strip()  # e.g., "4" or "3.9"
        except:
            rating = "N/A"

        writer.writerow([name, price, rating])

print("✅ Data saved to ecommerce_data.csv")
driver.quit()