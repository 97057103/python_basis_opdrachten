# Opdracht 3 condities
# Naam student: Jan Willem Sjoer
# Groep:IT2A




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

age = int(input("Geef uw leeftijd in aantal jaar\n"))
for group, (min_age, max_age) in leeftijd.items():
    if min_age <= age <= max_age:
        korting = kortings_percentages[group]
        te_betalen = normale_toegangsprijs * (1 - korting / 100)
        print(f"U behoort tot de groep {group}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {te_betalen:.2f}")
        break
