N = int(input());
arr = list(map(int, input().split()));

answer = [0] * 101;

answer[0] = arr[0];
if(arr[1] > arr[0]):
    answer[1] = arr[1];
else:
    answer[1] = arr[0];
if(arr[1] > arr[2] + arr[0]):
    answer[2] = arr[1];
else:
    answer[2] = arr[2] + arr[0];

for i in range(3, N):
    answer[i] = answer[i - 2] + arr[i];
    if(answer[i - 1] > answer[i]):
        answer[i] = answer[i - 1];

print(answer[N - 1]);