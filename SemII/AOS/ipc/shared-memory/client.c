#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

#define SHMKEY 75
#define K 1024

int shmid;

int main(void)
{
  int *pint;
  char *addr;

  printf("client running with pid %d\n", getpid());

  while ((shmid = shmget(SHMKEY, 64 * K, 0777)) < 0)
  {
    printf("client: shared memory not ready, waiting for signal...\n");
    sleep(1);
  }

  addr = (char *)shmat(shmid, 0, 0);
  pint = (int *)addr;

  while (*pint == 0)
  {
    printf("client: shared memory attached at address %x\n", addr);
    printf("client: server pid = %d\n", *pint);
    *pint = getpid();
    printf("client: pid of client = %d\n", *pint);
    printf("waiting for data from server...\n");
  };

  for (int i = 0; i < 256; i++)
  {
    printf("%d\n", pint[i]);
  }

  shmdt(addr);

  printf("client: received data from server, waiting for interrupt...\n");
  pause();
}
