package employees.accountant;

import java.util.HashSet;

import employees.Employee;
import employees.common.SubordinatesManager;

public class Accountant implements Employee {
    private String name;
    private double salary;
    public SubordinatesManager subordinates;

    public Accountant(String name, double salary, HashSet<Employee> subordinates) {
        this.name = name;
        this.salary = salary;
        this.subordinates = new SubordinatesManager(subordinates);
    }

    @Override
    public double getSalary() {
        return this.salary;
    }

    @Override
    public String getName() {
        return this.name;
    }

    private void paySalariesTo(Employee employee) {
        System.out.println("Paying " + employee.getName()
                + " $" + employee.getSalary());
    }

    @Override
    public void work() {
        System.out.println("I'm an accountant, I'm working");
        for (Employee employee : this.subordinates.getSubordinates()) {
            paySalariesTo(employee);
        }
        System.out.println("Paying myself, " + this.name
                + " $" + this.salary);
    }

}
