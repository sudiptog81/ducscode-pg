#include <bits/stdc++.h>

using namespace std;

struct Job {
  int s;
  int f;
};

inline bool operator<(const struct Job& lhs, const struct Job& rhs)
{
  return lhs.f < rhs.f;
}

int main(void)
{
  int fj = 0;

  set<struct Job> B;

  B.insert({0, 6});
  B.insert({1, 4});
  B.insert({3, 5});
  B.insert({3, 8});
  B.insert({4, 7});
  B.insert({5, 9});
  B.insert({6, 10});
  B.insert({8, 11});

  cout << "Set of Jobs:" << endl;
  for (auto j : B)
    cout << j.s << "-" << j.f << endl;

  set<struct Job> A;

  for (auto job : B)
  {
    if (job.s >= fj)
    {
      A.insert(job);
      fj = job.f;
    }
  }

  cout << "Set of Selected Jobs:" << endl;
  for (auto j : A)
    cout << j.s << "-" << j.f << endl;

  return 0;
}
