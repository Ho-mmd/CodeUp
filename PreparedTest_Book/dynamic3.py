n = eval(input());

a = list(map(int, input().split()));
b = [0] * 100;

b[0] = a[0];

if a[0] > a[1]:
    b[1] = a[0];
else:
    b[1] = a[1];

for i in range(2, n):
    if b[i - 1] > b[i - 2] + a[i]:
        b[i] = b[i - 1];
    else:
        b[i] = b[i - 2] + a[i];

print(b[n - 1]);