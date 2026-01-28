import pandas as pd

df = pd.read_csv("ecommerce_data_cleaned.csv")

print(df.head())

print(df.info())

print(df.describe())

import matplotlib.pyplot as plt

# Plot Price Distribution

plt.hist(df['Price'], bins=10)
plt.xlabel("Price (₹)")
plt.ylabel("Number of Products")
plt.title("Price Distribution of Flipkart Earbuds")
plt.show()


# Plot Rating Distribution

plt.hist(df['Rating'], bins=8)
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.title("Rating Distribution of Flipkart Earbuds")
plt.show()


# Scatter Plot (Price vs Rating)

plt.scatter(df['Price'], df['Rating'])
plt.xlabel("Price (₹)")
plt.ylabel("Rating")
plt.title("Price vs Rating of Flipkart Earbuds")
plt.show()

# STEP 5: Identify Top Rated Products
#Find the highest-rated earbuds available.
# Sort by Rating (Descending)

top_rated = df.sort_values(by="Rating", ascending=False)

print(top_rated.head(10)[['Product Name', 'Price', 'Rating']])

#STEP 6: Best Budget Products (Value for Money)
# Identify products under ₹800 with high ratings (≥ 4.0)
# Filter Best Budget Products

best_budget = df[(df['Price'] < 800) & (df['Rating'] >= 4.0)]

print(best_budget[['Product Name', 'Price', 'Rating']])


#STEP 7: Brand-wise Analysis
#Understand which brands perform best in terms of:
# Average rating and Average price
#  Extract Brand Name

df['Brand'] = df['Product Name'].str.split().str[0]

print(df[['Product Name', 'Brand']].head())


# Brand-wise Average Rating
#Find which brands are best rated on average.
# Average Rating per Brand

brand_rating = (
    df.groupby('Brand')['Rating']
      .mean()
      .sort_values(ascending=False)
)

print(brand_rating)

#Brand-wise Average Price
#Understand price positioning of each brand.
#Average Price per Brand

brand_price = (
    df.groupby('Brand')['Price']
      .mean()
      .sort_values()
)

print(brand_price)
