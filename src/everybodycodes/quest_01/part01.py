from collections import Counter

with open("data/quest-01/part01.txt") as f:
    line = f.readline()

cnt = Counter(line)

potions = cnt["A"] * 0 + cnt["B"] * 1 + cnt["C"] * 3
print(f"Potions needed: {potions}")
