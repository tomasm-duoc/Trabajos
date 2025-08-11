# Ejercicio 7

def fahrenheit(celsius):
    fahrenheit = ((9/5)*celsius)+32
    return fahrenheit

celsius = float(input("Ingrese un valor de grados Celsius: "))
temp_fahren = fahrenheit(celsius)

print(f"{celsius}°C son {round(temp_fahren,2)}°F")