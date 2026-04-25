try:
    with open("complaints.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Complaint file not found!")