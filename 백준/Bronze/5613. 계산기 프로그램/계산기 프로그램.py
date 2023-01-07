ans = int(input())
while True:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+': ans += n;
    elif op == '-': ans -= n;
    elif op == '*': ans *= n;
    elif op == '/': ans //= n;
print(ans)