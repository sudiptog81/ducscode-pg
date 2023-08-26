import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
  static Course course;

  void handleMenu() {
    System.out.println("Course: " + course.getName());
    System.out.println("1. View Students");
    System.out.println("2. View Teacher");
    System.out.println("3. Save Course");
    System.out.println("4. Load Course");
    System.out.println("5. Exit");

    System.out.print("Enter your choice: ");
    Scanner scanner = new Scanner(System.in);
    int choice = scanner.nextInt();

    switch (choice) {
      case 1:
        System.out.println("View Students");
        System.out.println(course.getStudents());
        break;
      case 2:
        System.out.println("View Teacher");
        System.out.println(course.getTeacher());
        break;
      case 3:
        System.out.println("Save Course");
        course.saveClass();
        System.out.println("Course saved to data.bin");
        break;
      case 4:
        System.out.println("Load Course");
        course = Course.loadClass();
        System.out.println("Course loaded from data.bin");
        break;
      case 5:
        System.out.println("Bye!");
        break;
      default:
        System.out.println("Invalid Choice");
        break;
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    ArrayList<Student> students = new ArrayList<Student>();

    Teacher teacher = new Teacher(1, "Prof. VB", "CS");

    Student s1 = new Student(1, "SG", "CS", new float[] { 100, 100, 60 });
    Student s2 = new Student(2, "RM", "Maths", new float[] { 100, 90, 60 });
    students.add(s1);
    students.add(s2);

    Course course = new Course(teacher, students, "Computer Science");
    course.saveClass();

    Main main = new Main();
    course = Course.loadClass();
    main.course = course;

    System.out.println("MENU\n------------");
    System.out.println("1. Teacher");
    System.out.println("2: Student");
    System.out.print("Enter Choice: ");

    int choice = sc.nextInt();

    switch (choice) {
      case 1:
        main.handleMenu();
        break;
    }

  }
}
