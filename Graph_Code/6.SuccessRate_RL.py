import matplotlib.pyplot as plt
import numpy as np

# Sample data for RL-based SEO success rate over time
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
success_rate = np.array([55, 58, 60, 63, 67, 70, 74, 78, 81, 85, 88, 92])  # Hypothetical success rate (%) over months

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(months, success_rate, color="blue", label="Success Rate (%)")
plt.plot(months, success_rate, linestyle="dashed", color="red", alpha=0.6)  # Trendline

# Labels and title
plt.xlabel("Months")
plt.ylabel("SEO Success Rate (%)")
plt.title("Reinforcement Learning in SEO – Success Rate Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Show plot
plt.show()
