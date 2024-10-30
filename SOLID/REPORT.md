# SOLID Principles

## Author: Mindrescu Dragomir
## Group: FAF-221

---

## Theory

The SOLID principles in software engineering provide guidelines for creating maintainable, understandable, and adaptable software. These principles improve design and architecture, making software systems easier to manage and extend.

The SOLID principles are:

* **Single Responsibility Principle (SRP)**  
  *Each class should have only one reason to change.*
* **Open-Closed Principle (OCP)**  
  *Software entities should be open for extension but closed for modification.*
* **Liskov Substitution Principle (LSP)**  
  *Objects of derived classes should be replaceable for their base classes without altering functionality.*
* **Interface Segregation Principle (ISP)**  
  *Clients should not be forced to depend on interfaces they do not use.*
* **Dependency Inversion Principle (DIP)**  
  *Depend on abstractions, not on concrete implementations.*

## Objectives:

* Gain familiarity with SOLID principles in software design.
* Implement two of these principles in a simple project.

## Implementation

To demonstrate the SOLID principles, a restaurant simulation is implemented where each component adheres to SOLID guidelines, resulting in a readable, extendable, and maintainable codebase.

### Single Responsibility Principle (SRP)
In this simulation, we want employees focused on single responsibilities. For example, a `Barman` class has the sole responsibility of serving drinks.

```java
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
```

This is a good example of SRP, since it focuses on the Barman's sole responsibility of serving drinks. It also adds a safety check and handles cases when a barman is asked to serve something other than a drink.

### Open-Closed Principle
We may serve multiple dishes at a restaurant. All those are somewhat similar, so we can start with the most common thing. We can define an abstract class `MenuItem`
```java
package food.items;

public abstract class MenuItem {
    protected String name;
    protected String description;
    protected double price;

    public MenuItem(String name, String description, double price) {
        this.name = name;
        this.description = description;
        this.price = price;
    }

    public String getDescription() {
        return this.description;
    }

    public String getName() {
        return this.name;
    }

    public double getPrice() {
        return this.price;
    }
}
```
Then we can use that to define the `FoodMenuItem` class that specializes in representing different dishes on our menu.
```java
package food.items.food;

import food.items.MenuItem;
import food.recipes.Recipe;

public class FoodMenuItem extends MenuItem {
    protected Recipe recipe;
    protected double weight;

    public FoodMenuItem(String name, String description, double price, Recipe recipe, double weight) {
        super(name, description, price);
        this.recipe = recipe;
        this.weight = weight;
    }

    public Recipe getRecipe() {
        return this.recipe;
    }

    public double getWeight() {
        return this.weight;
    }
}
```
and the `DrinkMenuItem` for items on our menu that are actually drinks.
```java
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
```
and we can go even further and extend a `DrinkMenuItem` to an `AlcoholicDrinkMenuItem`.
```java
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
```
This demonstrates that our system is open for extension - new types of menu items can be added by creating other specialized classes starting from the `MenuItem` abstract class, or extend upon other already specialized classes, like the `DrinkMenuItem` and `AlcoholicDrinkMenuItem`.
If we were to add a nullable `alcoholPercentage` field to the `DrinkMenuItem` class, we would jeopardize the flexibility of our system.

### Liskov Sybstitution Principle
It may become hard to manage people manually by telling them to work. That's why managers exist, so we can focus on other aspects of the restaurant. 
The `SubordinatesManager` is a utility class responsible for CRUD operations on employees some class has to manage. 
```java
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
                    + " is managing " + employee.getName());
            employee.work();
        }
    }
}
```
The `Manager` implements the `Employee` interface, which would allow us creating 10 layers of management in this restaurant. The role of a `Manager` is to delegate work to other `Employee` objects. 
Since any class that implements the `Employee` interface must implement the `work()` method, a `Manager` will be able to put any employee to work, either a cook, barman, accountant, or even another `Manager`
This is an example of the Liskov Substitution Principle - we allow a `Manager` call the `work()` method on employees without the `Manager` needing to know the concrete implementation or any details, and this will not break the system logic.

