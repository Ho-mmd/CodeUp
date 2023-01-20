a = eval(input());
b = [[0 for i in range(19)] for j in range(19)];

for k in range(a):
    x, y = map(int, input().split());
    b[x - 1][y - 1] = 1;

for i in range(19):
    if i != 0:
        print("");
    for j in range(19):
        print(b[i][j], end = " ");