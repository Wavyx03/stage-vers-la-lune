import personne

stock = {"nourriture": 30, "bois": 0, "pierre": 0,
         "fer": 0, "charbon": 0, "noyau": 0, "pierre_lune": 0}

investi = {"bois": 0}

def recolter(tache, lieu, ressource, quantite):
    p, refus = personne.choisir(tache, lieu)
    if p is None:
        return refus
    if stock["nourriture"] < 1:
        return "refus : plus rien à manger"
    stock["nourriture"] -= 1
    stock[ressource] += quantite
    p["fatigue"] += 1
    return f"{p['nom']} a récolté {quantite} {ressource}"

def couper():
    return recolter("couper", "foret", "bois", 3)

def tailler():
    return recolter("tailler", "carriere", "pierre", 3)

def extraire_fer(age):
    if age != "fer":
        return "refus : il faut l'âge du fer"
    return recolter("extraire", "carriere", "fer", 2)


def extraire_charbon(age):
    if age != "vapeur":
        return "refus : il faut l'âge de la vapeur"
    return recolter("extraire", "tourbiere", "charbon", 2)

def feu_de_bois():
    if stock["bois"] < 2 or stock["pierre"] < 1:
        return "refus : il faut 2 bois et 1 pierre"
    stock["bois"] -= 2
    stock["pierre"] -= 1
    return "feu de bois allumé"

def resume():
    bois = stock["bois"] + investi["bois"]
    fer = stock["fer"] + 2 * stock["noyau"]
    charbon = stock["charbon"] + stock["noyau"]
    return (f"nourriture {stock['nourriture']}, bois {stock['bois']}, pierre {stock['pierre']}, fer {stock['fer']}, charbon {stock['charbon']}, noyau {stock['noyau']}, pierre_lune {stock['pierre_lune']} | "
            f"bilan : bois {bois}, fer {fer}, charbon {charbon}")
