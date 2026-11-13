import old.personne as personne

carte = {"camp": True, "foret": False, "carriere": False, "filon": False, "tourbiere": False, "epave": False}


def explorer(stock):
    p, refus = personne.choisir("explorer", "camp")
    if p is None:
        return refus
    if stock["nourriture"] < 1:
        return "refus : plus rien à manger"
    for lieu in carte:
        if carte[lieu] is False:
            carte[lieu] = True
            stock["nourriture"] -= 1
            p["fatigue"] += 1
            return f"{p['nom']} découvre {lieu}"
    return "refus : tout est déjà exploré"

def lieux():
    connus = []
    for lieu in carte:
        if carte[lieu] == True:
            connus.append(lieu)
    return "lieux connus : " + ", ".join(connus)

def deplacer(nom, lieu):
    p = personne.trouver(nom)
    if p is None:
        return f"refus : {nom} est inconnu"
    if lieu not in carte or carte[lieu] is False:
        return "refus : lieu inconnu"
    p["lieu"] = lieu
    return f"{nom} va à {lieu}"
