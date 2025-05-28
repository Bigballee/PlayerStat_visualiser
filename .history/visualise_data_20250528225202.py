import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_etoo_stats():
    # Load Players stats data
    with open("drogba_stats.json", "r") as f:
        drogba_data = json.load(f)

    df = pd.DataFrame(drogba_data)

    # Sort by appearances for clearer chart (optional)
    df = df.sort_values(by="Appearances", ascending=False)

    x = np.arange(len(df['Competition']))
    width = 0.25

    # Plotting grouped bars
    plt.figure(figsize=(14, 7))
    plt.bar(x - width, df['Appearances'], width, label='Appearances', color='skyblue')
    plt.bar(x, df['Goals'], width, label='Goals', color='orange')
    plt.bar(x + width, df['Assists'], width, label='Assists', color='green')

    plt.title("Drogba Stats per Competition")
    plt.xlabel("Competition")
    plt.ylabel("Count")
    plt.xticks(x, df['Competition'], rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    # Save before showing
    plt.savefig("Drogbas_stats_plot.png")
    print("✅ Drogba stats plot saved as drogba_stats_plot.png")

    plt.show()

plot_drogba_stats()


