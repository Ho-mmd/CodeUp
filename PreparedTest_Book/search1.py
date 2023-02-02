N, M = map(int, input().split());
pot = [[] for i in range(N)];

cnt = 0;

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return 0;
    if pot[i][j] == 0:
        pot[i][j] = 1;
        dfs(i + 1, j);
        dfs(i - 1, j);
        dfs(i, j + 1);
        dfs(i, j - 1);
        return 1;
    return 0;
    
for i in range(N):
    pot[i] = list(map(int, input().split()));

for i in range(N):
    for j in range(M):
            flag = dfs(i, j);
            if flag == 1:
                cnt += 1;

print(cnt);