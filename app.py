import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.express as px

# Custom CSS for a Professional UI
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: black;
           
            margin-bottom: 10px;
        }
        .sub-title {
            text-align: center;
            font-size: 24px;
            font-weight: 500;
            color: #d4d4d4;
            margin-bottom: 40px;
        }
        .container {
            background-color: #f0f0f0;
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(255,255,255,0.1);
            text-align: center;
            width: 80%;
            margin: auto;
        }
        .feature-list {
            font-size: 20px;
            line-height: 2;
            color: #b8b8b8;
        }
       .btn-primary {
            display: inline-block;
            padding: 15px 30px;
            font-size: 20px;
            font-weight: bold;
            color: white;
            background: linear-gradient(135deg,  #3498db);
            border-radius: 10px;
            text-decoration: none;
            transition: 0.3s ease-in-out;
        }
        .btn-primary:hover {
            background: linear-gradient(135deg, #3498db, #1abc9c);
            transform: scale(1.1);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Mind Growth - Fitness & Gym Tracker</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Achieve your fitness goals with precision and motivation! 💪</div>", unsafe_allow_html=True)

# Dashboard Section
st.sidebar.title("📊 Dashboard Navigation")
menu = ["Home", "Workout Planner", "Calorie Calculator", "Progress Tracker", "Performance Analytics", "Community Challenges"]
choice = st.sidebar.radio("Go to", menu)

if choice == "Home":
    st.markdown("""
        <div class='container'>
            <h2>🚀 Welcome to Your Fitness Hub</h2>
            <p class='feature-list'>
                ✅ AI-based Workout Planning<br>
                ✅ Calorie & Macro Tracking<br>
                ✅ Progress Monitoring with Analytics<br>
                ✅ Gamified Streak & Reward System<br>
                ✅ Social Fitness Community with Challenges
            </p>
            <a href='#' class='btn-primary'>Start Now</a>
        </div>
    """, unsafe_allow_html=True)

elif choice == "Workout Planner":
    st.header("Workout Planner 🏋")
    workout_type = st.selectbox("Choose Your Workout Type", ["Full Body", "Chest", "Back", "Legs", "Arms", "Cardio"])
    exercises = st.text_area("Enter Exercises (comma separated)")
    sets_reps = st.text_area("Enter Sets & Reps (comma separated)")
    if st.button("Save Workout Plan"):
        st.success("Workout Plan Saved Successfully!")

elif choice == "Calorie Calculator":
    st.header("Calorie & Macro Calculator 🍽")
    weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, step=1)
    goal = st.selectbox("Your Goal", ["Bulking", "Cutting", "Maintenance"])
    if st.button("Calculate"):
        calories = weight * (35 if goal == "Bulking" else 25 if goal == "Cutting" else 30)
        st.success(f"Your daily calorie intake should be around {calories} kcal")

elif choice == "Progress Tracker":
    st.header("Progress Tracker 📊")
    weight_log = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, step=1)
    date_log = st.date_input("Select the date", datetime.today())
    if st.button("Save Progress"):
        st.success("Progress Saved Successfully!")
    
    # Graph
    st.subheader("Weight Progress Graph")
    df = pd.DataFrame({"Date": pd.date_range(start='2024-01-01', periods=5, freq='W'), "Weight": [70, 72, 74, 75, 77]})
    fig = px.line(df, x='Date', y='Weight', title='Weight Progress Over Time', markers=True)
    st.plotly_chart(fig)

elif choice == "Performance Analytics":
    st.header("Performance Analytics 📈")
    st.write("Analyze your workout intensity and improvements over time.")
    df = pd.DataFrame({
        "Week": [1, 2, 3, 4, 5],
        "Workouts Completed": [3, 4, 5, 4, 6],
        "Calories Burned": [1200, 1400, 1800, 1600, 2000]
    })
    fig = px.bar(df, x='Week', y=['Workouts Completed', 'Calories Burned'], barmode='group', title='Workout Performance')
    st.plotly_chart(fig)

elif choice == "Community Challenges":
    st.header("🏆 Community Challenges")
    st.write("Compete with friends and stay motivated!")
    challenges = {"Push-Up Challenge": "Complete 100 push-ups in a day", "Squat Challenge": "Do 200 squats", "Run Challenge": "Run 5km in one session"}
    for challenge, desc in challenges.items():
        st.subheader(challenge)
        st.write(desc)
        if st.button(f"Join {challenge}"):
            st.success(f"You're in for {challenge}! Crush it! 💪")