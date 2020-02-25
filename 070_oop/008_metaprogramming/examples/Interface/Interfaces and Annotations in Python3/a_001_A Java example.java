# // # TL;DR: Annotations in Python3 are very useful when declaring interfaces using abc metaclass.
# //
# // If you want to stop reading here, I'm not going to stop you:)
# //
# // If not, allow me to take you to on a small journey where I explain what all of this is about …
# // A Java example
# //
# // Let's assume you have a PostgreSQL database containing employee records. You are building a web site that will be
# // able to display information about an employee given its ID number.
# //
# // You have a class called SQLRepository that allows you to fetch employees by ID, and a EmployeeController class
# // with a viewEmployee method will be called when the user goes through the correct URL.
# //
# // Lastly, you have a Renderer class that knows how to generate the HTML description of your employees.
# // First attempt
# //
# // The most obvious way to implement the controller looks like this:

package mypackage.controller;

import mypackage.Employee;
import mypackage.repository.SQLRepository;
import mypackage.renderer.Renderer;

public class Controller {
    private SQLRepository repository;
    private Renderer renderer;

    public Controller() {
        repository = new SQLRepository();
        renderer = new Renderer();
    }

    public String viewEmployee(int id) {
        Employee employee = repository.getEmployeeByID(id);
        String res = renderer.renderEmployee(employee);
        return res;
    }
}

# // But there are a few problems with this implementation.
# // Testing the controller
# //
# // It's going to be difficult, right?
# //
# // As soon as you want to instantiate a new controller, the constructor of SQLRepository() will get called too, which means you'll have to set up a PostgreSQL database just so you can run the tests.
# //
# // We say that the “flow of control” goes from the Controller to the SQLRepository class, or that there is a runtime dependency between the Controller and the SQLRepository.
# //
# // And since Controller.java contains an import of the SQLRepository class, we say there is a source code dependency between the Controller and the SQLRepository classes.
# //
# // This is where interfaces come in.
# // Introducing an interface
# //
# // We are going to “decouple” the Controller and the SQLRepository by introducing an interface:

# // In Repository.java
public interface Repository {
    public Employee getEmployeeByID(int id);
}

# // Then, we tell SQLRepository to implement the interface:

+import mypackage.repository.Repository;

-public class SQLRepository {
+public class SQLRepository implements Repository {

# And finally we pass the repository as an argument to the Controller constructor:

-import mypackage.repository.SQLRepository;
+import mypackage.repository.Repository;
 import mypackage.renderer.Renderer;

 public class Controller {
-    private SQLRepository repository;
+    private Repository repository;
     private Renderer renderer;

-    public Controller() {
-        repository = new SQLRepository();
+    public Controller(Repository repository) {
+        this.repository = repository;
         renderer = new Renderer();
     }

# Note the flow of control still goes from the Controller to the Repository, but now the Controller.java file no longer depends on the SQLRepository.java source file.
# 
# Instead, both source files now depend on the Repository.java interface.
# 
# This is called the “Dependency Inversion Principle”.
# 
# An other way to describe the change is that we now have a boundary between the controller and the repository, and that the interface is what allows code to cross the boundary.
# 
# Using a different implementation of the Repository interface, it's now possible to test the Controller without ever touching the database:

public class FakeRepository implements Repository {
    private ArrayList<Employee> employees;

    public FakeRepository() {
        employees = new ArrayList<Employee>();
    }

    public void addEmployee(Employee employee) {
        employees.add(employee);
    }

    public Employee getEmployeeByID(int id) {
        return employees.get(id);
    }
}

public class ControllerTest extends TestCase {

    // ...

    public void testViewEmployee() {
        Employee smith = new Employee("John Smith");

        FakeRepository fakeRepository = new FakeRepository();
        fakeRepository.addEmployee(smith);

        Controller controller = new Controller(fakeRepository);

        String html = controller.viewEmployee(0);
        assertEquals(html, "<span class=\"employe\">John Smith</p>");
    }

}

# Interfaces in Java have other use than just dependency inversion, the example is mostly here for the sake of what's coming next.