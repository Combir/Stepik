a = int(input())
a1 = int(input())
a2 = int(input())
min_, max_ = min(a, a1, a2), max(a, a1, a2)
summ_ = (a + a1 + a2) - min_ - max_
print(max_, summ_, min_, sep = "\n") # end = "\n"