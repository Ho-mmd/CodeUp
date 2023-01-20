a = [[0 for i in range(10)] for j in range(10)];

for i in range(10):
    a[i] = list(map(int, input().split()));

x, y = 2, 2;
a[1][1] = 9;

while (1):
    if a[x - 1][y] == 1 and a[x][y - 1] == 1:
        break;
    else:
        if a[x - 1][y] == 0 or a[x - 1][y] == 2:
            if a[x - 1][y] == 2:
                a[x - 1][y] = 9;
                break;
            a[x - 1][y] = 9;
            y += 1;
        elif a[x][y - 1] == 0 or a[x][y - 1] == 2:
            if a[x][y - 1] == 2:
                a[x][y - 1] = 9;
                break;
            a[x][y - 1] = 9;    
            x += 1;

for i in range(10):
    for j in range(10):
        print(a[i][j], end = " ");
    print();