# countdown.py
from datetime import datetime

def countdown_to_october_2024():
    # Target date: October 1, 2024
    target_date = datetime(2024, 10, 1)

    # Get the current time
    now = datetime.now()

    # Calculate the difference
    time_left = target_date - now

    # Extract days, hours, minutes, and seconds
    days, seconds = time_left.days, time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    # Print the countdown
    print(f"Time left until October 1, 2024: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

if __name__ == "__main__":
    countdown_to_october_2024()
