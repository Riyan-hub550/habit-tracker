import streamlit as st
import datetime
import pandas as pd

# Initialize a session state for habit data
if 'habit_data' not in st.session_state:
    st.session_state.habit_data = {}

# Display app title
st.title("Habit Tracker")

# Input habit name
habit_name = st.text_input("Enter the habit you want to track:", "")

# Get today's date
today = datetime.date.today()

# Function to track habit completion
def track_habit():
    if habit_name != "":
        if habit_name not in st.session_state.habit_data:
            st.session_state.habit_data[habit_name] = []
        
        # Check if the user completed the habit today
        completed_today = today in st.session_state.habit_data[habit_name]
        
        if completed_today:
            st.warning(f"You've already marked this habit as completed today.")
        else:
            if st.button("Mark as Completed Today"):
                st.session_state.habit_data[habit_name].append(today)
                st.success(f"Great job! You've completed {habit_name} today.")

# Function to show streak
def show_streak():
    if habit_name in st.session_state.habit_data:
        habit_dates = st.session_state.habit_data[habit_name]
        streak = 0
        for i in range(len(habit_dates) - 1, 0, -1):
            if habit_dates[i] == habit_dates[i - 1] + datetime.timedelta(days=1):
                streak += 1
            else:
                break
        st.write(f"Your current streak for {habit_name} is: {streak + 1} day(s)")
    else:
        st.write("No streak data available yet. Start tracking your habit!")

# Show habit tracking options and streak
track_habit()
show_streak()

# Display habit history
st.write("### Habit Completion History")
if habit_name in st.session_state.habit_data:
    df = pd.DataFrame(st.session_state.habit_data[habit_name], columns=["Date"])
    df['Day of Week'] = df['Date'].apply(lambda x: x.strftime("%A"))
    st.write(df)