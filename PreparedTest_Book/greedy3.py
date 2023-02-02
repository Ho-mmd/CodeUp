a, b = map(int, input().split());

ist = [[0 for i in range(b)] for i in range(a)];

for i in range(a):
    ist[i] = list(map(int, input().split()));
    ist[i].sort();

min = ist[0][0];

for i in range(b):
    if min < ist[i][0]:
        min = ist[i][0];

print(min);