import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

class Event {
    private String name;
    private int availableTickets;

    public Event(String name, int availableTickets) {
        this.name = name;
        this.availableTickets = availableTickets;
    }

    public String getName() {
        return name;
    }

    public int getAvailableTickets() {
        return availableTickets;
    }

    public void setAvailableTickets(int availableTickets) {
        this.availableTickets = availableTickets;
    }
}

class Booking {
    private String eventName;
    private int numTickets;
    private String userName;
    private String phoneNumber;
    private String email;

    public Booking(String eventName, int numTickets, String userName, String phoneNumber, String email) {
        this.eventName = eventName;
        this.numTickets = numTickets;
        this.userName = userName;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    public String getEventName() {
        return eventName;
    }

    public int getNumTickets() {
        return numTickets;
    }

    public String getUserName() {
        return userName;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getEmail() {
        return email;
    }
}

public class TicketReservationSystem {
    private static ArrayList<Event> events = new ArrayList<>();
    private static ArrayList<Booking> bookings = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        initializeEvents();

        while (true) {
            clearScreen();
            displayMenu();
            int choice = getChoice();

            switch (choice) {
                case 1:
                    displayEvents();
                    break;
                case 2:
                    authenticateUser();
                    break;
                case 3:
                    cancelBooking();
                    break;
                case 4:
                    displayBookings();
                    break;
                case 5:
                    System.out.println("Exiting program. Thank you!");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void initializeEvents() {
        events.add(new Event("Concert", 100));
        events.add(new Event("Movie", 50));
        events.add(new Event("Conference", 30));
    }

    private static void displayMenu() {
        System.out.println("\nTicket Reservation System Menu:");
        System.out.println("1. View available events");
        System.out.println("2. Book tickets");
        System.out.println("3. Cancel booking");
        System.out.println("4. View bookings");
        System.out.println("5. Exit");
        System.out.print("Enter your choice: ");
    }

    private static int getChoice() {
        return scanner.nextInt();
    }

    private static void displayEvents() {
        System.out.println("\nAvailable Events:");
        System.out.println("-------------------------------");
        System.out.printf("%-20s %-10s\n", "Event Name", "Available Tickets");
        System.out.println("-------------------------------");

        for (Event event : events) {
            System.out.printf("%-20s %-10d\n", event.getName(), event.getAvailableTickets());
        }
    }

    private static void authenticateUser() {
        // Implement a simple authentication system
        System.out.print("Enter your username: ");
        String username = scanner.next();
        System.out.print("Enter your password: ");
        String password = scanner.next();

        // You can add more sophisticated authentication logic here
        // For simplicity, we'll just check if the username and password are the same
        if (username.equals(password)) {
            bookTickets();
        } else {
            System.out.println("Authentication failed. Please try again.");
        }
    }

    private static void bookTickets() {
        clearScreen();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the event name: ");
        String eventName = scanner.nextLine();

        Event selectedEvent = findEvent(eventName);

        if (selectedEvent == null) {
            System.out.println("Event not found. Please check the event name.");
            return;
        }

        System.out.print("Enter the number of tickets to book: ");
        int numTickets = scanner.nextInt();

        if (numTickets <= 0 || numTickets > selectedEvent.getAvailableTickets()) {
            System.out.println("Invalid number of tickets. Please enter a valid number.");
            return;
        }

        // Collect user information
        System.out.print("Enter your name: ");
        String userName = scanner.next();
        System.out.print("Enter your phone number: ");
        String phoneNumber = scanner.next();
        System.out.print("Enter your email: ");
        String email = scanner.next();

        // Update available tickets for the event
        selectedEvent.setAvailableTickets(selectedEvent.getAvailableTickets() - numTickets);

        // Add booking to the list
        bookings.add(new Booking(eventName, numTickets, userName, phoneNumber, email));

        System.out.println("Booking successful! Enjoy the event.");
        scanner.nextLine(); // Consume newline character
        scanner.nextLine(); // Wait for user to press Enter before returning to the menu
    }

    private static void cancelBooking() {
        clearScreen();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the event name to cancel booking: ");
        String eventName = scanner.nextLine();

        Event selectedEvent = findEvent(eventName);

        if (selectedEvent == null) {
            System.out.println("Event not found. Please check the event name.");
            return;
        }

        System.out.print("Enter the number of tickets to cancel: ");
        int numTickets = scanner.nextInt();

        Booking bookingToRemove = null;

        // Find the booking to remove
        for (Booking booking : bookings) {
            if (booking.getEventName().equals(eventName) && booking.getNumTickets() == numTickets) {
                bookingToRemove = booking;
                break;
            }
        }

        if (bookingToRemove != null) {
            // Update available tickets for the event
            selectedEvent.setAvailableTickets(selectedEvent.getAvailableTickets() + numTickets);

            // Remove the booking
            bookings.remove(bookingToRemove);

            System.out.println("Booking canceled successfully.");
            scanner.nextLine(); // Consume newline character
            scanner.nextLine(); // Wait for user to press Enter before returning to the menu
        } else {
            System.out.println("Booking not found. Please check the event name and number of tickets.");
        }
    }

    private static void displayBookings() {
        clearScreen();
        System.out.println("\nCurrent Bookings:");
        System.out.println("------------------------------------------------------");
        System.out.printf("%-20s %-10s %-20s %-15s %-20s\n", "Event Name", "Tickets", "User Name", "Phone Number", "Email");
        System.out.println("------------------------------------------------------");

        for (Booking booking : bookings) {
            System.out.printf("%-20s %-10d %-20s %-15s %-20s\n",
                    booking.getEventName(), booking.getNumTickets(), booking.getUserName(),
                    booking.getPhoneNumber(), booking.getEmail());
        }

        scanner.nextLine(); // Consume newline character
        scanner.nextLine(); // Wait for user to press Enter before returning to the menu
    }

    private static Event findEvent(String eventName) {
        for (Event event : events) {
            if (event.getName().equalsIgnoreCase(eventName)) {
                return event;
            }
        }
        return null;
    }

    private static void clearScreen() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}

