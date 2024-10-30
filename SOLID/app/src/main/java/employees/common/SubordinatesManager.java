package employees.common;

import java.util.HashSet;

import javax.annotation.Nullable;

import employees.Employee;

public class SubordinatesManager {
    @Nullable
    private HashSet<Employee> subordinates;

    public SubordinatesManager(HashSet<Employee> subordinates) {
        if (subordinates == null) {
            this.subordinates = new HashSet<>();
        } else {
            this.subordinates = new HashSet<>(subordinates);
        }
    }

    public HashSet<Employee> getSubordinates() {
        return this.subordinates;
    }

    public void setSubordinates(HashSet<Employee> subordinates) {
        this.subordinates = subordinates;
    }

    public void addSubordinate(Employee employee) {
        this.subordinates.add(employee);
    }

    public void removeSubordinate(Employee employee) {
        this.subordinates.remove(employee);
    }
}
