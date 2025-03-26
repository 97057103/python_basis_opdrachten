# Opdracht 2 lists
# Naam student: Jan Willem Sjoer
# Groep:IT2A


rivier_info = {
   "rijn":  [ "nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

rivier_info = { 
    "rijn": ["nederland", "duitsland", "frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

rivieren = list(rivier_info.keys())

# 1e rivier en het 2e land van die rivier
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")

# 2e rivier en het 1e land van die rivier
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[1]][0].capitalize()}")

# 3e rivier en het 3e land van die rivier
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[2]][2].capitalize()}")
