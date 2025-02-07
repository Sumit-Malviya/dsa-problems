from math import sqrt

n = 4
ans = 0
for i in range(1, n + 1):
    func = 0
    for j in range(1, int(sqrt(i)) + 1):
        if i % j == 0:
            func = func + j
            if i // j != j:
                func = func + (i // j)
    ans = ans + func
print(ans)
