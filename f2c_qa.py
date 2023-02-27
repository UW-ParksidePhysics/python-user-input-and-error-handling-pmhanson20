# Ask the user for a temperature in F and read the number
# Compute the temperature in C and print out


def convert_fahrenheit_to_celsius(degrees_fahrenheit):
    return (5/9)*(degrees_fahrenheit - 32)


input_temperature = float(input('Enter a temperature in degrees Fahrenheit: '))
output_temperature = convert_fahrenheit_to_celsius(input_temperature)
print(f'That temperature is {output_temperature} degrees Celsius')

