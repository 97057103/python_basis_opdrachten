# Opdracht 2 berekeningen
# Naam student: Jan Willem Sjoer
# Groep: IT2A

# Hier komt je code...

c = 25
f = 85

def celsius_naar_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_naar_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

f_uit_c = celsius_naar_fahrenheit(c)
c_uit_f = fahrenheit_naar_celsius(f)

print(f"{c} graden Celsius is gelijk aan {f_uit_c:.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {c_uit_f:.1f} graden Celsius")




