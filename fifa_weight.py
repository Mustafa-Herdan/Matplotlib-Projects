import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("fifa_data.csv")

plt.title("Weight Distribution of FIFA Players (in lbs)", fontdict={"fontsize": 15})

fifa.Weight = [int(x.strip("lbs")) if type(x) == str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa.loc[fifa.Weight >= 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ["Under 125", "125-150", "150-175", "175-200", "Over 200"]
colors = ["#1D5B79", "#468B97", "#EF6262", "#F3AA60", "#FAF0D7"]
explodes = [.4, .2, 0, 0, .4]

plt.pie(weights, labels=labels, colors=colors, autopct="%.2f %%", pctdistance=0.75, explode=explodes)

plt.savefig("FIFA Weight.png", dpi=300)
plt.show()


