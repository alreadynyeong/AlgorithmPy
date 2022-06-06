a, b = input().split()

minN = int(a.replace('6', '5'))+int(b.replace('6', '5'))
maxN = int(a.replace('5', '6'))+int(b.replace('5', '6'))
print(minN, maxN)