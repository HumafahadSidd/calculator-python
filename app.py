import streamlit as st
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        st.write(timer)
        time.sleep(1)
        t -= 1
    st.write('You are seeing this message after the delay of your given time!')

# Input for countdown time in seconds
t = st.number_input("Enter the time in seconds:", min_value=1, value=10, step=1)

if st.button("Start Countdown"):
    countdown(int(t))