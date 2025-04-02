# Opdracht 1 functies
# Naam student: Jan Willem Sjoer
# Groep:IT2A


def kilometers_naar_miles(km):
    return km / 1.609344

def miles_naar_kilometers(miles):
    return miles * 1.609344

kilometers = 1223
miles = 867

miles_converted = kilometers_naar_miles(kilometers)
km_converted = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_converted} miles")
print(f"{miles} miles = {km_converted} kilometers")