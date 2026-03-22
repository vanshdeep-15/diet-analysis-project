import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("All_Diets.csv")

# Fill missing values
cols = ['Protein(g)', 'Carbs(g)', 'Fat(g)']
df[cols] = df[cols].fillna(df[cols].mean())

# Average macros
avg_macros = df.groupby('Diet_type')[cols].mean()
print(avg_macros)

# Top protein recipes
top_protein = (
    df.sort_values('Protein(g)', ascending=False)
    .groupby('Diet_type')
    .head(5)
)

# Plot 1: Bar chart
plt.figure(figsize=(10,6))
sns.barplot(x=avg_macros.index, y=avg_macros['Protein(g)'])
plt.title("Average Protein by Diet Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/figure_1.png")
plt.close()

# Plot 2: Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(avg_macros, annot=True, cmap="coolwarm")
plt.title("Macronutrient Distribution by Diet Type")
plt.tight_layout()
plt.savefig("outputs/figure_2.png")
plt.close()

# Plot 3: Scatter
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=top_protein,
    x='Protein(g)',
    y='Carbs(g)',
    hue='Cuisine_type'
)
plt.title("Top Protein-Rich Recipes by Cuisine")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("outputs/figure_3.png")
plt.close()

print("✅ Analysis complete! Graphs saved in outputs folder.")