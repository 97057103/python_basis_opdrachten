# Opdracht 1 modules
# Naam student:Jan Willem Sjoer
# Groep:IT2A

# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

from my_modules import csv

for line in open("D://Deltion/Python Opdrachten/python_basis_opdrachten/opdrachten/095_modules/opdr_2/test.txt"):  
    print(csv.sanitize(line))
    print(line)


