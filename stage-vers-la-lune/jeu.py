import ages
import carte
import partie
import personne
import ressources
import vaisseau

def jouer():
    while True:
        ligne = input("> ").strip().lower()
        mots = ligne.split()
        if len(mots) == 0:
            continue
        mot = mots[0]
        nb = len(mots)
        if ligne == "quitter":
            print("à bientôt")
            break
        if ligne == "equipe":
            print(personne.equipe())
        elif mot == "recruter" and nb == 2:
            print(personne.recruter(ressources.stock, mots[1], ages.palces()))
        elif mot == "affecter" and nb == 3:
            print(personne.affecter(mots[1], mots[2]))
        elif mot == "libérer" and nb == 2:
            print(personne.liberer(mots[1]))
        elif mot == "reposer" and nb == 2:
            print(personne.reposer(ressources.stock, mots[1]))
        elif mot == "embarquer" and nb == 2:
            print(vaisseau.embarquer(mots[1]))
        elif ligne == "explorer":
            print(carte.explorer(ressources.stock))
        elif ligne == "lieux":
            print(carte.lieux())
        elif mot == "deplacer" and nb == 3:
            print(carte.deplacer(mots[1], mots[2]))
        elif mot == "couper":
            print(ressources.couper())
        elif ligne == "tailler":
            print(ressources.tailler())
        elif ligne == "feu de bois":
            print(ressources.feu_de_bois())
        elif ligne == "extraire fer":
            print(ressources.extraire_fer(ages.etat["age"]))
        elif ligne == "extraire charbon":
            print(ressources.extraire_charbon(ages.etat["age"]))
        elif ligne == "stock":
            print(ressources.resume())
        elif mot == "construire" and nb == 2:
            print(ages.construire(mots[1]))
        elif ligne == "avancer":
            print(ages.avancer())
        elif ligne == "produire":
            print(vaisseau.produire())
        elif ligne == "lancer":
            print(vaisseau.lancer())
        elif ligne == "sauver":
            print(partie.sauver())
        elif ligne == "charger":
            print(partie.charger())
        else:
            print("refus : commande inconnue")

jouer()