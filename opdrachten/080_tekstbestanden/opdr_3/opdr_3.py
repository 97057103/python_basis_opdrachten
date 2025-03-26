# Opdracht 3 Tekst opslaan
# Naam student: Jan Willem Sjoer
# Groep:IT2A

def versleutel_tekst(tekst, verschuiving=5):
    versleuteld = ""
    for char in tekst:
        if char.isalpha():  # Controleer of het een letter is
            ascii_offset = ord('A') if char.isupper() else ord('a')
            nieuwe_letter = chr(((ord(char) - ascii_offset + verschuiving) % 26) + ascii_offset)
            versleuteld += nieuwe_letter
        else:
            versleuteld += char  # Niet-letters blijven hetzelfde
    return versleuteld

# Vraag om invoer van de gebruiker
tekst = input("Geef de tekst die je wilt encrypten: \n")

# Versleutel de tekst en toon het resultaat
encrypted_tekst = versleutel_tekst(tekst)
print("\nVersleutelde tekst:")
print(encrypted_tekst)


