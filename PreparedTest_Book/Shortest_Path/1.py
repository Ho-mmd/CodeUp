#Djikstra
import heapq
INF = int(1e9)

n, m = map(int, input().split());
start = int(input());
graph = [[] for i in range(n + 1)];
distance = [INF] * (n + 1);

for i in range(n + 1):
    a, b, c = map(int, input().split());
    graph[a].append((b, c));

for i in range(m):
    q = [];
    heapq.heappush(q, (0, start));
    distance[start] = 0;

    while q:
        dist, now = heapq.heappop(q);
        if(distance[now] < dist):
            continue;
        for i in graph[now]:
            cost = dist + i[1];
        if (cost < distance[i[0]]):
            distance[i[0]] = cost;
            heapq.heappush(q, (cost, i[0]));


#Floyd
n, m = map(int, input().split());
graph = [[INF] * (n + 1) for i in range(n + 1)];

for i in range(n + 1):
    for j in range(n + 1):
        if(i == j):
            graph[i][j] = 0;

for i in range(m):
    a, b, c = map(int, input().split());
    graph[a][b] = c;

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            if(graph[i][j] > graph[i][k] + graph[k][j]):
                graph[i][j] = graph[i][k] + graph[k][j];