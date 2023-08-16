import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Importing the data
data = pd.read_csv("/Users/miteshagarwal/Downloads/apple_products.csv")
print(data.head())

# Checking whether data contains null or not
print(data.isnull().sum())

# Creating the new database according ti star rating
highest_rated = data.sort_values(by=["Star Rating"], 
                                 ascending=False)

# Considering only top 10 rows
highest_rated = highest_rated.head(10)

print(highest_rated)

# Bar Chart of number of ratings of highest rated Iphone
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label, 
                y = counts, 
            title="Number of Ratings of Highest Rated iPhones")
figure.show()

# Scatter Plot of sale price of iPhones and their ratings on Flipkart
figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Sale Price", size="Discount Percentage", 
                    trendline="ols", 
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()