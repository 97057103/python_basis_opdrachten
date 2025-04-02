# Opdracht 1 functies
# Naam student: Jan Willem Sjoer
# Groep: IT2A


def write_to_file(afile, atext):
    print (f"Schrijf dit maar even in een bestandje")
    # je code komt hier
    # het woordje pass hieronder kun je weghalen

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"

fo = open ('my_tekst.txt', 'wt')
fo.write(my_tekst) 
fo.close()
#fo = open ('my_tekst.txt', 'wt') maakt een tekst bestand en fo.write (my_tekst) schrijft de tekst, fo.close sluit het bestand. 
#def write_to_file maakt er een heroproepbaar iets van.
write_to_file(my_file, my_tekst)

