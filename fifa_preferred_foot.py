import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("fifa_data.csv")

plt.title("Foot Preference of FIFA Players", fontdict={"fontsize": 15})

left = fifa.loc[fifa["Preferred Foot"] == "Left"].count()[0]
right = fifa.loc[fifa["Preferred Foot"] == "Right"].count()[0]

labels = ["Left", "Right"]
colors = ["#64CCC5", "#176B87"]

plt.pie([left, right], labels=labels, colors=colors, autopct="%.2f %%")

plt.savefig("FIFA Preferred Foot Graph.png", dpi=300)
plt.show()



