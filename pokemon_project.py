import matplotlib.pyplot as plt
import pandas as pd

poke = pd.read_csv("pokemon.csv")
plt.figure(figsize=(10, 7))
plt.title("Pokemon", fontdict={"fontsize": 15, "fontweight": "bold"})

attack = poke.groupby('Type 1').agg({'Attack': 'mean'})
defense = poke.groupby('Type 1').agg({'Defense': 'mean'})
hp = poke.groupby('Type 1').agg({'HP': 'mean'})
speed = poke.groupby('Type 1').agg({'Speed': 'mean'})

plt.plot(attack, marker=".", label="Attack")
plt.plot(defense, marker=".", label="Defense")
plt.plot(hp, marker=".", label="HP")
plt.plot(speed, marker=".", label="Speed")

plt.xlabel("Type")
plt.ylabel("Power")

plt.yticks([30, 40, 50, 60, 70, 80, 90, 100])


plt.legend()
plt.savefig("Pokemon Graph.png", dpi=300)
plt.show()



