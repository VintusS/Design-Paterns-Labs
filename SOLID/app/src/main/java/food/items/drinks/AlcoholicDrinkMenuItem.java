package food.items.drinks;

public class AlcoholicDrinkMenuItem extends DrinkMenuItem {
    protected double alcoholPercentage;

    public AlcoholicDrinkMenuItem(String name, String description, double price, double volume,
            double alcoholPercentage) {
        super(name, description, price, volume);
        this.alcoholPercentage = alcoholPercentage;
    }

    public double getAlcoholPercentage() {
        return this.alcoholPercentage;
    }
}
