% 1. Définition des recettes et leurs ingrédients
recette(pizza).
recette(salade).
recette(pates_carbonara).
recette(omelette).
recette(sandwich_jambon_beurre).

% Ingrédients pour chaque recette
ingredients(pizza, [farine, eau, sel, levure, tomate, fromage]).
ingredients(salade, [laitue, tomate, concombre, vinaigre, huile]).
ingredients(pates_carbonara, [pates, creme, lardons, fromage, sel, poivre]).
ingredients(omelette, [oeufs, sel, poivre, fromage]).
ingredients(sandwich_jambon_beurre, [pain, beurre, jambon]).

% 2. Règle pour vérifier si tous les ingrédients nécessaires sont disponibles
tous_ingredients_disponibles(Recette, IngredientsDisponibles) :-
    ingredients(Recette, IngredientsNecessaires),
    forall(member(Ingredient, IngredientsNecessaires),
           member(Ingredient, IngredientsDisponibles)).

% Règle pour trouver les recettes possibles
recettes_possibles(IngredientsDisponibles, RecettesPossibles) :-
    findall(Recette,
            (recette(Recette),
             tous_ingredients_disponibles(Recette, IngredientsDisponibles)),
            RecettesPossibles).
