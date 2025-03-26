# Opdracht 3 tekstfuncties
# Naam student: Jan Willem Sjoer
# Groep:IT2A

# Hier komt je code...

tree_lines = [
    "    *        ", 
    "   ***       ", 
    "  ******     ", 
    " ********    ", 
    "***********  ", 
    "    ***      ", 
    "    ***      ", 
    "    ***      "
]
for line in tree_lines:
   print("   ".join([line] * 5))