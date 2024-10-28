a = input()
min_ = min(int(a[0]), int(a[1]), int(a[2]))
max_ = max(int(a[0]), int(a[1]), int(a[2]))
per = 0
if min_ < int(a[0]) < max_:
    per = int(a[0])
if min_ < int(a[1]) < max_:
    per = int(a[1])
if min_ < int(a[2]) < max_:
    per = int(a[2])
if max_ - min_ == per:
    print("Число интересное")
else:
    print("Число неинтересное")