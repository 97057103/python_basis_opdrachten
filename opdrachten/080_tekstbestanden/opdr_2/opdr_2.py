# Opdracht 2 tekstbestanden
# Naam student: Jan Willem Sjoer
# Groep: IT2A

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

import random

prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

aantal_pogingen = 0

while True:
    try:
        gok = int(input(prompt))
        aantal_pogingen += 1
        
        if gok < geheim_getal:
            print("Hoger")
        elif gok > geheim_getal:
            print("Lager")
        else:
            print(f"Je hebt het getal geraden! Het is {geheim_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer gedaan.")
            break
    except ValueError:
        print("Voer een geldig getal in tussen 1 en 100.")
