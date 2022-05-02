n = int(input())
for i in range(1, n+1):
    s = input().split()
    answer = ' '.join(s[::-1])
    print(f"Case #{i}: {answer}")