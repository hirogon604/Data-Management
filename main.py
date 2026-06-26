import random

heads = 0
tails = 0

print("Tossing a coin...")

for i in range(1, 4):
    if random.choice(["Heads", "Tails"]) == "Heads":
        print(f"Round {i}: Heads")
        heads += 1
    else:
        print(f"Round {i}: Tails")
        tails += 1

print(f"Heads: {heads}")
print(f"Tails: {tails}")
