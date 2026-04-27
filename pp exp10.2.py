import streamlit as st

st.title("🏥 BMI Health Checker")

st.write("Enter your details to check your BMI:")

# User inputs
weight = st.number_input("Enter your weight (kg)", min_value=1.0)
height_cm = st.number_input("Enter your height (cm)", min_value=1.0)

# Convert height to meters
height_m = height_cm / 100

if st.button("Calculate BMI"):
    if height_m > 0:
        bmi = weight / (height_m ** 2)

        st.subheader(f"Your BMI: {round(bmi, 2)}")

        # BMI Categories
        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")