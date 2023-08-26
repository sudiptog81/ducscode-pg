#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>

void f();
void sigcatch(int);

int main(void)
{
  int i, *ip;

  ip = (int *)f;
  for (i = 0; i < 20; i++)
  {
    signal(i, sigcatch);
  }

  *ip = i;

  printf("after assign to ip\n");
  f();
}

void f()
{
}

void sigcatch(int signum)
{
  printf("caught signal %d\n", signum);
  exit(1);
}
