n = int(input())
stuList = list(map(int, input().split()))
team = []

for i in range(n):
    team.append(max(stuList)+min(stuList))
    stuList.remove(max(stuList))
    stuList.remove(min(stuList))

print(min(team))