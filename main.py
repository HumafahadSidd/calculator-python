# def calculate_bmi(weight, height):
#     """Calculates BMI and provides health classification."""
#     bmi = weight / (height ** 2)
#     print(f"Your BMI is: {bmi:.2f}")

#     if bmi < 18.5:
#         print("You are underweight.")
#     elif 18.5 <= bmi < 25:
#         print("You are in a healthy weight range.")
#     elif 25 <= bmi < 30:
#         print("You are overweight.")
#     else:
#         print("You are obese.")

# # Get user input
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))

# calculate_bmi(weight, height)

import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kilograms:")
height = st.number_input("Enter your height in meters:")

if weight and height:
    bmi = weight / (height ** 2)
    st.write("Your BMI is:", bmi)

    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.write("You are in a healthy weight range.")
    elif 25 <= bmi < 30:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
