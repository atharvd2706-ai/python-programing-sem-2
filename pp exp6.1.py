total = 20

with open("expenses.txt", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            total += float(parts[1])

print("Total monthly expense:", total)