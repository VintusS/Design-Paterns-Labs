package food.ingredients.meat;

import food.ingredients.AbstractIngredient;
import food.ingredients.meat.enums.MeatType;

public class Meat extends AbstractIngredient {
    private MeatType meatType;

    public Meat(String name, String description, MeatType meatType) {
        super(name, description);
        this.meatType = meatType;
    }

    public MeatType getMeatType() {
        return meatType;
    }
}
