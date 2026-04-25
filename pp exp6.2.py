with open("attendance.txt", "a") as file:
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    status = input("Present/Absent: ")

    record = f"{roll} {name} {status}\n"
    file.write(record)

print("Record added successfully!")