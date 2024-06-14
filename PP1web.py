import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.header("Welcome to the BMI Calculator")
    
    weight = st.number_input("Please enter your weight in kilograms: ", min_value=10)
    height = st.slider("Please enter your height in meters: ",min_value=0.2,max_value=3.0)
    btn=st.button("Calculate")
    if btn:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        st.subheader(f"\nYour BMI is: {bmi:.2f}")
        st.subheader(f"Health category: {category}")

if __name__ == "__main__":
    main()
