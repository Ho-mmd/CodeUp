N, M = map(int, input().split());
arr = [];
answer = 0;

for i in range(N):
    arr.append(list(map(int, input().split())));

def dfs(arr, n, m, N, M):
    arr[n][m] = 2;
    if(n + 1 < N):
        if(arr[n + 1][m] == 0):
            dfs(arr, n + 1, m, N, M);
    if(n - 1 >= 0):
        if(arr[n - 1][m] == 0):
            dfs(arr, n - 1, m, N, M);
    if(m + 1 < M):
        if(arr[n][m + 1] == 0):
            dfs(arr, n, m + 1, N, M);
    if(m - 1 >= 0):
        if(arr[n][m - 1] == 0):
            dfs(arr, n, m - 1, N, M);


for i in range(N):
    for j in range(M):
        if(arr[i][j] == 0):
            dfs(arr, i, j, N, M);
            answer += 1;

print(answer);