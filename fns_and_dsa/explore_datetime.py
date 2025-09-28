from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date(days_to_add):
    """
    Calculate the future date after adding a number of days to the current date.

    Parameters:
        days_to_add (int): Number of days to add

    Returns:
        str: The future date in YYYY-MM-DD format
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Ask user for days to add and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        result = calculate_future_date(days)
        print("Future date:", result)
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
