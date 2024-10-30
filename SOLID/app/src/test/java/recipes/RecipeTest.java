package recipes;

import java.time.Duration;
import food.ingredients.AbstractIngredient;
import food.ingredients.Lavash;
import food.ingredients.Vegetable;
import food.ingredients.meat.Meat;
import food.ingredients.meat.enums.MeatType;
import food.recipes.Recipe;
import food.recipes.steps.RecipeStep;
import food.recipes.steps.enums.RecipeAction;
import food.recipes.steps.OneTimeRecipeStep;
import food.recipes.steps.TimedRecipeStep;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class RecipeTest {
    @Test
    void KebabRecipe() {
        AbstractIngredient chicken = new Meat("Chicken Tighs", "Tender chicken tighs", MeatType.CHICKEN);
        AbstractIngredient toamtoes = new Vegetable("Tomato", "Fresh Tomatos", true);
        AbstractIngredient onions = new Vegetable("Onion", "Fresh Onions", true);
        AbstractIngredient bellPepper = new Vegetable("Bell Pepper", "Fresh Bell Pepper", true);
        AbstractIngredient lavash = new Lavash("Lavash", "Arabic lavash", false);
        RecipeStep grillChicken = new TimedRecipeStep(chicken, "Grill the chicken", RecipeAction.GRILL,
                Duration.ofMinutes(1));
        RecipeStep cutTomatoes = new OneTimeRecipeStep(lavash, "Cut the tomatoes", RecipeAction.CUT);
        RecipeStep cutOnions = new OneTimeRecipeStep(lavash, "Cut the onions", RecipeAction.CUT);
        RecipeStep unfoldLavash = new OneTimeRecipeStep(lavash, "Unfold the lavash", RecipeAction.UNFOLD);
        RecipeStep mixIngredients = new OneTimeRecipeStep(lavash, "Mix the ingredients", RecipeAction.MIX);
        RecipeStep wrapIngredients = new OneTimeRecipeStep(lavash, "Wrap the ingredients", RecipeAction.FOLD);
        AbstractIngredient[] ingredients = { chicken, toamtoes, onions, bellPepper, lavash };
        RecipeStep[] steps = { grillChicken, cutTomatoes, cutOnions, unfoldLavash, mixIngredients, wrapIngredients };
        Recipe kebab = new Recipe("Kebab Recipe", ingredients, steps);
        System.out.println("You have successfully created a Kebab Recipe");
        assertEquals("Kebab Recipe", kebab.getName());
    }
}
