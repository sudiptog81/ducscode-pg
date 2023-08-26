#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <sys/times.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

void handler(int signo)
{
  printf("\ncaught interrupt...\n");
}

int main(void)
{
  struct tms tmsbuf, tmsbuf2;
  pid_t pid;
  clock_t start, end;

  signal(SIGINT, handler);

  start = times(&tmsbuf);

  printf("start: %s", ctime(&start));
  printf("tms_utime: %ld\n", tmsbuf.tms_utime);
  printf("tms_stime: %ld\n", tmsbuf.tms_stime);
  printf("tms_cutime: %ld\n", tmsbuf.tms_cutime);
  printf("tms_cstime: %ld\n", tmsbuf.tms_cstime);

  for (int i = 0; i < 15; i++)
  {
    if ((pid = fork()) == 0)
    {
      printf("child %d counting...\n", getpid());
      for (long long i = 0; i < 1e10; i++)
        ;
      printf("child %d done...\n", getpid());
      end = times(&tmsbuf2);
      printf("child %d end: %ld\n", getpid(), end - start);
      printf("tms_utime: %ld\n", tmsbuf2.tms_utime - tmsbuf.tms_utime);
      printf("tms_stime: %ld\n", tmsbuf2.tms_stime - tmsbuf.tms_stime);
      exit(0);
    }
  }

  for (int i = 0; i < 15; i++)
    wait(NULL);

  printf("parent counting...\n");

  for (long long i = 0; i < 1e10; i++)
    ;

  printf("parent done...\n");

  end = times(&tmsbuf2);
  printf("end: %ld\n", end - start);
  printf("tms_utime: %ld\n", tmsbuf2.tms_utime - tmsbuf.tms_utime);
  printf("tms_stime: %ld\n", tmsbuf2.tms_stime - tmsbuf.tms_stime);
  printf("tms_cutime: %ld\n", tmsbuf2.tms_cutime - tmsbuf.tms_cutime);
  printf("tms_cstime: %ld\n", tmsbuf2.tms_cstime - tmsbuf.tms_cstime);
}
