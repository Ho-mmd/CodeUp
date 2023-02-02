def bin(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2;
        if arr[mid] == target:
            return mid;
        elif arr[mid] < target:
            start = mid + 1;
        else:
            end = mid - 1;
    return;

a = int(input());
b = list(map(int, input().split()));
c = int(input());
d = list(map(int, input().split()));

b.sort();

for i in range(c):
    if bin(b, d[i], 0, a - 1):
        print("yes", end = " ");
    else:
        print("no", end = " ");