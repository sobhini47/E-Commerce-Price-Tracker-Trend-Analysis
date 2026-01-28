from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.flipkart.com/search?q=wireless+earbuds"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(url)

wait = WebDriverWait(driver, 15)

# Close login popup (VERY IMPORTANT)
try:
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    )
    close_btn.click()
except:
    pass

# Wait until products load
wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/p/')]"))
)

# XPATH selectors (RELIABLE)
names = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")
prices = driver.find_elements(By.XPATH, "//div[contains(text(),'₹')]")
ratings = driver.find_elements(By.XPATH, "//div[contains(@class,'XQDdHH')]")

print("Products found:", len(names))
print("\nSample Output:\n")

for i in range(min(5, len(names))):
    name = names[i].text
    price = prices[i].text if i < len(prices) else "N/A"
    rating = ratings[i].text if i < len(ratings) else "N/A"

    if name.strip() != "":
        print(f"Product: {name}")
        print(f"Price: {price}")
        print(f"Rating: {rating}")
        print("-" * 40)

driver.quit()