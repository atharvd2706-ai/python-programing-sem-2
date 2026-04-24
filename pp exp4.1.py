def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    topper = max(marks)
    
    return average, topper

marks = [75, 88, 92, 67, 90]

avg, top = analyze_marks(marks)

print("Average Marks:", avg)
print("Topper Marks:", top)