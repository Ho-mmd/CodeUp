N, M = map(int, input().split());
arr = []
answer = 0;

for i in range(N):
    arr.append(list(map(int, input().split())));
    if(answer < min(arr[i])):
        answer = min(arr[i]);

print(answer);