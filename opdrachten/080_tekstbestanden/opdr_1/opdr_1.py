# Opdracht 1 while-loops
# Naam student: Jan Willem Sjoer
# Groep:IT2A

# Jouw code komt hier

vragen_antwoorden = {
    "Wat vind je van de huidige regering?": "Kan beter",
    "Wat vind je van de Python-lessen tot nu toe?": "Erg lastig",
    "Wat vind jij de mooiste stad van Nederland?": "Nunspeet!"
}

# Open een bestand om de antwoorden op te slaan
with open("enquete_resultaten.txt", "w", encoding="utf-8") as bestand:
    for vraag, antwoord in vragen_antwoorden.items():
        print(vraag)  # Print de vraag
        input("(Druk op Enter voor het antwoord...) ")  # Wacht op input van de gebruiker
        print(f"Antwoord: {antwoord}\n")  # Toon het antwoord
        bestand.write(f"{vraag} {antwoord}\n")  # Sla op in het bestand

print("De enquête is voltooid.'")