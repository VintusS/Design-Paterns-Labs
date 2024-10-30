package solid;

import java.time.Duration;
import java.util.Set;

import employees.accountant.Accountant;
import employees.director.Manager;
import employees.producers.Barman;
import employees.producers.Cook;
import food.ingredients.AbstractIngredient;
import food.ingredients.Lavash;
import food.ingredients.Vegetable;
import food.ingredients.meat.Meat;
import food.ingredients.meat.enums.MeatType;
import food.items.drinks.AlcoholicDrinkMenuItem;
import food.items.drinks.DrinkMenuItem;
import food.items.food.FoodMenuItem;
import food.recipes.Recipe;
import food.recipes.steps.OneTimeRecipeStep;
import food.recipes.steps.RecipeStep;
import food.recipes.steps.TimedRecipeStep;
import food.recipes.steps.enums.RecipeAction;

public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
        getKebabRecipe();
        simulateRestaurant();
    }

    public static Recipe getKebabRecipe() {
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
        Recipe kebabRecipe = new Recipe("Kebab Recipe", ingredients, steps);
        return kebabRecipe;
    }

    public static DrinkMenuItem getJager() {
        DrinkMenuItem jager = new AlcoholicDrinkMenuItem("Jagermeister", "German herbal liqueur", 25, 0.7, 40);
        return jager;
    }

    public static void simulateRestaurant() {
        Recipe kebabRecipe = getKebabRecipe();
        FoodMenuItem kebab = new FoodMenuItem("Kebab",
                "Tender chicken kebab", 50, kebabRecipe, 420);
        Set<FoodMenuItem> cookableItems = Set.of(kebab);
        DrinkMenuItem jager = getJager();
        Cook cook = new Cook("John", 1000, cookableItems);
        cook.giveRequest(kebab);
        cook.giveRequest(kebab);
        Barman barman = new Barman("Nick", 1000);
        barman.giveRequest(kebab);
        barman.giveRequest(jager);
        Accountant accountant = new Accountant("Jane", 2000, null);
        accountant.subordinates.addSubordinate(cook);
        Manager kitchenManager = new Manager("Jake", 1500, null);
        Manager humanResourcesManager = new Manager("Alice", 1500, null);
        kitchenManager.subordinatesManager.addSubordinate(cook);
        kitchenManager.subordinatesManager.addSubordinate(barman);
        humanResourcesManager.subordinatesManager.addSubordinate(accountant);
        kitchenManager.work();
        humanResourcesManager.work();
    }
}
