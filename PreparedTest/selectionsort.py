a = [4, 3, 7, 1, 6];
n = len(a);

for i in range(n):
    min = i;
    for j in range(i + 1, n):
        if a[j] < a[min]:
            min = j;
    tmp = a[i];
    a[i] = a[min];
    a[min] = tmp;

print(a);