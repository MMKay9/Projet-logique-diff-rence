% 1. D�finition des recettes et leurs ingr�dients
recette(pizza).
recette(salade).
recette(pates_carbonara).
recette(omelette).
recette(sandwich_jambon_beurre).

% Ingr�dients pour chaque recette
ingredients(pizza, [farine, eau, sel, levure, tomate, fromage]).
ingredients(salade, [laitue, tomate, concombre, vinaigre, huile]).
ingredients(pates_carbonara, [pates, creme, lardons, fromage, sel, poivre]).
ingredients(omelette, [oeufs, sel, poivre, fromage]).
ingredients(sandwich_jambon_beurre, [pain, beurre, jambon]).

% 2. R�gle pour v�rifier si tous les ingr�dients n�cessaires sont disponibles
tous_ingredients_disponibles(Recette, IngredientsDisponibles) :-
    ingredients(Recette, IngredientsNecessaires),
    forall(member(Ingredient, IngredientsNecessaires),
           member(Ingredient, IngredientsDisponibles)).

% R�gle pour trouver les recettes possibles
recettes_possibles(IngredientsDisponibles, RecettesPossibles) :-
    findall(Recette,
            (recette(Recette),
             tous_ingredients_disponibles(Recette, IngredientsDisponibles)),
            RecettesPossibles).
