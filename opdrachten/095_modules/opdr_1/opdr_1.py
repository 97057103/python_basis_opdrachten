# Opdracht 1 functies
# Naam student: Jan Willem Sjoer
# Groep:IT2A

# importeer de module csv...


from my_modules import csv

def main():
    data = csv.test_csv("voorbeeld.csv")
    for rij in data:
        print(rij)


if __name__ == "__main__":
    main()