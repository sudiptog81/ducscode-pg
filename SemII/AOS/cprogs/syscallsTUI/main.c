#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>
#define BUF_SIZE 1024
#define PATH_SIZE 256

void clrscr();
void getch();
void handleMenu(int);

char buf[BUF_SIZE];

void clrbuff()
{
  for (int i = 0; i < BUF_SIZE; i++)
    buf[i] = '\0';
}

void readFile(char path[PATH_SIZE])
{
  int fd = open(path, O_RDONLY);

  if (fd == -1)
  {
    printf("Error: File not found!\n");
    return;
  }

  printf("File: %s\n", path);
  while (read(fd, buf, sizeof(buf)) > 0)
  {
    printf("%s\n", buf);
    clrbuff();
  }

  clrbuff();
  close(fd);
}

void readFileOffset(char path[PATH_SIZE], int start, int nBytes)
{
  int fd = open(path, O_RDONLY);

  if (fd == -1)
  {
    printf("Error: File not found!\n");
    return;
  }

  lseek(fd, start, SEEK_SET);

  printf("File: %s\n", path);
  read(fd, buf, nBytes);

  printf("%s", buf);

  clrbuff();
  close(fd);
}

void createFile(char path[PATH_SIZE], mode_t mode)
{
  umask(0000);

  int fd = creat(path, (mode_t)(mode));

  if (fd == -1)
  {
    printf("Error in creating file!!\n");
    return;
  }

  printf("Created File: %s\n", path);

  close(fd);
}

void writeFile(const char *path)
{
  int fd = open(path, O_WRONLY);

  if (fd == -1)
  {
    printf("Error: File not found!\n");
    return;
  }

  struct stat st;
  stat(path, &st);

  if (st.st_size > 0)
  {
    int choice;
    printf("File already has content! Do you want to overwrite? (0/1) ");
    scanf("%d", &choice);
    if (choice == 0)
      return;
  }

  close(fd);

  fd = open(path, O_WRONLY | O_TRUNC);

  int b = write(fd, buf, strlen(buf));

  clrbuff();
  printf("%d bytes written to file: %s\n", b, path);
  close(fd);
}

void writeFileOffset(char path[PATH_SIZE], int start)
{
  int fd = open(path, O_WRONLY);

  if (fd == -1)
  {
    printf("Error: File not found!\n");
    return;
  }

  struct stat st;
  stat(path, &st);

  if (st.st_size > 0)
  {
    int choice;
    printf("File already has content! Do you want to overwrite? (0/1) ");
    scanf("%d", &choice);
    if (choice == 0)
      return;
  }

  int b = write(fd, buf, strlen(buf));

  clrbuff();
  printf("%d bytes written to file: %s\n", b, path);
  close(fd);
}

void copyFile(char src[PATH_SIZE], char dest[PATH_SIZE])
{
  if (strcmp(src, dest) == 0)
  {
    printf("Error: Source and Destination cannot be same!\n");
    return;
  }

  int fd1 = open(src, O_RDONLY);
  if (fd1 == -1)
  {
    printf("Error: Source file not found!\n");
    return;
  }

  int fd2 = open(dest, O_WRONLY);
  if (fd2 == -1)
  {
    printf("Warning: Destination file not found! Create? (0/1) ");
    int choice;
    scanf("%d", &choice);
    if (choice == 0)
      return;
    else
    {
      createFile(dest, 0666);
      fd2 = open(dest, O_WRONLY);
    }
  }

  struct stat st;
  stat(dest, &st);

  if (st.st_size > 0)
  {
    int choice;
    printf("Destination file already has content! Do you want to overwrite? (0/1) ");
    scanf("%d", &choice);
    if (choice == 0)
      return;
  }

  int b = 0;
  while (read(fd1, buf, sizeof(buf)) > 0)
  {
    b += write(fd2, buf, strlen(buf));
    clrbuff();
  }

  clrbuff();
  printf("%d bytes copied from %s to %s\n", b, src, dest);

  close(fd1);
  close(fd2);
}

int main()
{
  int choice = 0;

  do
  {
    clrscr();

    printf("=========== MENU ============\n");
    printf(" 1. Read a File\n");
    printf(" 2. Read Y bytes from a File starting from X\n");
    printf(" 3. Create a File\n");
    printf(" 4. Write to File\n");
    printf(" 5. Write to File from Position X\n");
    printf(" 6. Copy File\n");
    printf(" 8. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    handleMenu(choice);

    getch();
  } while (choice != 8);

  return 0;
}

void handleMenu(int choice)
{
  int t;
  unsigned int temp;
  unsigned int mode;
  unsigned int start, nBytes;
  char *path[PATH_SIZE];

  clrbuff();

  switch (choice)
  {
  case 1:
    printf("Path: ");
    scanf("%s", &path);
    readFile(path);
    break;
  case 2:
    printf("Path: ");
    scanf("%s", &path);
    printf("Starting Position: ");
    scanf("%d", &start);
    printf("Number of Bytes: ");
    scanf("%d", &nBytes);
    readFileOffset(path, start, nBytes);
    break;
  case 3:
    printf("Path: ");
    scanf("%s", &path);
    printf("Permissions:\n");

    mode = 0;

    printf("\tOwner:\n");
    printf("\t\tread: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IRUSR;
    printf("\t\twrite: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IWUSR;
    printf("\t\texecute: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IXUSR;

    printf("\tGroup:\n");
    printf("\t\tread: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IRGRP;
    printf("\t\twrite: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IWGRP;
    printf("\t\texecute: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IXGRP;

    printf("\tOthers:\n");
    printf("\t\tread: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IROTH;
    printf("\t\twrite: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IWOTH;
    printf("\t\texecute: ");
    scanf("%d", &t);
    if (t == 1)
      mode |= S_IXOTH;

    createFile(path, mode);
    break;
  case 4:
    printf("Path: ");
    scanf("%s", &path);
    printf("Content: \n");
    scanf("%s", &buf);
    writeFile(path);
    break;
  case 5:
    printf("Path: ");
    scanf("%s", &path);
    printf("Starting Position: ");
    scanf("%d", &start);
    printf("Content: \n");
    while (scanf("%s", buf) == 1)
      printf("%s\n", buf);
    writeFileOffset(path, start);
    break;
  case 6:
    printf("Source Path: ");
    scanf("%s", &path);
    printf("Destination Path: ");
    scanf("%s", &buf);
    copyFile(path, buf);
    break;
  case 8:
    printf("Exiting...\n");
    break;
  default:
    break;
  }
}

void clrscr()
{
#ifdef _WIN32
  system("cls");
#elif __unix__
  system("clear");
#endif
  return;
}

void getch()
{
  char ch;
  printf("Press Enter to continue ... ");
  // scanf("%c", &ch);
  getchar();
  return;
}
