import java.io.*;

public class Student implements Serializable {
  private int id;
  private String name;
  private String course;
  private float[] marks;
  private static final long serialVersionUID = 1L;

  public Student() {
    this.id = 0;
    this.name = "";
    this.course = "";
    this.marks = new float[3];
  }

  public Student(int id, String name, String course, float[] marks) {
    this.id = id;
    this.name = name;
    this.course = course;
    this.marks = marks;
  }

  public int getId() {
    return this.id;
  }

  public String getName() {
    return this.name;
  }

  public String getCourse() {
    return this.course;
  }

  public float[] getMarks() {
    return this.marks;
  }

  public void setId(int id) {
    this.id = id;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setCourse(String course) {
    this.course = course;
  }

  public void setMarks(float[] marks) {
    this.marks = marks;
  }

  public float getAverage() {
    float sum = 0;
    for (int i = 0; i < this.marks.length; i++) {
      sum += this.marks[i];
    }
    return sum / this.marks.length;
  }

  public String toString() {
    return "Student: " + this.name + " (" + this.id + ") " + "Course: " + this.course + " Marks: " + this.marks[0]
        + ", " + this.marks[1] + ", " + this.marks[2] + ", Average: " + this.getAverage();
  }
}
