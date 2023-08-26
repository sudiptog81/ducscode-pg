final class Main {
  int i = 10;
  static final int j = 5;

  static {
    System.out.println("Main class initialized...");
  }

  void show() {
    int i = 100;
    System.out.println("Local Variable: " + i);
    System.out.println("Instance Variable: " + this.i);
  }

  static void display() {
    System.out.println("Static Variable: " + j);
    // j = j + 10;
  }

  public static void main(String[] args) {
    Main m = new Main();
    m.show();
    m.display();
    Main.display();
  }
}

// class A extends Main {

// }
