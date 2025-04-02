# Opdracht 1 functies
# Naam student: Jan Willem Sjoer
# Groep:IT2A

def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
      
        volledige_naam = " ".join(filter(None, [naam["voornaam"], naam["tussenvoegsel"], naam["achternaam"]]))
        print(volledige_naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)