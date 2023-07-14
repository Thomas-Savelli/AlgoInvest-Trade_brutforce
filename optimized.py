# Solution Optimale - Programmation Dynamique
import csv


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


def calculate_best_combination(actions):
    """
    Calcule la meilleure combinaison d'actions et les résultats.
    """
    n = len(actions)  # Nombre d'actions disponibles
    dp = [[0.0] * (MAX_INVESTMENT + 1) for _ in range(n + 1)]  # Matrice pour stocker les résultats intermédiaires
    selected_actions = [[None] * (MAX_INVESTMENT + 1) for _ in range(n + 1)]  # Matrice pour stocker les actions sélectionnées

    # Parcours des actions selectionnées
    for i in range(1, n + 1):
        action = actions[i - 1]
        action_cost = action['price']
        action_profit = action['profit']

        # Parcours des investissements possibles
        for j in range(MAX_INVESTMENT + 1):
            if action_cost <= j:
                # Vérifie si l'achat de l'action actuelle est plus rentable que de ne pas l'acheter
                if dp[i - 1][j] < dp[i - 1][int(j - action_cost + 0.5)] + action_cost * (action_profit / 100):
                    dp[i][j] = dp[i - 1][int(j - action_cost + 0.5)] + action_cost * (action_profit / 100)
                    selected_actions[i][j] = action
                else:
                    dp[i][j] = dp[i - 1][j]
                    selected_actions[i][j] = selected_actions[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
                selected_actions[i][j] = selected_actions[i - 1][j]

    best_combination = reconstruct_best_combination(selected_actions, MAX_INVESTMENT, actions)
    total_investment = sum(action['price'] for action in best_combination)
    total_profit = dp[n][MAX_INVESTMENT]
    total_investment = round_decimal(total_investment)
    total_profit = round_decimal(total_profit)
    return best_combination, total_investment, total_profit


def reconstruct_best_combination(selected_actions, remaining_investment, actions):
    """
    Reconstruit la meilleure combinaison d'actions à partir de la matrice selected_actions.
    """
    best_combination = []
    selected_set = set()
    for i in range(len(actions), 0, -1):
        if selected_actions[i][int(remaining_investment)] is not None:
            action = selected_actions[i][int(remaining_investment)]
            if action['name'] not in selected_set:
                best_combination.append(action)
                selected_set.add(action['name'])
                remaining_investment -= action['price']
    return best_combination


def round_decimal(value):
    """
    Arrondit la valeur décimale à deux chiffres après la virgule.
    """
    return round(value, 2)


def print_results(best_combination, total_investment, total_profit):
    """
    Affiche la meilleure combinaison et les résultats.
    """
    print("Meilleure combinaison :")
    for action in best_combination:
        print(f"Action : {action['name']} (Investissement : {action['price']} €)")
    print(f"Investissement maximal : {MAX_INVESTMENT} €")
    print(f"Investissement total réalisé : {total_investment} €")
    print(f"Bénéfice total prévu : {total_profit} €")


def main():
    # Chargement des actions à partir du fichier csv
    actions = load_csv("dataset1.csv")
    # Appel de la fonction pour créer la liste d'actions
    # actions = create_object(data)
    # Appel de la fonction pour calculer les combinaisons d'actions ainsi que la meilleure combinaison
    best_combination, total_investment, total_profit = calculate_best_combination(actions)
    print_results(best_combination, total_investment, total_profit)


if __name__ == '__main__':
    MAX_INVESTMENT = 500
    main()
