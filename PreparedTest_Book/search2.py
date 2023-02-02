from collections import deque

N, M = map(int, input().split());

mp = [[] for i in range(N)];

for i in range(N):
    mp[i] = list(map(int, input().split()));

def bfs(i, j):
    q = deque();
    q.append((i, j));
    while q:
        i, j = q.popleft();

        n_i = i + 1;
        n_j = j;
        if n_i < 0 or n_i >= N or n_j < 0 or n_j >= M:
            continue;
        if mp[n_i][n_j] == 1:
            mp[n_i][n_j] = mp[i][j] + 1;
            q.append((n_i, n_j)); 
        n_i = i - 1;
        n_j = j;

        if n_i < 0 or n_i >= N or n_j < 0 or n_j >= M:
            continue;
        if mp[n_i][n_j] == 1:
            mp[n_i][n_j] = mp[i][j] + 1;
            q.append((n_i, n_j)); 
        n_i = i;
        n_j = j + 1;

        if n_i < 0 or n_i >= N or n_j < 0 or n_j >= M:
            continue;
        if mp[n_i][n_j] == 1:
            mp[n_i][n_j] = mp[i][j] + 1;
            q.append((n_i, n_j)); 
        n_i = i;
        n_j = j - 1;
        
        if n_i < 0 or n_i >= N or n_j < 0 or n_j >= M:
            continue;
        if mp[n_i][n_j] == 1:
            mp[n_i][n_j] = mp[i][j] + 1;
            q.append((n_i, n_j)); 

    return mp[i - 1][j - 1];

print(bfs(0, 0));