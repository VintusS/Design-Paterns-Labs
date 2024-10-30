package employees.director;

import java.util.HashSet;
import employees.Employee;
import employees.common.SubordinatesManager;

public class Manager implements Employee {
    private String name;
    private double salary;
    public SubordinatesManager subordinatesManager;

    public Manager(String name, double salary, HashSet<Employee> subordinates) {
        this.name = name;
        this.salary = salary;
        this.subordinatesManager = new SubordinatesManager(subordinates);
    }

    @Override
    public double getSalary() {
        return this.salary;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void work() {
        System.out.println("Manager " + this.name
                + " is managing the team");
        for (Employee employee : this.subordinatesManager.getSubordinates()) {
            System.out.println("Manager " + this.name
                    + " is now managing " + employee.getName());
            employee.work();
        }
    }
}
