package employees.producers;

import food.items.MenuItem;

public abstract class AbstractProducingEmployee implements ProducingEmployee {
    protected String name;
    protected double salary;

    public AbstractProducingEmployee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public double getSalary() {
        return this.salary;
    }

    public abstract void giveRequest(MenuItem menuItem);
}
