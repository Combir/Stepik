g1, g2, g3 = input(), input(), input()
c1, c2, c3 = len(g1), len(g2), len(g3)
s = [c1, c2, c3]
min_ = min(s)
max_ = max(s)
if c1 == min_:
    print(g1)
if c2 == min_:
    print(g2)
if c3 == min_:
    print(g3)
if c1 == max_:
    print(g1)
if c2 == max_:
    print(g2)
if c3 == max_:
    print(g3)