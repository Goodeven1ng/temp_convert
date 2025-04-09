#temp_convert.py

# Prompt the user to input a Celsius temperature
celsius = input("Please enter a Celsius temperature: ")

# Cast the input to a float and store it in a variable
celsius = float(celsius)

# Calculate the Fahrenheit temperature using the formula
fahrenheit = (9/5) * celsius + 32

# Print the converted Fahrenheit temperature
print(f"Temperature in fahrenheit: {fahrenheit}")