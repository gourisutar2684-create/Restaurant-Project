import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. LOAD DATA
# --------------------------------

data = pd.read_csv("restaurants.csv")

print("========== RESTAURANT DATA ==========")
print(data)

# --------------------------------
# 2. BASIC INFORMATION
# --------------------------------

print("\n========== BASIC INFORMATION ==========")

print("Total Restaurants:", len(data))

print("\nColumns:")
print(data.columns)

print("\nData Information:")
print(data.info())

# --------------------------------
# 3. MISSING VALUES
# --------------------------------

print("\n========== MISSING VALUES ==========")

print(data.isnull().sum())

# --------------------------------
# 4. DUPLICATE RECORDS
# --------------------------------

print("\n========== DUPLICATE RECORDS ==========")

print("Duplicate Rows:", data.duplicated().sum())

# --------------------------------
# 5. CUISINE ANALYSIS
# --------------------------------

print("\n========== CUISINE ANALYSIS ==========")

print(data["Cuisine"].value_counts())

# --------------------------------
# 6. AVERAGE PRICE
# --------------------------------

print("\n========== AVERAGE PRICE ==========")

print("Average Price:", data["Price"].mean())

# --------------------------------
# 7. AVERAGE RATING
# --------------------------------

print("\n========== AVERAGE RATING ==========")

print("Average Rating:", data["Rating"].mean())

# --------------------------------
# 8. HIGHEST RATED RESTAURANTS
# --------------------------------

print("\n========== HIGHEST RATED RESTAURANTS ==========")

highest_rating = data.sort_values(
    "Rating",
    ascending=False
)

print(highest_rating[
    ["Restaurant_ID", "Cuisine", "Rating"]
].head(10))

# --------------------------------
# 9. AREA-WISE RESTAURANTS
# --------------------------------

print("\n========== AREA-WISE RESTAURANTS ==========")

print(data["Area"].value_counts())

# --------------------------------
# 10. ONLINE ORDERING
# --------------------------------

print("\n========== ONLINE ORDERING ==========")

print(data["Online_Order"].value_counts())

# --------------------------------
# 11. DELIVERY
# --------------------------------

print("\n========== DELIVERY ==========")

print(data["Delivery"].value_counts())

# --------------------------------
# 12. WEBSITE
# --------------------------------

print("\n========== WEBSITE ==========")

print(data["Website"].value_counts())

# --------------------------------
# 13. SOCIAL PRESENCE
# --------------------------------

print("\n========== SOCIAL PRESENCE ==========")

print(data["Social_Presence"].value_counts())

# --------------------------------
# 14. CUISINE-WISE AVERAGE RATING
# --------------------------------

print("\n========== CUISINE-WISE AVERAGE RATING ==========")

print(
    data.groupby("Cuisine")["Rating"].mean()
)

# --------------------------------
# 15. CUISINE-WISE AVERAGE PRICE
# --------------------------------

print("\n========== CUISINE-WISE AVERAGE PRICE ==========")

print(
    data.groupby("Cuisine")["Price"].mean()
)

# --------------------------------
# 16. PRICE AND RATING
# --------------------------------

print("\n========== PRICE AND RATING ==========")

print(
    data[["Price", "Rating"]].corr()
)

# --------------------------------
# 17. AREA-WISE AVERAGE PRICE
# --------------------------------

print("\n========== AREA-WISE AVERAGE PRICE ==========")

print(
    data.groupby("Area")["Price"].mean()
)

# --------------------------------
# 18. BASIC CHART - CUISINE
# --------------------------------

data["Cuisine"].value_counts().plot(
    kind="bar",
    title="Restaurant Count by Cuisine"
)

plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# --------------------------------
# 19. BASIC CHART - RATING
# --------------------------------

data["Rating"].plot(
    kind="hist",
    title="Restaurant Rating Distribution",
    bins=5
)

plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# --------------------------------
# 20. FINAL MESSAGE
# --------------------------------

print("\n========== PROJECT ANALYSIS COMPLETE ==========")

print("Data loading completed.")
print("Data cleaning checked.")
print("Cuisine analysis completed.")
print("Price analysis completed.")
print("Rating analysis completed.")
print("Area analysis completed.")
print("Digital presence analysis completed.")

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv("restaurants.csv")

print("========== RESTAURANT DATA ==========")
print(df)

# 2. Basic Information
print("\n========== BASIC INFORMATION ==========")
print("Total Restaurants:", len(df))
print("\nColumns:")
print(df.columns)

# 3. Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. Duplicate Records
print("\n========== DUPLICATES ==========")
print("Duplicate Records:", df.duplicated().sum())

