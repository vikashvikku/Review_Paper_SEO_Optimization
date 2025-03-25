import matplotlib.pyplot as plt

# Define years (2018-2025)
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

# Data for AI-Powered SEO & Voice Search Optimization Growth
ai_seo_growth = [10, 18, 30, 45, 60, 75, 85, 95]  # Hypothetical percentage
voice_search_growth = [5, 12, 22, 35, 50, 67, 80, 92]  # Hypothetical percentage

# Plot the graph
plt.figure(figsize=(8,5))
plt.plot(years, ai_seo_growth, marker='o', linestyle='-', color='g', label="AI in SEO Growth")
plt.plot(years, voice_search_growth, marker='s', linestyle='--', color='b', label="Voice Search Optimization Growth")

plt.xlabel("Year")
plt.ylabel("Adoption Rate (%)")
plt.title("AI-Powered SEO & Voice Search Optimization Growth (2018-2025)")
plt.xticks(years)
plt.yticks(range(0, 101, 10))
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
