# 1. Définition du dictionnaire des recettes
recettes = {
    'Pizza': ['farine', 'eau', 'sel', 'levure', 'tomate', 'fromage'],
    'Salade': ['laitue', 'tomate', 'concombre', 'vinaigre', 'huile'],
    'Pates Carbonara': ['pates', 'creme', 'lardons', 'fromage', 'sel', 'poivre'],
    'Omelette': ['oeufs', 'sel', 'poivre', 'fromage'],
    'Sandwich Jambon-Beurre': ['pain', 'beurre', 'jambon']
}

# 2. Fonction pour trouver les recettes réalisables
def trouver_recettes_possibles(ingredients_disponibles):
    recettes_possibles = []
    
    # Convertir la liste d'ingrédients en minuscules pour la comparaison
    ingredients_disponibles = [ing.lower() for ing in ingredients_disponibles]
    
    # Vérifier chaque recette
    for nom_recette, ingredients_necessaires in recettes.items():
        # Vérifier si tous les ingrédients nécessaires sont disponibles
        if all(ingredient in ingredients_disponibles for ingredient in ingredients_necessaires):
            recettes_possibles.append(nom_recette)
    
    return recettes_possibles

# 3. Tests avec différents ensembles d'ingrédients
def main():
    # Test 1: Ingrédients pour pizza
    test1 = ['farine', 'eau', 'sel', 'levure', 'tomate', 'fromage']
    print("Test 1 - Ingrédients disponibles:", test1)
    print("Recettes possibles:", trouver_recettes_possibles(test1))
    print()

    # Test 2: Ingrédients variés
    test2 = ['oeufs', 'sel', 'poivre', 'fromage', 'laitue', 'tomate', 'huile']
    print("Test 2 - Ingrédients disponibles:", test2)
    print("Recettes possibles:", trouver_recettes_possibles(test2))
    print()

    # Test 3: Ingrédients pour plusieurs recettes
    test3 = ['farine', 'eau', 'sel', 'levure', 'tomate', 'fromage', 
             'oeufs', 'poivre', 'pain', 'beurre', 'jambon']
    print("Test 3 - Ingrédients disponibles:", test3)
    print("Recettes possibles:", trouver_recettes_possibles(test3))

if __name__ == "__main__":
    main()