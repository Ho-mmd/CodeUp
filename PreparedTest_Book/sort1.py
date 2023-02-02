a = eval(input());
b = [];

for i in range(a):
    b.append(eval(input()));

b.sort(reverse = True);

for i in b:
    print(i, end = " ");