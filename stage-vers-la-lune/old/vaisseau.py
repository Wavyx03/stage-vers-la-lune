import old.ages as ages
import old.personne as personne
import old.ressources as ressources

def produire():
    stock = ressources.stock
    if stock["nourriture"] < 1:
        return "refus : plus rien à manger"
    if stock["fer"] < 2 or stock["charbon"] < 1:
        return "refus : il faut 2 fer et 1 charbon"
    for p in personne.gens:
        if p["fatigue"] < 3:
            stock["fer"] -= 2
            stock["charbon"] -= 1
            stock["noyau"] += 1
            stock["nourriture"] -= 1
            p["fatigue"] += 1
            return f"{p['nom']} produit un noyau"
    return f"refus : {personne.gens[0]['nom']} est épuisé"

def embarquer(nom):
    p = personne.trouver(nom)
    if p is None:
        return f"refus : {nom} est inconnu"
    if p["embarque"] == True:
        return f"refus : {nom} est déjà embarqué"
    p["embarque"] = True
    return f"{nom} embarque"

def lancer():
    equipage = 0
    for p in personne.gens:
        if p["embarque"] == True:
            equipage += 1
    if equipage < 2 or "vaisseau" not in ages.batiments:
        return "refus : l'équipage est incomplet"
    if ressources.stock["nourriture"] < 2:
        return "refus : l'équipage n'a plus à manger"
    ressources.stock["pierre_lune"] += 1
    return "le vaisseau part pour la Lune et ramène une pierre de lune"
