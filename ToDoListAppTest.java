import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ToDoListAppTest {

    @Test
    public void testWelcomeHeading() {
        String expected = "\n<<< Welcome to My To-Do List Application >>>\n" +
                          "____________________________________________\n";
        assertEquals(expected, ToDoListApp.welcomeHeading());
    }

    @Test
    public void testDisplayMenu() {
        String expected = "1. Add a Task\n" +
                          "2. View All Tasks\n" +
                          "3. Mark Task as Complete\n" +
                          "4. Delete a Task\n" +
                          "5. Exit\n";
        assertEquals(expected, ToDoListApp.displayMenu());
    }

    @Test
    public void testAddTask() {
        // Reset state manually
        ToDoListApp.taskCount = 0;
        ToDoListApp.tasks = new String[100][2];

        String result = ToDoListApp.addTask("Buy groceries");
        assertEquals("\n<<< Task added successfully >>>\n", result);
        assertEquals(1, ToDoListApp.taskCount);
        assertEquals("Buy groceries", ToDoListApp.tasks[0][0]);
        assertEquals("Incomplete", ToDoListApp.tasks[0][1]);
    }

    @Test
    public void testViewTasksWhenEmpty() {
        // Reset state manually
        ToDoListApp.taskCount = 0;
        ToDoListApp.tasks = new String[100][2];

        assertEquals("No tasks recorded.\n", ToDoListApp.viewTasks());
    }

    @Test
    public void testViewTasksWithTasks() {
        // Reset state manually
        ToDoListApp.taskCount = 0;
        ToDoListApp.tasks = new String[100][2];

        ToDoListApp.addTask("Buy groceries");
        ToDoListApp.addTask("Read a book");

        String expected = "\n<<< Tasks >>>\n" +
                          "1. [ ] Buy groceries\n" +
                          "2. [ ] Read a book\n";

        assertEquals(expected, ToDoListApp.viewTasks());
    }

    @Test
    public void testMarkTaskCompleteValid() {
        // Reset state manually
        ToDoListApp.taskCount = 0;
        ToDoListApp.tasks = new String[100][2];

        ToDoListApp.addTask("Buy groceries");
        String result = ToDoListApp.markTaskComplete(1);
        assertEquals("Task marked as complete!\n", result);
        assertEquals("Complete", ToDoListApp.tasks[0][1]);
    }

    @Test
    public void testMarkTaskCompleteInvalid() {
        // Reset state manually
        ToDoListApp.taskCount = 0;
        ToDoListApp.tasks = new String[100][2];

        ToDoListApp.addTask("Buy groceries");
        String result = ToDoListApp.markTaskComplete(5);
        assertEquals("Invalid task number.\n", result);
    }

    @Test
    public void testDeleteTaskValid() {
        // Reset state manually
        ToDoListApp.taskCount = 0;
        ToDoListApp.tasks = new String[100][2];

        ToDoListApp.addTask("Buy groceries");
        ToDoListApp.addTask("Read a book");

        String result = ToDoListApp.deleteTask(1);
        assertEquals("Task deleted!\n", result);
        assertEquals(1, ToDoListApp.taskCount);
        assertEquals("Read a book", ToDoListApp.tasks[0][0]); // Shifted up
    }

    @Test
    public void testDeleteTaskInvalid() {
        // Reset state manually
        ToDoListApp.taskCount = 0;
        ToDoListApp.tasks = new String[100][2];

        ToDoListApp.addTask("Buy groceries");
        String result = ToDoListApp.deleteTask(5);
        assertEquals("Invalid task number.\n", result);
    }
}
