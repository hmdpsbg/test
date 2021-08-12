n = int(input())
m = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = []
for i, j in zip(a, b):
    c.append((i, j))
s1 = sorted(c, key=lambda x:x[0], reverse = True)
s2 = sorted(s1, key=lambda x:x[1], reverse = True)

s1 = s1[:m]
_max = 0

for i in s2:
    if not i in s1:
        s2.remove(s1)

for i in range(m):
    flag = 1
    for j in range(len(s2)):
        if s2[j] in s1:
            _max += s2[j][0] - s2[j][1] * i
            s2.pop(j)
            flag = 0
            break
    if flag:
        _max += s1[i][0] - s1[i][1] * i
    print(_max)
print(_max)