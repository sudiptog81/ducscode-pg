public class Main {
  static void widening() {
    System.out.println("WIDENING\n--------------");
    short a = 0b10;
    System.out.println((int) (a));
  }

  static void narrowing() {
    System.out.println("NARROWING\n--------------");
    short c = 0x10;
    c = (short) (c + 5);
    System.out.println(c);

    byte __b = 127;
    System.out.println((byte) (__b + 2));

    long a = 2_000_000_000_000L;
    byte b = 20;
    int d = (int) (a + b);
    System.out.println(d);

    int i = 10;
    byte _b = (byte) (i + 5e2);
    System.out.println(_b);
  }

  static void character() {
    System.out.println("CHARACTERS\n--------------");
    System.out.println(Character.MIN_CODE_POINT);
    System.out.println(Character.MAX_CODE_POINT);

    char t = '\u20b9';
    System.out.println(t);

    int $y = 65;
    System.out.println((char) ($y));
    System.out.println((int) ($y));

    char a = (char) 1114111;
    System.out.println((char) (a + 66));
  }

  static void floating() {
    System.out.println("FLOATING\n--------------");
    System.out.println(Float.MAX_VALUE + 'E' + Float.MAX_EXPONENT);
    float f = 3.4028235E38f;
    System.out.println((float) (f * 1e31));
    System.out.println((double) (f * 1e31));
    System.out.println(Double.MAX_VALUE + 'E' + Double.MAX_EXPONENT);
    double d = 1.7976931348623157E308d;
    System.out.println((double) (d * 1e3));
  }

  public static void main(String[] args) {
    widening();
    narrowing();
    character();
    floating();
  }
}
