# Solution classique - Algorithme par Force Brut
import itertools
import csv
from tqdm import tqdm


def load_csv(filepath):
    """
    Charge les données à partir du fichier CSV.
    """
    with open(filepath, "r", encoding="latin-1") as file:
        csv_reader = csv.reader(file, delimiter=',')

        # Ignore la premiere ligne (en tête)
        next(csv_reader)

        actions = []
        for row in csv_reader:
            actions.append({
                "name": row[0],
                "price": float(row[1]),
                "profit": float(row[2])
            })
    return actions


# Appel de la fontion de chargement des actions
liste_actions = load_csv('actions.csv')

meilleure_combinaison = None
benefice_maximum = 0
investissement_total = 0  # Initialisation en dehors de la boucle

combinaisons = []


# Générer toutes les combinaisons possibles avec itertools.combinations
# Ce qui nous permet d'éviter d'écrire manuellement un algorithme de génération de combinaison
# Les combinaisons sont stockées dans la liste [combinaisons]
for i in tqdm(range(1, len(liste_actions) + 1)):
    combinaisons += itertools.combinations(liste_actions, i)

print(f"Nombre de générations totales de combinaisons possibles : {len(combinaisons)}")

# Parcourir les combinaisons et trouver la meilleure
for combinaison in tqdm(combinaisons):
    # Initialisation des variables à 0 pour chaque nouvelle combinaison
    cout_total = 0
    benefice_total = 0

    # Vérifier si la combinaison respecte les contraintes
    for action in combinaison:
        cout = action["price"]
        benefice = action["profit"]

        # Ajout du cout au cout_total
        cout_total += cout

        # On récupére le benefice et on effectue les calculs pour obtenir le benefice total prévu
        benefice_total += cout * (benefice / 100)

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
    nom = action['name']
    cout = action['price']
    investissement = cout
    print(f"Action : {nom} (Investissement : {investissement} €)")

print(f"Investissement total : {investissement_total} €")
print(f"Bénéfice total prévu : {benefice_maximum} €")
