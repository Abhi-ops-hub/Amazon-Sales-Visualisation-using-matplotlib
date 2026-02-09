import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"amazon.csv")

# Drop rows with missing critical values
df = df.dropna(subset=['product_name', 'user_id', 'review_id'])

# Top 10 most reviewed products
most_sell = df['product_name'].value_counts().head(10)

# plt.figure(figsize=(10, 8))

colors = ['r','y','m','g','b','k','c','skyblue','orange','purple']

plt.bar(
    most_sell.index,
    most_sell.values,
    color=colors,
    label='Review Count'
)

plt.xlabel("Product Name")
plt.ylabel("Number of Reviews")
plt.title("Top 10 Most Reviewed Products on Amazon")

plt.legend(fontsize=10)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("top_reviewed.png", dpi=300, bbox_inches='tight')
plt.show()
