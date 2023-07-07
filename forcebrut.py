import json
import itertools


def load_json():
    """ Permet de récupérer et charger les données de actions.json """
    # Premiere étape -> Charger le contenu de actions.json
    with open('actions.json', 'r') as file:
        contenu_json = file.read()

    # Deuxieme étape -> Parser le contenu de actions.json
    donnees_actions = json.loads(contenu_json)

    # Troisieme étape -> Accéder aux données des actions
    actions = donnees_actions["actions"]

    # Quatrieme étape -> Stocker les données dans une liste d'objet pour chaque action
    liste_actions = []
    for action in actions:
        nom = action["Action #"]
        cout = action["Cout par action (en euros)"]
        benefice = action["Benefice (apres 2 ans)"]

        # Création d'un objet représentant l'action
        objet_action = {
            "nom": nom,
            "cout": cout,
            "benefice": benefice
        }

        liste_actions.append(objet_action)

    # # Vérification et affichage des données des actions
    # for action in liste_actions:
    #     print(f"Nom : {action['nom']}")
    #     print(f"Coût : {action['cout']} euros")
    #     print(f"Bénéfice : {action['benefice']}")
    #     print("------------------------")

    return liste_actions


# Appel de la fontion de chargement des actions
liste_actions = load_json()

meilleure_combinaison = None
benefice_maximum = 0
investissement_total = 0  # Initialisation en dehors de la boucle

combinaisons = []


# Générer toutes les combinaisons possibles avec itertools.combinations
# Ce qui nous permet d'éviter d'écrire manuellement un algorithme de génération de combinaison
# Les combinaisons sont stockées dans la liste [combinaisons]
for i in range(1, len(liste_actions) + 1):
    combinaisons += itertools.combinations(liste_actions, i)

print(f"Nombre de générations totales de combinaisons possibles : {len(combinaisons)}")

# Parcourir les combinaisons et trouver la meilleure
for combinaison in combinaisons:
    # Initialisation des variables à 0 pour chaque nouvelle combinaison
    cout_total = 0
    benefice_total = 0

    # Vérifier si la combinaison respecte les contraintes
    for action in combinaison:
        cout = action["cout"]
        benefice = action["benefice"]

        # Ajout du cout au cout_total
        cout_total += int(cout)

        # On récupére le benefice et on effectue les calculs pour obtenir le benefice total prévu
        benefice_total += int(cout) * (float(benefice.strip('%')) / 100)

    if cout_total <= 500 and benefice_total > benefice_maximum:
        benefice_maximum = benefice_total
        meilleure_combinaison = combinaison
        investissement_total = cout_total

# Afficher la meilleure combinaison et les résultats
print("")
print("------------------------------")
print("")
print("Meilleure combinaison :")
for action in meilleure_combinaison:
    nom = action['nom']
    cout = action['cout']
    investissement = int(cout)
    print(f"Action : {nom} (Investissement : {investissement} €)")

print(f"Investissement total : {investissement_total} €")
print(f"Bénéfice total prévu : {benefice_maximum} €")
