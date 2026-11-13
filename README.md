# Stage vers la lune

Jeu textuel en Python dont l'objectif est de gérer une petite colonie qui progresse dans les âges technologiques jusqu'à pouvoir envoyer un vaisseau vers la Lune.

## Vue d'ensemble

Le projet simule une gestion de ressources et de population dans un terminal. Le joueur doit :

- recruter des personnes,
- leur affecter des tâches,
- explorer le terrain,
- récolter les ressources,
- construire des bâtiments,
- faire progresser la civilisation par âges,
- produire un noyau et lancer un vaisseau.

Les données du jeu sont sauvegardées au format JSON dans un fichier `sauvegarde.json`.

## Prérequis

- Python 3
- Aucun package externe requis

## Lancer le jeu

Depuis le dossier du projet :

```bash
python jeu.py
```

## Commandes principales

Le jeu attend des commandes saisies dans le terminal. Voici quelques exemples :

- `equipe` : affiche les membres de l'équipe
- `recruter Ada` : recrute une personne
- `explorer` : explore un lieu non découvert
- `lieux` : liste les zones déjà découvertes
- `deplacer Ada foret` : déplace un personnage vers un lieu connu
- `couper` : récolte du bois
- `tailler` : récolte de la pierre
- `extraire fer` : extrait du fer à l'âge du fer
- `extraire charbon` : extrait du charbon à l'âge de la vapeur
- `stock` : affiche les ressources disponibles
- `construire camp` : construit un bâtiment
- `avancer` : fait progresser l'âge technologique
- `produire` : crée un noyau
- `lancer` : envoie un vaisseau vers la Lune
- `sauver` : sauvegarde la partie
- `charger` : recharge la dernière sauvegarde
- `quitter` : termine le jeu

## Structure du projet

- `ages.py` : gestion des âges technologiques et construction des bâtiments
- `carte.py` : exploration et déplacement sur la carte
- `jeu.py` : boucle principale du jeu et traitement des commandes
- `partie.py` : sauvegarde et chargement de la partie
- `personne.py` : gestion de l'équipe et des tâches
- `ressources.py` : ressources, récolte et production
- `vaisseau.py` : production du noyau et lancement du vaisseau

## Mécanique de jeu

Le but n'est pas seulement de récolter des ressources, mais de progresser dans la civilisation :

1. on commence au stade de la pierre ;
2. le fait de construire une forge permet d'accéder à l'âge du fer ;
3. la mine permet d'aller vers l'âge de la vapeur ;
4. le réacteur permet d'atteindre l'âge du réacteur ;
5. ensuite, il faut produire un noyau et lancer le vaisseau pour obtenir une pierre de lune.

## Sauvegarde

La partie est enregistrée dans le fichier `sauvegarde.json` avec les éléments suivants :

- les personnages,
- les ressources,
- les bâtiments construits,
- la carte explorée,
- l'âge actuel de la civilisation.

## Objectif final

Le but du projet est de créer un mini jeu de gestion/aventure en mode texte, inspiré des jeux de civilisation, entièrement codé en Python et jouable directement dans le terminal.
