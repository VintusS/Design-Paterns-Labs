package food.ingredients.meat.enums;

public enum MeatType {
    BEEF("Beef"),
    CHICKEN("Chicken"),
    LAMB("Lamb");

    private final String value;

    MeatType(String value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return value;
    }
}
