import matplotlib.pyplot as plt
import numpy as np


# Data for AI impact on SEO metrics (Traditional SEO vs AI-powered SEO)
metrics = ["CTR (%)", "Bounce Rate (%)", "Page Ranking", "Organic Traffic (%)"]
traditional_seo = [4, 60, 30, 50]  # Hypothetical values for traditional SEO
ai_powered_seo = [12, 35, 10, 85]  # Hypothetical values for AI-powered SEO

# Bar Chart
x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(8,5))
bars1 = ax.bar(x - width/2, traditional_seo, width, label='Traditional SEO', color='r')
bars2 = ax.bar(x + width/2, ai_powered_seo, width, label='AI-Powered SEO', color='g')

# Labels and title
ax.set_xlabel("SEO Metrics")
ax.set_ylabel("Performance Value")
ax.set_title("Impact of AI on SEO Metrics")
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
