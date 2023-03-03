def dfs(graph, v, visited):
    visited[v] = 1;

    for i in graph[v]:
        if (visited[i] != 1):
            dfs(graph, i, visited);

q = [];

def bfs(graph, v, visit):
    visit[v] = 1;
    q.append(v);

    while q:
        tmp = q.pop(0);
        for i in graph[tmp]:
            if(visit[i] != 1):
                visit[i] = 1;
                q.append(i);