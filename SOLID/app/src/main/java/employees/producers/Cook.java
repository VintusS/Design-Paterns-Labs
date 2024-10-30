package employees.producers;

import food.items.food.FoodMenuItem;
import food.items.MenuItem;
import food.recipes.steps.RecipeStep;
import food.recipes.steps.TimedRecipeStep;
import java.util.LinkedList;
import java.util.Set;

import java.util.Queue;

public class Cook extends AbstractProducingEmployee {
    private Set<FoodMenuItem> cookableItems;
    private Queue<FoodMenuItem> cookingQueue;

    public Cook(String name, double salary, Set<FoodMenuItem> cookableItems) {
        super(name, salary);
        this.cookableItems = cookableItems;
        this.cookingQueue = new LinkedList<>();
    }

    @Override
    public void giveRequest(MenuItem item) {
        if (item == null) {
            System.out.println("Cannot add null item to the queue.");
        } else if (!(item instanceof FoodMenuItem)) {
            System.out.println("Cannot add non-food item to the queue.");
        } else {
            System.out.println(item.getName() + " has been added to " + this.getName() + "'s cooking queue.");
            cookingQueue.add((FoodMenuItem) item);
        }
    }

    private void cookNextItem() {
        if (cookingQueue.isEmpty()) {
            System.out.println(this.getName() + " has no items to cook.");
            return;
        }
        FoodMenuItem itemToCook = cookingQueue.poll();
        if (itemToCook != null) {
            boolean canCook = false;
            for (FoodMenuItem menuItem : cookableItems) {
                if (menuItem.equals(itemToCook)) {
                    canCook = true;
                    break;
                }
            }
            if (!canCook) {
                System.out.println(this.getName() + " cannot cook " + itemToCook.getName() + ".");
            } else {
                System.out.println(this.getName() + " is cooking " + itemToCook.getName() + ".");
                RecipeStep[] steps = itemToCook.getRecipe().getSteps();
                for (int i = 0; i < steps.length; i++) {
                    RecipeStep step = steps[i];
                    if (step instanceof TimedRecipeStep) {
                        TimedRecipeStep timedStep = (TimedRecipeStep) step;
                        System.out.println("Step " + (i + 1) + ": " + timedStep.getDescription() + " for "
                                + timedStep.getDuration().toSeconds() + " seconds.");
                    } else {
                        System.out.println("Step " + (i + 1) + ": " + step.getDescription());
                    }
                }
            }
        }
    }

    @Override
    public void work() {
        while (!cookingQueue.isEmpty()) {
            this.cookNextItem();
        }
    }
}
