money = int(input())
change = 1000-money
coin = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coin:
    cnt += change//i
    change = change%i
    
print(cnt)