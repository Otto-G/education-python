def celsiusToFahrenheit(celsius:float | int):
    """
    celsiusToFahrenheit will take a temperature as a float and will
    return the corresponding value in Fahrenheit as a float"""

    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

temperature = input("Enter the temperature in ℃\n")
print("Temp in ℉ is {:.2f}".format(celsiusToFahrenheit(float(temperature))))