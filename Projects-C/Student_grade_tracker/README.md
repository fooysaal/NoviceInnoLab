# Student Grade Tracker (C Console Application)

This is a simple console-based Student Grade Tracker written in C. The program allows users to add student records, display sorted student records, search for a student by ID, calculate and display the average grade of all students, and exit the program.

## Features

- **Add Student:** Users can add new student records by providing the student's name, ID, and grade. The program prompts the user if they want to add more students.

- **Display Students:** The program displays all student records sorted by their IDs. It uses a simple bubble sort algorithm to sort the students.

- **Search Student:** Users can search for a specific student by entering their ID. If the student is found, their information is displayed.

- **Calculate Average Grade:** The program calculates and displays the average grade of all students.

- **Exit:** Users can choose to exit the program.

## Concepts Used

- **Structures:** The program uses a C structure (`struct Student`) to represent each student's data, including name, ID, and grade.

- **File Handling:** Student records are stored in a binary file (`grades.dat`). The program uses file I/O functions (`fopen`, `fwrite`, `fread`, `fclose`) to read and write student records.

- **Dynamic Memory Allocation:** The program dynamically allocates memory for an array of students to facilitate sorting.

- **Sorting Algorithm:** A simple bubble sort algorithm is implemented to sort students by their IDs.

- **Menu-Driven Interface:** The program uses a menu-driven approach, allowing users to choose different operations.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/fooysaal/NoviceInnoLab/Projects-C/student-grade-tracker.git
    ```

2. Compile the program:

    ```bash
    gcc student_grade_tracker.c -o student_grade_tracker
    ```

3. Run the executable:

    ```bash
    ./student_grade_tracker
    ```

## Sample Usage

1. Choose option 1 to add a new student and follow the prompts.

2. Choose option 2 to display sorted student records.

3. Choose option 3 to search for a student by ID.

4. Choose option 4 to calculate and display the average grade.

5. Choose option 5 to exit the program.

## Contribution

Feel free to make changes and work with the projects add new features or modification as per your idea. Create an issue if that benefits
the project it will be a great project.
