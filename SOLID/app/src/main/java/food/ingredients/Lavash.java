package food.ingredients;


public class Lavash extends AbstractIngredient {
    private boolean isCheesy;

    public Lavash(String name, String description, boolean isCheesy) {
        super(name, description);
        this.isCheesy = isCheesy;
    }

    public boolean isCheesy() {
        return isCheesy;
    }
}
