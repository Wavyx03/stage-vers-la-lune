import json

import old.ages as ages
import old.carte as carte
import old.personne as personne
import old.ressources as ressources

def sauver():
    donnees = {
        "gens": personne.gens,
        "stock": ressources.stock,
        "investi": ressources.investi,
        "carte": carte.carte,
        "age": ages.etat["age"],
        "batiments": ages.batiments,
    }
    fichier = open("sauvegarde.json", "w")
    json.dump(donnees, fichier)
    fichier.close()
    return "partie sauvée"

def charger():
    try:
        fichier = open("sauvegarde.json")
    except FileNotFoundError:
        return "refus : aucune sauvegarde"
    donnees = json.load(fichier)
    fichier.close()
    personne.gens.clear()
    personne.gens.extend(donnees["gens"])
    ressources.stock.update(donnees["stock"])
    ressources.investi.update(donnees["investi"])
    carte.carte.update(donnees["carte"])
    ages.etat["age"] = donnees["age"]
    ages.batiments.clear()
    ages.batiments.extend(donnees["batiments"])
    return "partie chargée"


def reinitialiser():
    personne.gens.clear()
    personne.gens.extend([
        {"nom": "ada", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False},
        {"nom": "bo", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False},
        {"nom": "abdoul", "lieu": "camp", "tache": "libre", "fatigue": 0, "embarque": False},
    ])

    ressources.stock.clear()
    ressources.stock.update({
        "nourriture": 30,
        "bois": 0,
        "pierre": 0,
        "fer": 0,
        "charbon": 0,
        "noyau": 0,
        "pierre_lune": 0,
    })

    ressources.investi.clear()
    ressources.investi.update({"bois": 0})

    carte.carte.clear()
    carte.carte.update({
        "camp": True,
        "foret": False,
        "carriere": False,
        "filon": False,
        "tourbiere": False,
        "epave": False,
    })

    ages.etat["age"] = "pierre"
    ages.batiments.clear()
    return "partie réinitialisée"
