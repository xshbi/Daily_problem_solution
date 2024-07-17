def hours_to_seconds(hours):
    seconds = hours * 3600  # 1 hour = 3600 seconds
    return seconds

try:
    hours = float(input("Enter the number of hours: "))
    if hours < 0:
        print("Please enter a non-negative number of hours.")
    else:
        seconds = hours_to_seconds(hours)
        print(f'{hours} hours is equal to {seconds} seconds')
except ValueError:
    print("Invalid input. Please enter a valid number of hours.")
