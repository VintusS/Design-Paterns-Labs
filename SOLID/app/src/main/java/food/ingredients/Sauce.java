package food.ingredients;

public class Sauce extends AbstractIngredient {
    private boolean isSpicy;

    public Sauce(String name, String description, boolean isSpicy) {
        super(name, description);
        this.isSpicy = isSpicy;
    }

    public boolean isSpicy() {
        return isSpicy;
    }
}
