from typing import List, Dict, Tuple
from functools import partial

# 1. Définition du dictionnaire des recettes
recettes: Dict[str, List[str]] = {
    'Pizza': ['farine', 'eau', 'sel', 'levure', 'tomate', 'fromage'],
    'Salade': ['laitue', 'tomate', 'concombre', 'vinaigre', 'huile'],
    'Pates Carbonara': ['pates', 'creme', 'lardons', 'fromage', 'sel', 'poivre'],
    'Omelette': ['oeufs', 'sel', 'poivre', 'fromage'],
    'Sandwich Jambon-Beurre': ['pain', 'beurre', 'jambon']
}

# 2. Fonctions fonctionnelles pour le traitement des recettes
def verifier_ingredients(ingredients_requis: List[str], ingredients_dispo: List[str]) -> bool:
    """Vérifie si tous les ingrédients requis sont disponibles"""
    return all(map(lambda x: x in ingredients_dispo, ingredients_requis))

def formater_recette(recette_tuple: Tuple[str, List[str]]) -> dict:
    """Formate une recette en dictionnaire avec nom et ingrédients"""
    nom, ingredients = recette_tuple
    return {'nom': nom, 'ingredients': ingredients}

def trouver_recettes_possibles(ingredients: List[str]) -> List[dict]:
    """Trouve toutes les recettes possibles avec les ingrédients donnés"""
    # Convertir les ingrédients en minuscules
    ingredients_dispo = list(map(str.lower, ingredients))
    
    # Filtrer les recettes possibles
    recettes_possibles = filter(
        lambda x: verifier_ingredients(x[1], ingredients_dispo),
        recettes.items()
    )
    
    # Formater les résultats
    return list(map(formater_recette, recettes_possibles))

# 3. Tests avec différentes listes d'ingrédients
def afficher_resultats(ingredients: List[str]) -> None:
    """Affiche les résultats pour une liste d'ingrédients donnée"""
    print(f"Ingrédients disponibles: {ingredients}")
    resultats = trouver_recettes_possibles(ingredients)
    print("Recettes possibles:")
    for recette in resultats:
        print(f"- {recette['nom']} (nécessite: {', '.join(recette['ingredients'])})")
    print()

def main():
    # Test 1: Ingrédients pour pizza
    test1 = ['farine', 'eau', 'sel', 'levure', 'tomate', 'fromage']
    afficher_resultats(test1)

    # Test 2: Ingrédients variés
    test2 = ['oeufs', 'sel', 'poivre', 'fromage', 'laitue', 'tomate', 'huile']
    afficher_resultats(test2)

    # Test 3: Ingrédients pour plusieurs recettes
    test3 = ['farine', 'eau', 'sel', 'levure', 'tomate', 'fromage', 
             'oeufs', 'poivre', 'pain', 'beurre', 'jambon']
    afficher_resultats(test3)

if __name__ == "__main__":
    main()