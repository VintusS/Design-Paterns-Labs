package food.recipes;

import food.ingredients.AbstractIngredient;
import food.recipes.steps.RecipeStep;

public class Recipe {
    private String name;
    private AbstractIngredient[] ingredients;
    private RecipeStep[] steps;

    public Recipe(String name, AbstractIngredient[] ingredients, RecipeStep[] steps) {
        this.name = name;
        this.ingredients = ingredients;
        this.steps = steps;
    }

    public String getName() {
        return name;
    }

    public AbstractIngredient[] getIngredients() {
        return ingredients;
    }

    public RecipeStep[] getSteps() {
        return steps;
    }
}
