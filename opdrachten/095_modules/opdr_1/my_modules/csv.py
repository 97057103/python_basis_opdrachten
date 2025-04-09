def test_csv(bestand):
    with open(bestand, "r") as file:
        regels = file.readlines() 
        return [regel.strip().split(',') for regel in regels]
    