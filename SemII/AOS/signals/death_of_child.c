#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>

int main(int argc, char **argv)
{
  int i, ret_val, ret_code;

  if (argc > 1)
  {
    signal(SIGCLD, SIG_IGN);
  }

  for (i = 0; i < 15; i++)
  {
    if (fork() == 0)
    {
      /* child proc here */
      printf("child proc %x\n", getpid());
      exit(i);
    }
  }

  ret_val = wait(&ret_code);
  printf("wait ret_val %x ret_code %x\n", ret_val, ret_code);
}
