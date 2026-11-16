personnes = [
    {"nom": "ada", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False},
    {"nom": "bo", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False}
]

for personne in personnes:
    personne["lieu"] = "camp"
    personne["tache"] = "libre"
    personne["fatigue"] = 0
    personne["embarque"] = False

print("Personnes initialisées :")
for personne in personnes:
    print(f"{personne['nom']} ({personne['lieu']}, {personne['tache']}, fatigue {personne['fatigue']})")
