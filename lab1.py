def fahrenheit_to_celsius():
    try:
        fahrenheit = int(input("Enter temperature in Fahrenheit: "))

        celsius = (fahrenheit - 32) * 100 / (212 - 32)

        print(f"Temperature in Celsius: {celsius:.1f}")

    except ValueError:
        print("Error: please enter an integer number.")


if __name__ == "__main__":
    fahrenheit_to_celsius()

input("Натисніть Enter, щоб завершити...")
