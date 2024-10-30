package food.ingredients;

public class Falafel extends AbstractIngredient {
    private boolean isGlutenFree;

    public Falafel(String name, String description, boolean isGlutenFree) {
        super(name, description);
        this.isGlutenFree = isGlutenFree;
    }

    public boolean isGlutenFree() {
        return isGlutenFree;
    }
}
