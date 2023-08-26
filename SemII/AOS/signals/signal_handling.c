#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

void handler(int signum)
{
  printf("I: received signal (%d)\nI: exiting...\n", signum);
  exit(0);
}

int main(void)
{
  printf("I: pid=%d\n", getpid());
  signal(SIGINT, handler);
  signal(SIGALRM, handler);
  signal(SIGKILL, handler);
  signal(SIGTERM, handler);
  alarm(10);
  kill(0, SIGINT);
  pause();
}
