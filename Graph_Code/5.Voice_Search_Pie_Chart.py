import matplotlib.pyplot as plt

# Data for voice search optimization adoption
labels = ["Fully Optimized", "Partially Optimized", "Not Optimized"]
sizes = [45, 35, 20]  # Hypothetical percentages
colors = ["#66c2a5", "#fc8d62", "#8da0cb"]
explode = (0.1, 0, 0)  # Exploding the first slice for emphasis

# Create pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, explode=explode, startangle=140, shadow=True)
plt.title("AI-Driven Voice Search Optimization Adoption (2025)")
plt.show()
