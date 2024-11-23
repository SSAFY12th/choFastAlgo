import sys
dx = [-1,0,1,0]
dy = [0,1,0,-1]



n,m = map(int,input().split())


board = [[0] * (m+1) for _ in range(n+1) ]
INT_MAX = sys.maxsize
MAX_G = 2500

for i in range(1,n+1):
    raw = [0]+ list(map(int,input().split()))
    
    for j in range(1,m+1):
        board[i][j] = raw[j]

node = 0
renum = [[0] * (m+1) for _ in range(n+1)]

graph = [[0] * (MAX_G+ 1) for _ in range(MAX_G + 1)]


# 각 정점을 노드로 표현 해야함, 노드의 갯수도 새야함 
for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            node += 1
            renum[i][j] = node


for i in range(1,node+1):
    for j in range(1,node+1):
        graph[i][j] =  INT_MAX



for i in range(1, n+1):
    for j in range(1, m+1):

        if board[i][j] == 1:
            for k in range(4):
                cnt = 1

                while True:
                    nx = i + dx[k] * cnt
                    ny = j + dy[k] * cnt

                    if nx < 1 or ny < 1 or nx > n or ny > m:
                        break

                    if board[nx][ny] == 1:
                        graph[renum[i][j]][renum[nx][ny]] = cnt - 1
                        break
                    
                    cnt +=1


vis = [False] * (node+1)
dist = [INT_MAX] * (node+1)
dist[1]= 0
# 프림 



ans = 0
for i in range(1,node+1):
    min_idx = -1
    for j in range(1,node+1):
        if vis[j]: 
             continue

        if min_idx == -1 or dist[min_idx] > dist[j]:
            min_idx = j
        
    # 방문 처리 
    vis[min_idx] = True
    # ans 더하기
    ans += dist[min_idx]

    # 만약에 다음에 연결할 노드가 없으면 종료  pass
    if dist[min_idx] == INT_MAX:
        ans = -1
        break



    for j in range(1,node+1):
        # if board[min_idx][j] == 0:
        #     continue
        
        dist[j] = min(graph[min_idx][j],dist[j])

print(ans)