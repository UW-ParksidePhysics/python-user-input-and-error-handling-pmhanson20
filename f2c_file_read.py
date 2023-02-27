# Ask the user for a temperature in F and read the number
# Compute the temperature in C and print out


def convert_fahrenheit_to_celsius(degrees_fahrenheit):
    return (5/9)*(degrees_fahrenheit - 32)


filename = 'temperature_data.txt'
with open(filename, 'r') as infile:
    lines = infile.readlines()

input_temperature = float(lines[2].split()[2])
print(f'The temperature read from the {filename} is {input_temperature} degrees Fahrenheit.')
output_temperature = convert_fahrenheit_to_celsius(input_temperature)
print(f'That temperature is {output_temperature} degrees Celsius')