# 5. Cuisine-wise Count
print("\n========== CUISINE-WISE COUNT ==========")
print(df["Cuisine"].value_counts())

# 6. Average Price
print("\n========== AVERAGE PRICE ==========")
print("Average Price:", round(df["Price"].mean(), 2))

# 7. Average Rating
print("\n========== AVERAGE RATING ==========")
print("Average Rating:", round(df["Rating"].mean(), 2))

# 8. Highest Rated Restaurants
print("\n========== HIGHEST RATED ==========")
print(df[["Restaurant_ID", "Cuisine", "Rating"]]
      .sort_values("Rating", ascending=False).head())

# 9. Area-wise Count
print("\n========== AREA-WISE COUNT ==========")
print(df["Area"].value_counts())

# 10. Online Ordering
print("\n========== ONLINE ORDER ==========")
print(df["Online_Order"].value_counts())

# 11. Delivery
print("\n========== DELIVERY ==========")
print(df["Delivery"].value_counts())

# 12. Website
print("\n========== WEBSITE ==========")
print(df["Website"].value_counts())

# 13. Social Presence
print("\n========== SOCIAL PRESENCE ==========")
print(df["Social_Presence"].value_counts())

# 14. Cuisine-wise Average Rating
print("\n========== CUISINE-WISE AVG RATING ==========")
print(df.groupby("Cuisine")["Rating"].mean().round(2))

# 15. Cuisine-wise Average Price
print("\n========== CUISINE-WISE AVG PRICE ==========")
print(df.groupby("Cuisine")["Price"].mean().round(2))

# 16. Area-wise Average Price
print("\n========== AREA-WISE AVG PRICE ==========")
print(df.groupby("Area")["Price"].mean().round(2))

# 17. Restaurants Rating Above 4
print("\n========== RATING ABOVE 4 ==========")
print(df[df["Rating"] > 4][
    ["Restaurant_ID", "Cuisine", "Price", "Rating"]
])

# 18. Price Above Average
avg_price = df["Price"].mean()

print("\n========== PRICE ABOVE AVERAGE ==========")
print(df[df["Price"] > avg_price][
    ["Restaurant_ID", "Menu_Item", "Price"]
])

# 19. Online Ordering Available
print("\n========== ONLINE ORDER AVAILABLE ==========")
print(df[df["Online_Order"] == "Yes"][
    ["Restaurant_ID", "Cuisine", "Online_Order"]
])

# 20. Weak Digital Presence
print("\n========== WEAK DIGITAL PRESENCE ==========")
print(df[df["Social_Presence"] == "Low"][
    ["Restaurant_ID", "Website", "Online_Order", "Social_Presence"]
])

# 21. Delivery Available
print("\n========== DELIVERY AVAILABLE ==========")
print(df[df["Delivery"] == "Yes"][
    ["Restaurant_ID", "Cuisine", "Delivery"]
])

# 22. Most Reviewed Restaurants
print("\n========== MOST REVIEWED ==========")
print(df[["Restaurant_ID", "Reviews"]]
      .sort_values("Reviews", ascending=False).head())

# 23. Offers Available
print("\n========== OFFERS AVAILABLE ==========")
print(df[df["Offers"] == "Yes"][
    ["Restaurant_ID", "Cuisine", "Offers"]
])

# 24. Price-Rating Correlation
print("\n========== PRICE-RATING CORRELATION ==========")
print(df["Price"].corr(df["Rating"]))

# 25. Final Summary
print("\n========== FINAL SUMMARY ==========")
print("Total Restaurants:", len(df))
print("Average Price:", round(df["Price"].mean(), 2))
print("Average Rating:", round(df["Rating"].mean(), 2))
print("Total Reviews:", df["Reviews"].sum())

# ================= CHARTS =================

# Chart 1: Cuisine Count
df["Cuisine"].value_counts().plot(kind="bar")
plt.title("Restaurants by Cuisine")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# Chart 2: Average Price by Cuisine
df.groupby("Cuisine")["Price"].mean().plot(kind="bar")
plt.title("Average Price by Cuisine")
plt.xlabel("Cuisine")
plt.ylabel("Average Price")
plt.tight_layout()
plt.show()

# Chart 3: Average Rating by Cuisine
df.groupby("Cuisine")["Rating"].mean().plot(kind="bar")
plt.title("Average Rating by Cuisine")
plt.xlabel("Cuisine")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# Chart 4: Restaurants by Area
df["Area"].value_counts().plot(kind="bar")
plt.title("Restaurants by Area")
plt.xlabel("Area")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# Chart 5: Price vs Rating
plt.scatter(df["Price"], df["Rating"])
plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

print("\n========== ANALYSIS COMPLETED ==========")

