N, M = map(int, input().split());
arr = [];
answer = [10001] * 101;

for i in range(N):
    arr.append(int(input()));

answer[0] = 0;

for i in arr:
    for j in range(i, M + 1):
        if(answer[j - i] != 10001):
            if(answer[j] > answer[j - i] + 1):
                answer[j] = answer[j - i] + 1;

if(answer[M] == 10001):
    print(-1);
else:
    print(answer[M]);