n, w, h, l = map(int, input().split())
answer = (w // l) * (h // l)
if n < answer:
    print(n)
else:
    print(answer)