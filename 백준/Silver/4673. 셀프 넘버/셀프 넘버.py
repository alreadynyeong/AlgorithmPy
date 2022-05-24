num = set(range(1, 10001))
num_list = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num_list.add(i)

self_num = sorted(num - num_list)
for i in self_num:
    print(i)