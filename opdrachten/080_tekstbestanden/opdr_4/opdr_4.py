# Opdracht 4 Tekst opslaan
# Naam student:Jan Willem Sjoer
# Groep:IT2A


# Party enquete
# Vragenlijst
# Vragenlijst
vragen = [
    ("voornaam", "Wat is je voornaam?"),
    ("achternaam", "Wat is je achternaam?"),
    ("drank", "Wat neem je mee aan drank?"),
    ("eten", "Wat neem je mee om te eten?")
]

# Opslagbestand
bestand_naam = "party_gasten.txt"

# Open bestand om antwoorden op te slaan
with open(bestand_naam, "a", encoding="utf-8") as bestand:
    feestganger = {}
    for sleutel, vraag in vragen:
        antwoord = input(f"{vraag} \n")
        feestganger[sleutel] = antwoord
    
    # Opslaan in bestand
    bestand.write("---\n")
    for sleutel, waarde in feestganger.items():
        bestand.write(f"{sleutel}: {waarde}\n")
    bestand.write("\n")

print("\nBedankt voor het invullen!")
print("See you at the party.")
