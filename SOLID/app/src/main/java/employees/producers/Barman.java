package employees.producers;

import food.items.MenuItem;
import food.items.drinks.DrinkMenuItem;

public class Barman extends AbstractProducingEmployee {
    public Barman(String name, double salary) {
        super(name, salary);
    }

    @Override
    public void giveRequest(MenuItem menuItem) {
        if (menuItem == null) {
            System.err.println("Menu item cannot be null");
        } else if (!(menuItem instanceof DrinkMenuItem)) {
            System.err.println("Barman can only serve drinks");
        } else {
            System.out.println("I'm a barman, I'm giving you some " + menuItem.getName());
        }
    }

    @Override
    public void work() {
        System.out.println("I'm a barman, I'm working");
    }

}
