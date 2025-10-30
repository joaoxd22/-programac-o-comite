def celsius_para_fahrenheit(celsius):
  return (celsius * 9/5) + 32

temperatura_celsius = 25
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")
