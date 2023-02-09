N, M = map(int, input().split());
arr = [];
answer = 0;

for i in range(N):
    arr.append(list(map(int, input().split())));

def bfs(arr, a, b, an):
    arr[a][b] = 2;
    tmp = [];
    tmp.append([a, b, an]);

    while tmp:
        tp = tmp.pop(0);
        if(tp[0] == N - 1 and tp[1] == M - 1):
            return tp[2] + 1;
 
        if(tp[0] + 1 < N):
            if(arr[tp[0] + 1][tp[1]] == 1):
                arr[tp[0] + 1][tp[1]] = 2;
                tmp.append([tp[0] + 1, tp[1], tp[2] + 1]);
        if(tp[0] - 1 >= 0):
            if(arr[tp[0] - 1][tp[1]] == 1):
                arr[tp[0] - 1][tp[1]] = 2;
                tmp.append([tp[0] - 1, tp[1], tp[2] + 1]);
        if(tp[1] + 1 < M):
            if(arr[tp[0]][tp[1] + 1] == 1):
                arr[tp[0]][tp[1] + 1] = 2;
                tmp.append([tp[0], tp[1] + 1, tp[2] + 1]);
        if(tp[1] - 1 >= 0):
            if(arr[tp[0]][tp[1] - 1] == 1):
                arr[tp[0]][tp[1] - 1] = 2;
                tmp.append([tp[0], tp[1] - 1, tp[2] + 1]);


answer = bfs(arr, 0, 0, answer);

print(answer);