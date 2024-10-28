n, m = int(input()), int(input())
count = 0
if m <= m:
    for i in range(n, m+1):
        if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
            count += 1
print(count)