import matplotlib.pyplot as plt
import numpy as np

# Data for Voice Search Adoption Growth (2018-2025)
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
voice_search_adoption = [8, 15, 25, 37, 50, 65, 78, 90]  # Hypothetical adoption percentage

# Line Graph for Voice Search Adoption Growth
plt.figure(figsize=(8,5))
plt.plot(years, voice_search_adoption, marker='d', linestyle='-', color='r', label="Voice Search Adoption")

# Labels and Title
plt.xlabel("Year")
plt.ylabel("Adoption Rate (%)")
plt.title("Growth of Voice Search Adoption (2018-2025)")
plt.xticks(years)
plt.yticks(range(0, 101, 10))
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
