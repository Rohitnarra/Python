kelvin = [22, 54, 73, 82]
celsius = []
farenheit = []

for temperature in kelvin:
    temperature_in_Celsius = temperature - 273.15
    temperature_in_farenheit = 1.8*(temperature-273)+32
    #print(temperature_in_Celsius)
    celsius.append(temperature_in_Celsius)
    farenheit.append(temperature_in_farenheit)

print(f"List of temperature in celsius {celsius}")
print(f"List of temperature in farenheit {farenheit}")

"""first we given the values for kelvin
then given empty list to celsius and farenheit
then used 'Fur loop' to the kelvin list and gave the formulas for converting kelvin to celsius and farenheit
then appended values for the empty list in celsius and farenheit
printed the results """