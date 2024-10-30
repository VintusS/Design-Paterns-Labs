package food.items.drinks;

import food.items.MenuItem;

public class DrinkMenuItem extends MenuItem {
    protected double volume;

    public DrinkMenuItem(String name, String description, double price, double volume) {
        super(name, description, price);
        this.volume = volume;
    }

    public double getVolume() {
        return this.volume;
    }

}