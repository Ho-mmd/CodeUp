from collections import deque

def dfs(graph, v, visited):
    visited[v] = 1; #노드 방문 표시
    for i in graph[v]: #방문 노드와 연결된 노드 중
        if visited[i] == 0: #방문 안 한 노드 있으면
            dfs(graph, i , visited); #재귀 start

def bfs(graph, start, visited):
    queue = deque([start]); #queue 만들어서 시작점 삽입
    visited[start] = 1; #방문 노드 표시
    while queue: #queue가 빌 때까지
        v = queue.popleft() #요소 out
        for i in graph[v]: #연결된 노드 중
            if visited[i] == 0: #방문 안 했으면
                queue.append(i); #queue에 삽입하고
                visited[i] = 1; #방문 표시
