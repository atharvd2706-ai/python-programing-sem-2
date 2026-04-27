import streamlit as st

st.title("🎓 Student Result Calculator")

# Student name
name = st.text_input("Enter Student Name")

# Number of subjects
num_subjects = st.number_input("Number of Subjects", min_value=1, step=1)

marks = []
total = 0

for i in range(int(num_subjects)):
    mark = st.number_input(f"Marks for Subject {i+1}", min_value=0.0, max_value=100.0, key=i)
    marks.append(mark)
    total += mark

if st.button("Calculate Result"):
    percentage = total / num_subjects

    st.subheader(f"Student: {name}")
    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {round(percentage, 2)}%")

    # Grade logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "Fail"

    st.success(f"Grade: {grade}")