import java.io.Serializable;

public class Teacher implements Serializable {
  private int id;
  private String name;
  private String department;
  private static final long serialVersionUID = 1L;

  public Teacher() {
    this.id = 0;
    this.name = "";
    this.department = "";
  }

  public Teacher(int id, String name, String department) {
    this.id = id;
    this.name = name;
    this.department = department;
  }

  public int getId() {
    return this.id;
  }

  public String getName() {
    return this.name;
  }

  public String getDepartment() {
    return this.department;
  }

  public void setId(int id) {
    this.id = id;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setDepartment(String department) {
    this.department = department;
  }

  public String toString() {
    return "Teacher: " + this.name + " (" + this.id + ") " + "Department: " + this.department;
  }
}
