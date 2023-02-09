
def dfs(arr, visited, v):
    visited[v] = 1;
    
    for i in arr[v]:
        if(visited[i] == 0):
            dfs(arr, visited, i);

def bfs(ar, visit, v):
    visit[v] = 1;
    tm = [];
    tm.append(v);
    while ar:
        tmp = ar.pop(0);
        for i in tmp:
            if(visit[i] == 0):
                visit[i] = 1;
                ar.append(i);