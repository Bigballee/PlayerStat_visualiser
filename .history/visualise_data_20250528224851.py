import json
import matplotlib.pyplot as plt
import pandas as pd


def plot_etoo_stats():
    # Load Eto'o stats data
    with open("etoo_stats.json", "r") as f:
        etoo_data = json.load(f)

    df = pd.DataFrame(etoo_data)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.bar(df['Competition'], df['Appearances'], label='Appearances', alpha=0.6)
    plt.bar(df['Competition'], df['Goals'], label='Goals', alpha=0.6)
    plt.bar(df['Competition'], df['Assists'], label='Assists', alpha=0.6)

    plt.title("Eto'o Stats per Competition")
    plt.xlabel("Competition")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # Save the plot
    plt.savefig("etoo_stats_plot.png")
    print("✅ Eto'o stats plot saved as etoo_stats_plot.png") 

