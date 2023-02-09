N = int(input());
arr = [0] * 1001;

arr[1] = 1;
arr[2] = 3;

for i in range(3, N + 1):
    arr[i] = (arr[i - 2] * 2 + arr[i - 1]) % 796796;

print(arr[N]);