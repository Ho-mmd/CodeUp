h, w = map(int, input().split());

a = [[0 for i in range(w)] for j in range(h)];

n = eval(input());

for i in range(n):
    l, d, x, y = map(int, input().split());
    if d == 0:
        for j in range(l):
            a[x - 1][y - 1] = 1;
            y += 1;
    else:
        for j in range(l):
            a[x - 1][y - 1] = 1;
            x += 1;

for i in range(h):
    for j in range(w):
        print(a[i][j], end = " ");
    print();