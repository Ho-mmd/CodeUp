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
        for k in range(4):
            