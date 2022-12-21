P = [
  [24/24,0,0,0],
  [12/24,12/24,0,0],
  [8/24,8/24,8/24,0],
  [6/24,6/24,6/24,6/24],
]

def comps(i, j):
  if i == 1:
    return 1
  if j == 1:
    return i - j
  return i - j + 1

_sum = 0
for i in range(2, 5):
  for j in range(1, i + 1):
    print("P(%d,%d) = %f, comps(%d,%d) = %f" % (i, j, P[i - 1][j - 1], i, j, comps(i, j)))
    _sum += P[i - 1][j - 1] * comps(i, j)

print("Average Number of Comparisons = %f" % _sum)
