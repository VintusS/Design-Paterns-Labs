package food.ingredients;


public class Vegetable extends AbstractIngredient {
    private boolean isOrganic;

    public Vegetable(String name, String description, boolean isOrganic) {
        super(name, description);
        this.isOrganic = isOrganic;
    }

    public boolean isOrganic() {
        return isOrganic;
    }
}
