#!/usr/bin/env python3
# Dit is de module
# In dit bestand komen alle functies.
# Je kunt de functies in een ander .py bestand gebruiken door te starten  met:
# from my_modules import csv

def sanitize(line):
  new_lst = [] 
  lst = line.split(',')
  for item in lst:
       new_lst.append(item.lower().strip())
       return new_lst

def create_person(lst):
     person = {"voornaam": "", "tussenvoegsel": "", "achternaam": ""}
     person["voornaam"] = lst[0]
     person["tussenvoegsel"] = lst[1]
     person["achternaam"] = lst[2]
     return person
def dd_fullname(person):
    # stel voor- en achternaam samen tot een volledige naam
    pass
    
def print_persons(persons, filter=["full_name"]):
    # print de van alle personen de volledige naam en het totaal aantal personen
    pass

