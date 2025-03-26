# Opdracht 3 input functie
# Naam student: Jan Willem Sjoer
# Groep:IT2A

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

pizzas.sort()
print(pizzas)

pizzas.append('Shoarma')
print(pizzas)

pizzas.remove('olivio')
print(pizzas)

print(pizzas[:3])

print(pizzas[len(pizzas)//2:len(pizzas)//2 + 1])

print(pizzas[-3:])