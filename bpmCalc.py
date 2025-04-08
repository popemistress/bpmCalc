import streamlit as st

def calculate_calories_burned(sex, age, weight_kg, avg_hr, duration_min):
    """
    Calculate estimated calories burned based on heart rate, weight, age, and duration.
    :param sex: 'male' or 'female'
    :param age: Age in years
    :param weight_kg: Weight in kilograms
    :param avg_hr: Average heart rate during training (in bpm)
    :param duration_min: Duration of exercise in minutes
    :return: Estimated total calories burned
    """
    if sex.lower() == 'male':
        calories_per_min = (
            -55.0969 + (0.6309 * avg_hr) + (0.1988 * weight_kg) + (0.2017 * age)
        ) / 4.184
    elif sex.lower() == 'female':
        calories_per_min = (
            -20.4022 + (0.4472 * avg_hr) - (0.1263 * weight_kg) + (0.074 * age)
        ) / 4.184
    else:
        raise ValueError("Sex must be either 'male' or 'female'")

    total_calories = calories_per_min * duration_min
    return round(total_calories, 2)

# Streamlit interface
st.title("Heart Rate-Based Calorie Burn Calculator")

sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age (years)", min_value=10, max_value=100, value=30)
weight_kg = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0)
avg_hr = st.number_input("Average Heart Rate (bpm)", min_value=60, max_value=220, value=130)
duration_min = st.number_input("Duration of Exercise (minutes)", min_value=1, max_value=300, value=60)

if st.button("Calculate Calories Burned"):
    calories = calculate_calories_burned(sex, age, weight_kg, avg_hr, duration_min)
    st.success(f"Estimated Calories Burned: {calories} kcal")