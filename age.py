from datetime import datetime

# Function to calculate age from birthdate
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year

    # Adjust age if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

# Ask user for their birthday
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert the input string to a datetime object
try:
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    # Calculate and print the age
    age = calculate_age(birthdate)
    print(f"Your age is: {age} years")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
