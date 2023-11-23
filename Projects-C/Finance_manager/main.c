#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_USERS 100
#define MAX_NAME_LENGTH 50
#define MAX_PASSWORD_LENGTH 50
#define MAX_EXPENSES 100
#define MAX_DESCRIPTION_LENGTH 100

struct Expense {
    float amount;
    char description[MAX_DESCRIPTION_LENGTH];
};

struct User {
    char username[MAX_NAME_LENGTH];
    char password[MAX_PASSWORD_LENGTH];
    float totalIncome;
    float totalExpense;
    struct Expense expenses[MAX_EXPENSES];
    int expenseCount;
};

int userCount = 0;
struct User users[MAX_USERS];

// Function to clear the console screen
void clearScreen() {
    system("clear || cls");
}

// Function to register a new user
void registerUser() {
    clearScreen();  // Clear the console

    printf("Enter your username: ");
    scanf("%s", users[userCount].username);

    printf("Enter your password: ");
    scanf("%s", users[userCount].password);

    users[userCount].totalIncome = 0;
    users[userCount].totalExpense = 0;

    printf("Registration successful!\n");

    userCount++;
}

// Function to authenticate a user
int authenticateUser(char *username, char *password, int *index) {
    for (int i = 0; i < userCount; i++) {
        if (strcmp(username, users[i].username) == 0 && strcmp(password, users[i].password) == 0) {
            *index = i;
            return 1; // Authentication successful
        }
    }
    return 0; // Authentication failed
}

// Function to add income
void addIncome(struct User *user) {
    float income;
    printf("Enter the income amount: $");
    scanf("%f", &income);
    user->totalIncome += income;
    printf("Income added successfully!\n");
}

// Function to add expense with details
void addExpenseWithDetails(struct User *user) {
    clearScreen();  // Clear the console

    struct Expense *currentExpense = &user->expenses[user->expenseCount];
    
    printf("Enter the expense amount: $");
    scanf("%f", &currentExpense->amount);

    // clearBuffer();  // Clear the input buffer

    printf("Enter a description for the expense: ");
    fgets(currentExpense->description, MAX_DESCRIPTION_LENGTH, stdin);

    // Remove the newline character at the end
    size_t len = strlen(currentExpense->description);
    if (len > 0 && currentExpense->description[len - 1] == '\n') {
        currentExpense->description[len - 1] = '\0';
    }

    user->totalExpense += currentExpense->amount;
    user->expenseCount++;

    printf("Expense added successfully!\n");
}

// Function to view financial status and expense details
void viewFinancialStatus(struct User *user) {
    clearScreen();  // Clear the console

    printf("\nFinancial Status for User: %s\n", user->username);
    printf("Total Income: $%.2f\n", user->totalIncome);
    printf("Total Expense: $%.2f\n", user->totalExpense);
    printf("Remaining Balance: $%.2f\n", user->totalIncome - user->totalExpense);
    
    // Ask the user to go back to the main menu
    printf("\nDo you want to go back to the main menu? (y/n): ");
    char choice;
    scanf(" %c", &choice);

    if (choice == 'y' || choice == 'Y') {
        return;  // Return to the main menu
    }
}

// Function to view expense details
void viewExpenseDetails(struct User *user) {
    clearScreen();  // Clear the console

    printf("\nExpense Details for User: %s\n", user->username);

    if (user->expenseCount > 0) {
        for (int i = 0; i < user->expenseCount; i++) {
            printf("%d. Amount: $%.2f, Description: %s\n", i + 1, user->expenses[i].amount, user->expenses[i].description);
        }
    } else {
        printf("No expenses to display.\n");
    }

    // Ask the user to go back to the main menu
    printf("\nDo you want to go back to the main menu? (y/n): ");
    char choice;
    scanf(" %c", &choice);

    if (choice == 'y' || choice == 'Y') {
        return;  // Return to the main menu
    }
}

// Function to display the main menu
void displayMenu() {
    clearScreen();
    printf("\nPersonal Finance Manager\n");
    printf("1. Add Income\n");
    printf("2. Add Expense\n");
    printf("3. View Financial Status\n");
    printf("4. View Expense Details\n");  // Add this line
    printf("5. Logout\n");
}

int main() {
    int choice;
    char username[MAX_NAME_LENGTH];
    char password[MAX_PASSWORD_LENGTH];
    int currentUserIndex;

    do {
        clearScreen();
        printf("\n1. Register\n");
        printf("2. Login\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                registerUser();
                break;
            case 2:
                printf("Enter your username: ");
                scanf("%s", username);

                printf("Enter your password: ");
                scanf("%s", password);

                if (authenticateUser(username, password, &currentUserIndex)) {
                    printf("Login successful!\n");

                    do {
                        displayMenu();
                        printf("Enter your choice: ");
                        scanf("%d", &choice);

                        // Modify the switch-case block in the main loop
                        switch (choice) {
                            case 1:
                                addIncome(&users[currentUserIndex]);
                                break;
                            case 2:
                                addExpenseWithDetails(&users[currentUserIndex]);  // Change to use the new function
                                break;
                            case 3:
                                viewFinancialStatus(&users[currentUserIndex]);
                                break;
                            case 4:
                                viewExpenseDetails(&users[currentUserIndex]);  // Add this line
                                break;
                            case 5:
                                printf("Logging out...\n");
                                break;
                            default:
                                printf("Invalid choice. Please try again.\n");
                        }

                    } while (choice != 5);

                } else {
                    printf("Authentication failed. Please check your username and password.\n");
                }
                break;
            case 3:
                printf("Exiting the program. Goodbye!\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 3);

    return 0;
}