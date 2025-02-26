import java.util.Scanner;

public class ToDoListApp {
    static String[][] tasks = new String[100][2]; // 2D Array to store task description and status
    static int taskCount = 0; // Counter for number of tasks

    public static String welcomeHeading() {
        return "\n<<< Welcome to My To-Do List Application >>>\n" +
               "____________________________________________\n";
    }

    public static String displayMenu() {
        return "1. Add a Task\n" +
               "2. View All Tasks\n" +
               "3. Mark Task as Complete\n" +
               "4. Delete a Task\n" +
               "5. Exit\n";
    }

    public static String addTask(String taskDescription) {
        if (taskCount < tasks.length) {
            tasks[taskCount][0] = taskDescription; // Store task description
            tasks[taskCount][1] = "Incomplete";   // Default status
            taskCount++;
            return "\n<<< Task added successfully >>>\n";
        } else {
            return "\nTask list is full! Cannot add more tasks.\n";
        }
    }

    public static String viewTasks() {
        if (taskCount == 0) {
            return "No tasks recorded.\n";
        }
        String result = "\n<<< Tasks >>>\n";
        for (int i = 0; i < taskCount; i++) {
            String taskStatus = tasks[i][1].equals("Complete") ? "[X] " : "[ ] ";
            result += (i + 1) + ". " + taskStatus + tasks[i][0] + "\n";
        }
        return result;
    }

    public static String markTaskComplete(int taskNumber) {
        if (taskNumber >= 1 && taskNumber <= taskCount) {
            tasks[taskNumber - 1][1] = "Complete";
            return "Task marked as complete!\n";
        } else {
            return "Invalid task number.\n";
        }
    }

    public static String deleteTask(int taskNumber) {
        if (taskNumber >= 1 && taskNumber <= taskCount) {
            for (int i = taskNumber - 1; i < taskCount - 1; i++) {
                tasks[i][0] = tasks[i + 1][0];
                tasks[i][1] = tasks[i + 1][1];
            }
            taskCount--;
            return "Task deleted!\n";
        } else {
            return "Invalid task number.\n";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println(welcomeHeading());

        while (true) {
            System.out.println(displayMenu());
            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Enter task description: ");
                String taskDescription = scanner.nextLine();
                System.out.println(addTask(taskDescription));
            } else if (choice.equals("2")) {
                System.out.println(viewTasks());
            } else if (choice.equals("3")) {
                System.out.println(viewTasks());
                System.out.print("Enter task number to mark complete: ");
                int taskNumber = scanner.nextInt();
                scanner.nextLine(); // Consume newline
                System.out.println(markTaskComplete(taskNumber));
            } else if (choice.equals("4")) {
                System.out.println(viewTasks());
                System.out.print("Enter task number to delete: ");
                int taskNumber = scanner.nextInt();
                scanner.nextLine(); // Consume newline
                System.out.println(deleteTask(taskNumber));
            } else if (choice.equals("5")) {
                System.out.println("Exiting application. Goodbye!");
                break;
            } else {
                System.out.println("Invalid choice, please try again.");
            }
        }
       
    }
}
