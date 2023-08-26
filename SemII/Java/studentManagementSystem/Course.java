import java.util.ArrayList;
import java.io.*;

public class Course implements Serializable {
  private Teacher teacher;
  private ArrayList<Student> students;
  private String name;
  private static final long serialVersionUID = 1L;

  public Course() {
    this.teacher = new Teacher();
    this.students = new ArrayList<Student>();
    this.name = "";
  }

  public Course(Teacher teacher, ArrayList<Student> students, String name) {
    this.teacher = teacher;
    this.students = students;
    this.name = name;
  }

  public Teacher getTeacher() {
    return this.teacher;
  }

  public ArrayList<Student> getStudents() {
    return this.students;
  }

  public String getName() {
    return this.name;
  }

  void writeObjectsToFile(String filepath, Object serObj) {
    try {
      FileOutputStream fileOut = new FileOutputStream(filepath);
      ObjectOutputStream objectOut = new ObjectOutputStream(fileOut);
      objectOut.writeObject(serObj);
      objectOut.close();
    } catch (Exception ex) {
      ex.printStackTrace();
    }
  }

  public void saveClass() {
    ArrayList<Object> objects = new ArrayList<Object>();
    objects.add(this);
    writeObjectsToFile("data.bin", this);
    System.out.println("Course saved to data.bin");
  }

  static ArrayList<Object> readObjectsFromFile(String filepath) {
    ArrayList<Object> objects = new ArrayList<Object>();
    try {
      FileInputStream fileIn = new FileInputStream(filepath);
      ObjectInputStream objectIn = new ObjectInputStream(fileIn);
      Object obj = objectIn.readObject();
      objects.add(obj);
    } catch (Exception ex) {
      ex.printStackTrace();
    }
    return objects;
  }

  public static Course loadClass() {
    ArrayList<Object> objects = new ArrayList<Object>();
    objects = readObjectsFromFile("data.bin");
    Course course = (Course) objects.get(0);
    return new Course(course.teacher, course.students, course.name);
  }
}
