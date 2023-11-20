#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TASKS 100
#define MAX_TASK_LENGTH 50
#define MAX_NAME_LENGTH 50

struct Task {
    char description[MAX_TASK_LENGTH];
    int done;
};

// Function to clear the console screen
void clearScreen() {
    system("clear || cls");
}

// Function to print a welcome header with task statistics
void printHeader(char *userName, int taskCount, int tasksDone) {
    clearScreen();
    printf("Welcome, %s!\n", userName);
    printf("Total tasks: %d\tTasks done: %d\n\n", taskCount, tasksDone);
}

// Function to add a new task to the task list
void addTask(struct Task tasks[], int *taskCount) {
    if (*taskCount < MAX_TASKS) {
        clearScreen();
        printf("<===To-Do List ADD TASK===>\n");
        printf("Enter task description: ");
        scanf(" %[^\n]s", tasks[*taskCount].description);
        tasks[*taskCount].done = 0;
        (*taskCount)++;
        printf("Task added successfully!\n");
    } else {
        printf("Sorry, the task list is full.\n");
    }
}

// Function to view tasks and interact with the user
void viewTasks(struct Task tasks[], int taskCount, int *tasksDone) {
    int userChoice;

    do {
        // Reset tasksDone counter for the current view
        int currentTasksDone = 0;

        printHeader("To-Do List", taskCount, *tasksDone);
        printf("Tasks:\n");

        for (int i = 0; i < taskCount; i++) {
            printf("%d. %s - %s\n", i + 1, tasks[i].description, (tasks[i].done == 1) ? "Done" : "Not Done");

            // Increment the counter only if the task is marked as done
            if (tasks[i].done == 1) {
                currentTasksDone++;
            }
        }

        printf("\n\n");

        printf("1. Back to Main Menu\n");
        printf("Enter your choice: ");
        scanf("%d", &userChoice);

        // Update the total tasksDone after processing all tasks
        *tasksDone = currentTasksDone;

    } while (userChoice != 1);
}

// Function to mark a task as done
void markAsDone(struct Task tasks[], int taskCount, int *tasksDone) {
    int taskIndex;
    printf("Enter the task number to mark as done: ");
    scanf("%d", &taskIndex);

    if (taskIndex >= 1 && taskIndex <= taskCount) {
        tasks[taskIndex - 1].done = 1;
        (*tasksDone)++;
        printf("Task marked as done!\n");
    } else {
        printf("Invalid task number.\n");
    }
}

// Function to delete a task from the task list
void deleteTask(struct Task tasks[], int *taskCount, int *tasksDone) {
    int taskIndex;
    printf("Enter the task number to delete: ");
    scanf("%d", &taskIndex);

    if (taskIndex >= 1 && taskIndex <= *taskCount) {
        // Decrement tasksDone if the deleted task was marked as done
        if (tasks[taskIndex - 1].done == 1) {
            (*tasksDone)--;
        }

        for (int i = taskIndex - 1; i < *taskCount - 1; i++) {
            strcpy(tasks[i].description, tasks[i + 1].description);
            tasks[i].done = tasks[i + 1].done;
        }
        (*taskCount)--;
        printf("Task deleted successfully!\n");
    } else {
        printf("Invalid task number.\n");
    }
}

// Main function to run the to-do list program
int main() {
    char userName[MAX_NAME_LENGTH];
    printf("<======================================>\n");
    printf("\tWelcome to To_Do List!\n");
    printf("<======================================>\n");
    printf("Enter your name: ");
    scanf(" %[^\n]s", userName);

    struct Task tasks[MAX_TASKS];
    int taskCount = 0;
    int tasksDone = 0;
    int choice;

    do {
        printHeader(userName, taskCount, 0);
        printf("1. Add Task\n2. View Tasks\n3. Mark as Done\n4. Delete Task\n5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addTask(tasks, &taskCount);
                break;
            case 2:
                viewTasks(tasks, taskCount, &tasksDone);
                break;
            case 3:
                markAsDone(tasks, taskCount, &tasksDone);
                break;
            case 4:
                deleteTask(tasks, &taskCount, &tasksDone);
                break;
            case 5:
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 5);

    return 0;
}