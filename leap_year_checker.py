# Leap Year Checker

def check_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print("=" * 40)
print("         LEAP YEAR CHECKER")
print("=" * 40)

while True:
    try:
        year = int(input("\nEnter a year (or 0 to exit): "))

        if year == 0:
            print("Thank you for using Leap Year Checker!")
            break

        if year < 1:
            print("Please enter a valid year.")
            continue

        if check_leap_year(year):
            print(year, "is a Leap Year!")
            print("Number of days: 366")
        else:
            print(year, "is not a Leap Year.")
            print("Number of days: 365")

    except ValueError:
        print("Invalid input! Please enter a whole number.")