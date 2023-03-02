#4.4 HW this is not right

fahrenheit_temp = eval(input('input temperature in fahrenheit:'))

from f2c_qa import convert_fahrenheit_to_celsius


data_array = open('Fdeg.data.txt', 'r')
data_contents = data_array.readlines()
data_array.close()

f_value = float(data_contents[7].split()[2])

print(f'{convert_fahrenheit_to_celsius(f_value)}')


