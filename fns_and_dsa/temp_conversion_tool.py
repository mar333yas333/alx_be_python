# temp_conversion_tool.py

# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # Must explicitly use + 32
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # Must explicitly use - 32
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


if __name__ == "__main__":
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = input("Choose conversion (1/2): ")

        if choice == "1":
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
        elif choice == "2":
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")
