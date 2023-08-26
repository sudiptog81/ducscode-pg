#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void displayResult(char, int, int);

int main(int argc, char **argv)
{
  // long long res;

  if (argc != 4)
  {
    printf("ERROR\n");
    return 1;
  }

  for (int i = 2; i < argc; i++)
  {
    res = atoi(argv[i]);
  }

  return 0;
}

void displayResult(char op, int x, int y)
{
  switch (op)
  {
  case '+':
    printf("Sum = %d\n", x + y);
    break;
  case '-':
    printf("Difference = %d\n", x - y);
    break;
  case '*':
    printf("Product = %d\n", x * y);
    break;
  case '/':
    printf("Quotient = %d\n", x / y);
    break;
  case '^':
    printf("Power = %d\n", (int)(pow(x, y)));
    break;
  case '%':
    printf("Remainder = %d\n", x % y);
    break;
  default:
    printf("Invalid Operator => %c\n", op);
  }
}
