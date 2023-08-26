import java.util.ArrayList;

/**
 * WAP to accept a bunch of numbers as CLI args and print their sum
 * 
 * Written by Sudipto Ghosh, University of Delhi.
 */

public class Main {
  public static void main(String[] args) {
    int sum = 0;
    ArrayList<Integer> numbers = new ArrayList<>();
    System.out.println(args);
    for (String string : args) {
      try {
        int number = Integer.parseInt(string);
        numbers.add(number);
        sum += number;
      } catch (NumberFormatException e) {
        System.out.println("Invalid number: " + string);
      }
    }

    System.out.println("Numbers: " + numbers);
    System.out.println("Sum: " + sum);
  }
}
