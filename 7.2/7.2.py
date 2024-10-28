m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)

if m > n:
    for j in range(m, n-1, -1):
        print(j)

if m == n:
    print(m)