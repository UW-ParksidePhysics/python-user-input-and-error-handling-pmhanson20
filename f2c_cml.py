from sys import argv


def convert_fahrenheit_to_celsius(degrees_fahrenheit):
    return (5/9)*(degrees_fahrenheit - 32)


input_temperature = float(argv[1])
print(f'The temperature read from the command line is {input_temperature} degrees Fahrenheit.')
output_temperature = convert_fahrenheit_to_celsius(input_temperature)
print(f'That temperature is {output_temperature} degrees Celsius')

