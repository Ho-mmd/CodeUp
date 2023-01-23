#Left Shift

a = [3, 2, 1, 5, 7];
n = len(a);

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            tmp = a[j];
            a[j] = a[j - 1];
            a[j - 1] = tmp;

print(a);