import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=wireless+earbuds"

# STRONG HEADERS to bypass basic blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

response = requests.get(url, headers=headers)

print("Response status code:", response.status_code)
print("Length of page content:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

# FIND ELEMENTS
names = soup.find_all("a", class_="IxWX8O")
prices = soup.find_all("div", class_="hZ3P6w")
ratings = soup.find_all("div", class_="MKiFS6")

print("Products found:", len(names))
print("\nSample Output:\n")

for i in range(min(5, len(names))):
    name = names[i].text.strip()
    price = prices[i].text.strip() if i < len(prices) else "N/A"
    rating = ratings[i].text.strip() if i < len(ratings) else "N/A"

    print(f"Product: {name}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print("-" * 40)