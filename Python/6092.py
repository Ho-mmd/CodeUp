a = eval(input());
b = list(map(int, input().split()));
c = [0 for i in range(23)];

for i in b:
    c[i - 1] += 1;

for j in c:
    print(j, end = " ");
