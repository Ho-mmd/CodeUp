import heapq
INF = int(1e9)

n, m = map(int, input().split());
graph = [[INF] * (n + 1) for i in range(n + 1)];
answer = 0;

for i in range(n + 1):
    for j in range(n + 1):
        if(i == j):
            graph[i][j] = 0;

for i in range(m):
    a, b = map(int, input().split());
    graph[a][b] = 1;
    graph[b][a] = 1;

x, k = map(int, input().split());

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            if(graph[i][j] > graph[i][k] + graph[k][j]):
                graph[i][j] = graph[i][k] + graph[k][j];
 

if(graph[1][k] == INF or graph[k][x] == INF):
    answer = -1;
else:
    answer = graph[1][k] + graph[k][x];    

print(answer);
