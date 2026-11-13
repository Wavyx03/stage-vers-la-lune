import ages
import carte
import partie
import personne
import ressources
import vaisseau

def jouer():
    while True:
        # On lit la ligne tapée, en minuscules et sans espaces autour
        ligne = input("> ").strip().lower()
        # On coupe la ligne en mots : "affecter ada couper" -> ["affecter", "ada", "couper"]
        mots = ligne.split()
        # Ligne vide : on recommence
        if len(mots) == 0:
            continue
        mot = mots[0]   # le premier mot = la commande
        nb = len(mots)  # le nombre de mots (pour vérifier qu'il ne manque rien)

        if ligne == "quitter":
            print("à bientôt")
            break

        # Personnes
        if ligne == "equipe":
            print(personne.equipe())
        elif mot == "recruter" and nb == 2:
            print(personne.recruter(ressources.stock, mots[1], ages.palces()))
        elif mot == "affecter" and nb == 3:
            print(personne.affecter(mots[1], mots[2]))
        elif mot == "liberer" and nb == 2:
            print(personne.liberer(mots[1]))
        elif mot == "reposer" and nb == 2:
            print(personne.reposer(ressources.stock, mots[1]))
        elif mot == "embarquer" and nb == 2:
            print(vaisseau.embarquer(mots[1]))

        # Terrain
        elif ligne == "explorer":
            print(carte.explorer(ressources.stock))
        elif ligne == "lieux":
            print(carte.lieux())
        elif mot == "deplacer" and nb == 3:
            print(carte.deplacer(mots[1], mots[2]))
        elif ligne == "couper":
            print(ressources.couper())
        elif ligne == "tailler":
            print(ressources.tailler())
        elif ligne == "extraire fer":
            print(ressources.extraire_fer(ages.etat["age"]))
        elif ligne == "extraire charbon":
            print(ressources.extraire_charbon(ages.etat["age"]))
        elif ligne == "stock":
            print(ressources.resume())
        elif ligne == "aide":
            print("Commandes disponibles :")
            print("  equipe : affiche l'équipe")
            print("  recruter <nom> : recrute une personne")
            print("  affecter <nom> <lieu> : affecte une personne à un lieu")
            print("  liberer <nom> : libère une personne")
            print("  reposer <nom> : fait reposer une personne")
            print("  embarquer <nom> : embarque une personne")
            print("  explorer : explore la carte")
            print("  lieux : affiche les lieux")
            print("  deplacer <nom> <lieu> : déplace une personne")
            print("  couper : récolte du bois")
            print("  tailler : récolte de la pierre")
            print("  extraire fer : récolte du fer")
            print("  extraire charbon : récolte du charbon")
            print("  stock : affiche le stock")
            print("  construire <batiment> : construit un bâtiment")
            print("  avancer : avance dans le temps")
            print("  produire : produit un noyau")
            print("  lancer : lance le vaisseau")
            print("  sauver : sauve la partie")
            print("  charger : charge la partie")
            print("  reinitialiser : remet la partie à zéro")
            print("  etat : affiche l'état de l'âge")
            print("  aide ages : affiche l'aide sur les âges")

        # Camp
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
        elif ligne in ["reinitialiser", "reset"]:
            print(partie.reinitialiser())
        elif ligne in ["etat", "resume"]:
            print(ages.resume())
        elif ligne in ["aide ages", "aide_age", "aide-ages"]:
            print(ages.aide())

        # secret
        elif ligne == "tomy":
            print("Devloppeur : Tomy")
        elif ligne == "mathieu":
            print("Devloppeur : Mathieu")

        # Tout le reste
        else:
            print("refus : commande inconnue")


jouer()
