def convert_fahrenheit_to_celsius(degrees_fahrenheit):
    return (5/9)*(degrees_fahrenheit - 32)


data_array = open('fdeg_data.txt', 'r')
data_contents = data_array.readlines()
data_array.close()

f_values = []
for line in data_contents[2:]:
    f_values.append( float(line.split()[2]) )

c_values = [convert_fahrenheit_to_celsius(f_value) for f_value in f_values]

print("Fahrenheit  Celsius")
for f_value, c_value in zip(f_values, c_values):
    print(f"{f_value:.2f}       {c_value:.2f}")


