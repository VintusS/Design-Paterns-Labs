package food.recipes.steps;

import javax.annotation.Nullable;

import food.ingredients.AbstractIngredient;
import food.recipes.steps.enums.RecipeAction;

public interface RecipeStep {
    public AbstractIngredient getIngredient();

    @Nullable
    public String getDescription();

    public RecipeAction getAction();
}
