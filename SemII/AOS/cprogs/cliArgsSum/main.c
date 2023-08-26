#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
  if (argc < 2)
  {
    printf("Usage: %s <num_1> <num_2> ... <num_N>\n", argv[0]);
    return 1;
  }

  int i, sum = 0;

  for (i = 1; i < argc; i++)
  {
    sum += atoi(argv[i]);
  }

  printf("Sum = %d\n", sum);

  return 0;
}
