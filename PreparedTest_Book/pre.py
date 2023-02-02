from collections import deque

def dfs(graph, v, visited):
    visited[v] = 1;
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited);

def bfs (graph, start, visited):
    q = deque([start]);
    visited[start] = 1;
    while q:
        v = q.popleft();
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i);
                visited[i] = 1; 