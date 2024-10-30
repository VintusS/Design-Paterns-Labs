package food.recipes.steps;

import food.ingredients.AbstractIngredient;
import food.recipes.steps.enums.RecipeAction;

public class OneTimeRecipeStep implements RecipeStep {
    protected AbstractIngredient ingredient;
    protected String description;
    protected RecipeAction action;

    public OneTimeRecipeStep(AbstractIngredient ingredient, String description, RecipeAction action) {
        this.ingredient = ingredient;
        this.description = description;
        this.action = action;
    }

    @Override
    public RecipeAction getAction() {
        return this.action;
    }

    @Override
    public String getDescription() {
        return this.description;
    }

    @Override
    public AbstractIngredient getIngredient() {
        return this.ingredient;
    }

}
