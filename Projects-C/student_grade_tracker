#include <stdio.h>
#include <stdlib.h>

struct Student {
    char name[50];
    int id;
    float grade;
};

// Function to add a new student record
void addStudent(FILE *file) {
    struct Student student;

    do {
        printf("Enter student name: ");
        scanf("%s", student.name);
        printf("Enter student ID: ");
        scanf("%d", &student.id);
        printf("Enter student grade: ");
        scanf("%f", &student.grade);

        fwrite(&student, sizeof(struct Student), 1, file);

        printf("Student record added successfully.\n");

        // Ask if the user wants to add another student
        printf("Do you want to add another student? (y/n): ");
        char choice;
        scanf(" %c", &choice);

        if (choice != 'y' && choice != 'Y') {
            break;
        }
    } while (1);
}

// Function to display sorted student records by ID
void displayStudents(FILE *file) {
    struct Student *students;
    struct Student temp;
    int studentCount = 0;

    // Count the number of students in the file
    rewind(file);
    while (fread(&temp, sizeof(struct Student), 1, file) == 1) {
        studentCount++;
    }

    // Allocate memory for an array of students
    students = (struct Student *)malloc(studentCount * sizeof(struct Student));

    // Read students from the file into the array
    rewind(file);
    for (int i = 0; i < studentCount; i++) {
        fread(&students[i], sizeof(struct Student), 1, file);
    }

    // Sort the students by ID using bubble sort (you can use other sorting algorithms for efficiency)
    for (int i = 0; i < studentCount - 1; i++) {
        for (int j = 0; j < studentCount - i - 1; j++) {
            if (students[j].id > students[j + 1].id) {
                // Swap the students
                struct Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }

    // Display sorted students
    printf("\nStudent Records (Sorted by ID):\n");
    printf("------------------------------------------------\n");
    printf("%-20s %-10s %-10s\n", "Name", "ID", "Grade");
    printf("------------------------------------------------\n");

    for (int i = 0; i < studentCount; i++) {
        printf("%-20s %-10d %-10.2f\n", students[i].name, students[i].id, students[i].grade);
    }

    printf("------------------------------------------------\n");

    // Free allocated memory
    free(students);
}

// Function to search for a student by ID
void searchStudent(FILE *file) {
    int searchID;
    struct Student student;

    printf("Enter student ID to search: ");
    scanf("%d", &searchID);

    rewind(file);

    while (fread(&student, sizeof(struct Student), 1, file) == 1) {
        if (student.id == searchID) {
            printf("\nStudent Found:\n");
            printf("------------------------------------------------\n");
            printf("%-20s %-10s %-10s\n", "Name", "ID", "Grade");
            printf("------------------------------------------------\n");
            printf("%-20s %-10d %-10.2f\n", student.name, student.id, student.grade);
            printf("------------------------------------------------\n");
            return;
        }
    }

    printf("Student with ID %d not found.\n", searchID);
}

// Function to calculate and display the average grade of all students
void calculateAverageGrade(FILE *file) {
    struct Student student;
    float totalGrade = 0.0;
    int studentCount = 0;

    rewind(file);

    while (fread(&student, sizeof(struct Student), 1, file) == 1) {
        totalGrade += student.grade;
        studentCount++;
    }

    if (studentCount > 0) {
        float averageGrade = totalGrade / studentCount;
        printf("Average Grade of all students: %.2f\n", averageGrade);
    } else {
        printf("No students in the records.\n");
    }
}

int main() {
    FILE *file;

    file = fopen("grades.dat", "ab+");

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    int choice;

    do {
        printf("------------------------------------------------\n");
        printf("\n\t\tStudent Grade Tracker\n\n");
        printf("------------------------------------------------\n");
        printf("1. Add Student\n");
        printf("2. Display Students\n");
        printf("3. Search Student\n");
        printf("4. Calculate Average Grade\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStudent(file);
                break;
            case 2:
                displayStudents(file);
                break;
            case 3:
                searchStudent(file);
                break;
            case 4:
                calculateAverageGrade(file);
                break;
            case 5:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }

    } while (choice != 5);

    fclose(file);

    return 0;
}
