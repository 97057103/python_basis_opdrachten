# Opdracht 4 Tekst opslaan
# Naam student:Jan Willem Sjoer
# Groep:IT2A


# Party enquete
# Vragenlijst
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Opslagbestand
bestand_naam = "party_gasten.txt"

# Open bestand om antwoorden op te slaan
with open(bestand_naam, "a", encoding="utf-8") as bestand:
    feestganger = {}
    for i, vraag in enumerate(vragen, start=1):
        antwoord = input(f"{i}. {vraag} \n")
        sleutel = vraag.split()[2].lower()  # Pak het sleutelwoord (voornaam, achternaam, etc.)
        feestganger[sleutel] = antwoord
    
    # Opslaan in bestand
    bestand.write("---\n")
    for sleutel, waarde in feestganger.items():
        bestand.write(f"{sleutel}: {waarde}\n")
    bestand.write("\n")

print("\nBedankt voor het invullen!")
print("See you at the party.")