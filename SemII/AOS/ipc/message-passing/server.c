#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/types.h>

#define MSGKEY 75

struct msgform
{
  long mtype;
  char mtext[256];
} msg;

int msgid;

void cleanup(int signum)
{
  msgctl(msgid, IPC_RMID, 0);
  printf("server: received signal %d - bye!\n", signum);
  exit(0);
}

int main(void)
{
  int pid, *pint;

  for (int i = 0; i < 64; i++)
  {
    signal(i, cleanup);
  }

  msgid = msgget(MSGKEY, 0777 | IPC_CREAT);

  printf("server running with pid %d\n", getpid());

  for (;;)
  {
    msgrcv(msgid, &msg, 256, 1, 0);
    pint = (int *)msg.mtext;
    pid = *pint;
    printf("server: receive from pid %d\n", pid);
    msg.mtype = pid;
    *pint = getpid();
    msgsnd(msgid, &msg, sizeof(int), 0);
  }
}
