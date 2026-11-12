import carte
import ressources

etat = {"age": "pierre"}

batiments = []

def palces():
    if "dortoir" in batiments:
        return 8
    return 4

def construire(nom):
    stock = ressources.stock
    if nom not in ["camp", "dortoir", "forge", "mine", "reacteur", "vaisseau"]:
        return f"refus : on ne construit pas {nom}"
    if nom in batiments:
        return f"refus : {nom} est déjà construit"
    if nom in ["camp", "dortoir", "forge"]:
        if stock["bois"] < 3 or stock["pierre"] < 3:
            return "refus : il faut 3 bois et 3 pierres"
        stock["bois"] -= 3
        stock["pierre"] -= 3
        ressources.investi["bois"] += 3
    elif nom == "mine":
        if stock["fer"] < 2:
            return "refus : il faut 2 fer"
        stock["fer"] -= 2
    elif nom == "reacteur":
        if stock["charbon"] < 2:
            return "refus : il faut 2 charbon"
        stock["charbon"] -= 2
    elif nom == "vaisseau":
        if carte.carte["epave"] == False:
            return "refus : l'épave est inconnue"
        batiments.append(nom)
        return f"construit : {nom}"
    batiments.append(nom)
    return f"construit : {nom}"


def avancer():
    if etat["age"] == "pierre" and "forge" in batiments:
        etat["age"] = "fer"
    elif etat["age"] == "fer" and "mine" in batiments:
        etat["age"] = "vapeur"
    elif etat["age"] == "vapeur" and "reacteur" in batiments:
        etat["age"] = "reacteur"
    else:
        return "refus : on ne peut pas avancer"
    return f"âge : {etat['age']}"

