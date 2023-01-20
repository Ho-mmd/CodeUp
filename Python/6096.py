a = [[0 for i in range(19)] for i in range(19)];

for i in range(19):
    a[i] = list(map(int, input().split()));

b = eval(input());

for i in range(b):
    x, y = map(int, input().split());
    for j in range(19):
        for k in range(19):
            if j == (x - 1) and k == (y - 1):
                continue;
            elif j == (x - 1) or k == (y - 1):
                if a[j][k] == 0:
                    a[j][k] = 1;
                else:
                    a[j][k] = 0;

for i in range(19):
    if i != 0:
        print();
    for j in range(19):
        print(a[i][j], end = " ");

