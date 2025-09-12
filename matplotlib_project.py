import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\DELL\Downloads\vgsales.csv")

"""Ques. Market Share of Top Publishers
Problem: You work for a new game studio and need to understand the competitive landscape. Your goal is to identify the publishers with the largest market share in terms of global sales to determine who your main competitors are.
How can you use a pie chart to visualize the percentage of global sales for the top 5 publishers? **bold text**
"""

publisher_global_sales = df.groupby('Publisher', as_index=False)['Global_Sales'].sum()
publisher_global_sales = publisher_global_sales.sort_values(by='Global_Sales', ascending=False).head(5)

labels = publisher_global_sales['Publisher'].tolist()
sizes = publisher_global_sales['Global_Sales'].tolist()

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Market Share of Top 5 Video Game Publishers', fontweight='bold')
plt.show()



"""Ques. Trends in Game Sales Over Time
Problem: A game developer wants to see how the "Sports" genre has performed over the years to help predict future trends.
How can you create a line plot to show the total worldwide sales (Global_Sales) for the "Sports" genre from the first year in the data to the last? **bold text**
"""

sports_global_sales = df[df['Genre'] == 'Sports'][['Year', 'Global_Sales']]

sports_global_sales = sports_global_sales.groupby('Year')['Global_Sales'].sum().reset_index()

x = sports_global_sales['Year']
y = sports_global_sales['Global_Sales']

plt.plot(x, y)
plt.title('Global_Sales for the "Sports" genre ')
plt.xlabel('Year')
plt.ylabel('Global_Sales')
plt.grid()
plt.show()



"""Ques. Regional Popularity of Game Genres
Problem: A marketing team needs to decide where to focus advertising efforts for an upcoming Action game. They need to know which regions (NA_Sales, EU_Sales, JP_Sales) have been historically most receptive to this genre.
How can you create a grouped bar chart to compare the total sales of Action games in North America, Europe, and Japan? **bold text**
"""

action_genre_sales = df[df['Genre'] == 'Action'].groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum()

x = action_genre_sales.index
y_cols = ['NA_Sales', 'EU_Sales', 'JP_Sales']

bar_width = 0.25
x_pos = range(len(x))

plt.figure(figsize=(14, 6))

for i, col in enumerate(y_cols):
    plt.bar(
        [p + i*bar_width for p in x_pos],
        action_genre_sales[col],
        width=bar_width,
        label=col
    )

plt.xticks([p + bar_width for p in x_pos], x, rotation=45)
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.title("Grouped Bar Chart Example")
plt.legend()
plt.tight_layout()
plt.show()



"""Ques. Platform-Specific Genre Performance
Problem: As an analyst for a console manufacturer, you need to understand which game genres are most successful on a specific platform, like the Nintendo Wii.
How can you use a horizontal bar chart to show the total sales for each Genre on the Wii platform, sorted from highest to lowest sales? **bold text**
"""

wii_platform = df[df['Platform'] == 'Wii']

r1 = wii_platform.groupby('Genre')['Global_Sales'].sum().reset_index()

r1 = r1.sort_values(by='Global_Sales', ascending=False)

x = r1['Global_Sales']
y = r1['Genre']

plt.figure(figsize=(10,6))
plt.barh(y, x, color='skyblue')

plt.xlabel("Total Global Sales (Millions)")
plt.ylabel("Genre")
plt.title("Genre Performance on Wii Platform")
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()