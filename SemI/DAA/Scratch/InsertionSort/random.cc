#include <bits/stdc++.h>

using namespace std;
ofstream fout("random.csv");

const int SIZE = 3;

int totComp = 0;
int numPerm = 0;

int insert(int *A, int i)
{
  int comp = 0;

  int j = i - 1;
  int key = A[i];

  while (j >= 0)
  {
    comp++;
    if (A[j] > key)
    {
      A[j + 1] = A[j];
      j--;
    }
    else
    {
      break;
    }
  }

  A[j + 1] = key;

  fout << j + 2 << ",";
  cout << "\t\tinserted " << key << " at j = " << j + 2 << endl;

  return comp;
}

int insertionSort(int *A, int n)
{
  int iterComp, totComp = 0;
  int C[SIZE];
  for (int i = 0; i < n; i++)
  {
    C[i] = A[i];
  }
  for (int i = 1; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      fout << C[j];
      if (j != 2)
        fout << " ";
    }
    cout << "\tfor i = " << i + 1 << ", " << endl;
    fout << "," << i + 1 << ",";
    iterComp = insert(A, i);
    cout << "\t\tcomparisons: " << iterComp << endl;
    fout << iterComp << "\n";
    totComp += iterComp;
  }

  cout << "\ttotal comparisons: " << totComp << endl;

  return totComp;
}

void print(int *A, int n)
{
  for (int i = 0; i < n; i++)
  {
    cout << A[i];
    if (i != SIZE)
      cout << " ";
  }
  cout << endl;
}

/**
 * Generates all permutations of an array and sort them using insertion sort
 * Input: set of numbers A, size of array n
 */
void generatePermutationsAndSort(int *A, int n)
{
  if (n == 1)
  {
    int B[SIZE];
    cout << "permutation " << ++numPerm << ": ";
    print(A, SIZE);
    for (int i = 0; i < SIZE; i++)
    {
      B[i] = A[i];
    }
    totComp += insertionSort(B, SIZE);
    cout << "sorted: ";
    print(B, SIZE);
    cout << "------------------------" << endl;
    return;
  }

  for (int i = 0; i < n; i++)
  {
    swap(A[i], A[n - 1]);
    generatePermutationsAndSort(A, n - 1);
    swap(A[i], A[n - 1]);
  }
}

int main(void)
{
  srand(time(0));

  int B[SIZE];
  for (int i = 0; i < SIZE; i++)
  {
    B[i] = rand() % 10 + 1;
  }
  fout << "permutation,i,j,comparisons\n";
  generatePermutationsAndSort(B, SIZE);
  cout << "Average Number of Comparisons Done: " << totComp << endl;
}
