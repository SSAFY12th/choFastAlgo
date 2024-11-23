import sys
n,m = (map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(m)]

mx = sys.maxsize
graph = [[0] * (n+1) for _ in range(n+1)] 
vis = [False] * (n+1)
dist = [mx] * (n+1)


for x,y,z in board:
    graph[x][y] = z
    graph[y][x] = z


res = 0

dist[1] = 0

for i in range(1,n+1):
    min_idx = -1

    for j in range(1, n+1):
        if vis[j]:
            continue

        if min_idx == -1 or dist[min_idx] > dist[j]:
            min_idx = j

    vis[min_idx] = True
    res += dist[min_idx]

    for j in range(1,n+1):
        if graph[min_idx][j] == 0:
            continue
        
        dist[j] = min(graph[min_idx][j], dist[j])

print(res)

    
    







