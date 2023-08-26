#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <time.h>

#define SHMKEY 75
#define K 1024

int shmid;

void print_shm_info(int shmid)
{
  struct shmid_ds shmid_ds;
  shmctl(shmid, IPC_STAT, &shmid_ds);

  printf("shm stat info:\n");
  printf("\tshm_segsz: %d\n", shmid_ds.shm_segsz);
  printf("\tshm_cpid: %d\n", shmid_ds.shm_cpid);
  printf("\tshm_lpid: %d\n", shmid_ds.shm_lpid);
  printf("\tshm_nattch: %d\n", shmid_ds.shm_nattch);
  printf("\tshm_atime: %s", ctime(&shmid_ds.shm_atime));
  printf("\tshm_dtime: %s", ctime(&shmid_ds.shm_dtime));
  printf("\tshm_ctime: %s", ctime(&shmid_ds.shm_ctime));
}

void cleanup(int signum)
{
  printf("server: received signal %d - bye!\n", signum);
  print_shm_info(shmid);
  shmctl(shmid, IPC_RMID, 0);
  exit(0);
}

int main(void)
{
  int *pint;
  char *addr1, *addr2;

  for (int i = 0; i < 64; i++)
  {
    signal(i, cleanup);
  }

  shmid = shmget(SHMKEY, 128 * K, 0777 | IPC_CREAT);

  printf("server running with pid %d\n", getpid());

  addr1 = (char *)shmat(shmid, 0, 0);
  addr2 = (char *)shmat(shmid, 0, 0);

  printf("addr1: 0x%x\n", addr1);
  printf("add21: 0x%x\n", addr2);

  pint = (int *)addr1;

  for (int i = 0; i < 256; i++)
  {
    *pint++ = i;
  }

  pint = (int *)addr1;
  *pint = 256;

  pint = (int *)addr2;
  for (int i = 0; i < 256; i++)
  {
    printf("%d\n", *pint++);
  }

  print_shm_info(shmid);

  shmdt(addr1);
  shmdt(addr2);

  pause();
}
