import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("Cuisines.csv")
price_count = df['Price range'].value_counts().sort_index()
total_restaurants = len(df)
price_percentage = (price_count/total_restaurants)*100
result = pd.DataFrame({ "Price Range": price_count.index,"Number of Restaurants": price_count.values,"Percentage": price_percentage.values})
print(result)
plt.figure()
plt.bar(result["Price Range"], result["Number of Restaurants"])
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Price Range Distribution of Restaurants")
plt.show()
