import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv("fifa_data.csv")

plt.title("Distribution of Player Skills in FIFA 2018", fontdict={"fontsize": 15})

bins = np.arange(40, 110, 10)

plt.hist(fifa.Overall, bins=bins, color="#abcdef")

plt.xlabel("Skill Level")
plt.ylabel("Number of Players")

plt.xticks(bins)

plt.savefig("FIFA Skill Graph.png", dpi=300)
plt.show()


