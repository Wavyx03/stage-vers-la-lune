gens = [
    {"nom": "ada", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False},
    {"nom": "bo", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False},
    {"nom": "abdoul", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False}
]


def trouver(nom):
    for p in gens:
        if p["nom"] == nom:
            return p
    return None


def equipe():
    lignes = []
    for p in gens:
        ligne = f"{p['nom']} ({p['lieu']}, {p['tache']}, fatigue {p['fatigue']}"
        if p["embarque"]:
            ligne += ", embarqué"
        lignes.append(ligne + ")")
    return "équipe : " + ", ".join(lignes)


def recruter(stock, nom, places):
    if trouver(nom) is not None:
        return f"refus : {nom} est déjà là"
    if len(gens) >= places:
        return "refus : plus de place"
    if stock["nourriture"] < 2:
        return "refus : plus rien à manger"
    stock["nourriture"] -= 2
    gens.append({"nom": nom, "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False})
    return f"{nom} rejoint le camp"


def affecter(nom, tache):
    p = trouver(nom)
    if p is None:
        return f"refus : {nom} est inconnu"
    if tache not in ["couper", "tailler", "extraire", "explorer"]:
        return "refus : tâche inconnu"
    p["tache"] = tache
    return f"{nom} va {tache}"


def liberer(nom):
    p = trouver(nom)
    if p is None:
        return f"refus : {nom} est inconnu"
    p["tache"] = "libre"
    return f"{nom} est libre"


def reposer(stock, nom):
    p = trouver(nom)
    if p is None:
        return f"refus : {nom} est inconnu"
    if stock["nourriture"] < 1:
        return "refus : plus rien à manger"
    stock["nourriture"] -= 1
    p["fatigue"] = 0
    return f"{nom} est reposé"


def choisir(tache, lieu):
    refus = f"refus : personne pour {tache}"
    for p in gens:
        if p["tache"] != tache:
            continue
        if p["lieu"] != lieu:
            refus = f"refus : {p['nom']} doit être à {lieu}"
        elif p["fatigue"] >= 3:
            refus = f"refus : {p['nom']} est épuisé"
        else:
            return p, ""
    return None, refus
