import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("fifa_data.csv")

plt.title("Professional Soccer Team Comparison", fontdict={"fontsize": 15})

madrid = fifa.loc[fifa.Club == "Real Madrid"]["Overall"]
barcelona = fifa.loc[fifa.Club == "FC Barcelona"]["Overall"]

labels = ["Real Madrid", "FC Barcelona"]

boxes = plt.boxplot([madrid, barcelona], labels=labels, patch_artist=True)

for box in boxes["boxes"]:
    box.set(color="#2D4356")


plt.ylabel("FIFA Overall Rating")

plt.savefig("FIFA Team Comparison.png", dpi=300)
plt.show()

