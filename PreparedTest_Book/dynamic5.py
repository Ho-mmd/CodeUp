a, b = map(int, input().split());
c = [];
d = [10001] * 1001;
d[0] = 0;
flag = 0;

for i in range(a):
    c.append(int(input()));

for i in range(a):
    for j in range(c[i], b + 1):
        if d[j - c[i]] != 10001:
            if d[j] > d[j - c[i]] + 1:
                d[j] = d[j - c[i]] + 1;
                
if d[j] == 10001:
    print(-1);
else:
    print(d[j]);
