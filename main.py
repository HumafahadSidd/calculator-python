import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('You are seeiing this code after a delay of your given time !')

# Input for countdown time in seconds
t = input("Enter the time in seconds: ")

# Convert input to integer
t = int(t)

# Start the countdown
countdown(t)