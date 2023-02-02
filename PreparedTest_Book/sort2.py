a = eval(input());
b = [];

for i in range(2):
    data = input().split();
    b.append((data[0], int(data[1])));

b = sorted(b, key = lambda x : x[1]);

for i in b:
    print(i[0], end = " ");