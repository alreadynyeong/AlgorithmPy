sunn = 0
for _ in range(5):
    a = int(input())
    sunn = sunn + (a if a>=40 else 40)
print(sunn//5)