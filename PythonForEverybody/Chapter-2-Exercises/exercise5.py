"Chapter 2: Exercise 5"


def celsius_to_fahrenheit(celsius: float | int) -> float:
    """
    celsiusToFahrenheit will take a temperature as a float and will
    return the corresponding value in Fahrenheit as a float"""

    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


temperature = input("Enter the temperature in ℃\n")
print(f"Temp in ℉ is {celsius_to_fahrenheit(float(temperature)):.2f}")
