import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cuisines.csv")
print(df.head())
cuisines_series=df['Cuisines'].dropna().str.split(',')
all_cuisines=cuisines_series.explode()
cuisines_counts = all_cuisines.value_counts()
top_3_cuisines=cuisines_counts.head(3)
total_restaurants=len(df)
top_3_percentage = (top_3_cuisines/total_restaurants)*100
result = pd.DataFrame({
    "Cuisine": top_3_cuisines.index,
    "Number of Restaurants": top_3_cuisines.values,
    "Percentage (%)": top_3_percentage.values
})
print(result)
plt.figure()
plt.bar(result['Cuisine'],result['Number of Restaurants'])
plt.xlabel('Cuisine')
plt.ylabel('Number of Restaurants')
plt.title('Top 3 Most Comman Cuisines')
plt.savefig("Top_3_Cuisines.png", bbox_inches = "tight")
plt.show()
result.to_csv("Top_3_Cuisines_Result.csv",index=False)