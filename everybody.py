import countdown
print("ilia: hi everybody")
print("oshri: hi ilia")
print("Yoni: This is confusing.....")
print("Elad: wake UP!")
print("Hi im Dugibeat")
# DugibeatCountdown

# Ask the user if they want to see the countdown
response = input("Do you want to see the countdown to October 1, 2024? (yes/no): ").strip().lower()

# Check the user's response
if response == 'yes':
    # Call the countdown function
    countdown.countdown_to_october_2024()
else:
    print("Countdown not displayed.")