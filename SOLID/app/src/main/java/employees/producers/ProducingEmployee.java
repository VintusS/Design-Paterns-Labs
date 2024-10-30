package employees.producers;

import employees.Employee;
import food.items.MenuItem;

public interface ProducingEmployee extends Employee {
    public void giveRequest(MenuItem menuItem);
}
