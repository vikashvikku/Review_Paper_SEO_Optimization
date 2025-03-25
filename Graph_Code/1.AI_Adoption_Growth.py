import matplotlib.pyplot as plt
import numpy as np

# Data for AI adoption in digital marketing (2015-2025)
years = np.arange(2015, 2026, 1)
ai_adoption_rate = [5, 8, 12, 18, 25, 35, 45, 55, 65, 75, 82]  # Hypothetical percentage adoption

# Plot the graph
plt.figure(figsize=(8,5))
plt.plot(years, ai_adoption_rate, marker='o', linestyle='-', color='b', label="AI Adoption Rate")

# Labels and title
plt.xlabel("Year")
plt.ylabel("AI Adoption in Digital Marketing (%)")
plt.title("Growth of AI in Digital Marketing (2015-2025)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