### Interface Segregation Principle
We can have different types of employees working in a restaurant. To ensure that they are following the SRP and the OCP, it would be useful to follow the Interface Segregation Principle. 
For example, we have the `Employee` interface:
```java
package employees;

public interface Employee {
    public String getName();

    public double getSalary();

    public void work();
}
```
which defines the most generalized *contract* each employee must adhere to. Since we have employees that serve people, we can name them `ProducingEmployee`, which will have a new method added to the base interface, `giveRequest`
```java
package employees.producers;

import employees.Employee;
import food.items.MenuItem;

public interface ProducingEmployee extends Employee {
    public void giveRequest(MenuItem menuItem);
}
```
This approach allows us to have the class `Accountant` that implements only the `Employee` interface, and the classes `Cook` and `Barman` will implement the `ProducingEmployee`. Thus an `Accountant` doesn't need to implement unnecessary for its' job methods. 
```java
public class Accountant implements Employee {
    private String name;
    private double salary;
    @Nullable
    private HashSet<Employee> subordinates;

    public Accountant(String name, double salary, HashSet<Employee> subordinates) {
        this.name = name;
        this.salary = salary;
        if (subordinates == null) {
            this.subordinates = new HashSet<>();
        } else {
            this.subordinates = new HashSet<>(subordinates);
        }
    }
```

### Dependency Inversion Principle
Following the previously used `Accountant` class, we can describe also the DIP. The `Accountant` class has methods used to pay salaries to other people - objects that implement the `Employee` interface. 
```java
package employees.accountant;

import java.util.HashSet;

import employees.Employee;

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
        System.out.println("Paying myself $" + this.salary);
    }
}
```
This implementation follows the Dependency Inversion Principle (DIP) by ensuring that Accountant depends on the Employee interface (an abstraction), not concrete classes. The SubordinatesManager handles operations on employees, keeping Accountant decoupled from low-level details. 
This design allows for easy extension with new employee types, making the system flexible and maintaining adherence to the DIP by relying on abstractions rather than specific implementations.


## Results
In the main class, define a method `simulateRestaurant()` like this:
```java
public static void simulateRestaurant() {
        Recipe kebabRecipe = getKebabRecipe();
        FoodMenuItem kebab = new FoodMenuItem("Kebab",
                "Tender chicken kebab", 50, kebabRecipe, 420);
        Set<FoodMenuItem> cookableItems = Set.of(kebab);
        DrinkMenuItem jager = getJager();
        Cook cook = new Cook("John", 1000, cookableItems);
        cook.giveRequest(kebab);
        cook.giveRequest(kebab);
        Barman barman = new Barman("Nick", 1000);
        barman.giveRequest(kebab);
        barman.giveRequest(jager);
        Accountant accountant = new Accountant("Jane", 2000, null);
        accountant.subordinates.addSubordinate(cook);
        Manager kitchenManager = new Manager("Jake", 1500, null);
        Manager humanResourcesManager = new Manager("Alice", 1500, null);
        kitchenManager.subordinatesManager.addSubordinate(cook);
        kitchenManager.subordinatesManager.addSubordinate(barman);
        humanResourcesManager.subordinatesManager.addSubordinate(accountant);
        kitchenManager.work();
        humanResourcesManager.work();
    }
```
Where we instantiate some objects that will help showcasing the execution of the system. Using the `./gradlew run` command on Linux, we will see this output: 
```
Kebab has been added to John's cooking queue.
Kebab has been added to John's cooking queue.
Barman can only serve drinks
I'm a barman, I'm giving you some Jagermeister
Manager Jake is managing the team
Manager Jake is now managing John
John is cooking Kebab.
Step 1: Grill the chicken for 60 seconds.
Step 2: Cut the tomatoes
Step 3: Cut the onions
Step 4: Unfold the lavash
Step 5: Mix the ingredients
Step 6: Wrap the ingredients
John is cooking Kebab.
Step 1: Grill the chicken for 60 seconds.
Step 2: Cut the tomatoes
Step 3: Cut the onions
Step 4: Unfold the lavash
Step 5: Mix the ingredients
Step 6: Wrap the ingredients
Manager Jake is now managing Nick
I'm a barman, I'm working
Manager Alice is managing the team
Manager Alice is now managing Jane
I'm an accountant, I'm working
Paying John $1000.0
Paying myself, Jane $2000.0
```

# Conclusions
In this lab work, we successfully implemented the SOLID principles in a restaurant simulation, demonstrating how these design guidelines can lead to cleaner, more maintainable, and flexible code. 
By applying the Single Responsibility Principle, we ensured that each class has a distinct role, such as the Barman focusing solely on serving drinks. 
The Open-Closed Principle allowed us to easily extend our menu system without modifying existing code, promoting scalability. 
Additionally, the Liskov Substitution Principle enabled seamless interaction between various employee types, reinforcing the use of abstractions through the Employee interface. 
The Interface Segregation Principle ensured that employees only implemented the methods necessary for their roles, while the Dependency Inversion Principle decoupled high-level components from low-level implementations, fostering flexibility and adaptability in our design. 
Overall, this exercise highlighted the importance of adhering to SOLID principles in software development, ultimately leading to a robust and extensible architecture suitable for real-world applications.