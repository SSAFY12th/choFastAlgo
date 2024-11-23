import sys
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]

m_size = sys.maxsize


graph = [[0]* (n+1) for _ in range(n+1)] # 인접 행렬을 나타내기 위해서 2차원으로 준다. 
vis = [False]  * (n+1) # 해당 노드 방문 여부 
dist = [m_size] * (n+1)  # 가중치  처음 가중치는 무한으로 두거나 가중치의 끝값을 둔다.


# 인접 행렬 구현
for x,y,z in board:
    graph[x][y] = z
    graph[y][x] = z


dist[1] = 0 # 아무 정점 0으로 두기


ans = 0  # 결과 값 저장 

# OV^2 a프림 구현
for i in range(1,n+1):
    min_idx = -1

    # 해당 노드에서 다음 노드를 돌아다니며 가장 작은 가중치 초기화
    for j in range(1, n+1):
        if vis[j]:
            continue

        if ( min_idx == -1 or dist[min_idx] > dist[j]):
            min_idx = j
    
    vis[min_idx] = True # 방문 처리 해주고
    ans += dist[min_idx] # ans 추가

    for j in range(1,n+1):
        # 방문했으면 넘어가기
        if graph[min_idx][j] == 0:
            continue
        
        dist[j] = min(graph[min_idx][j], dist[j])

print(ans)
        
"""
전체 코드 흐름 요약
입력 처리: 간선 정보로 인접 행렬 생성.
MST 초기화: 방문 여부(vis), 최소 가중치(dist) 초기화.
프림 알고리즘:
MST에 포함되지 않은 노드 중 최소 가중치의 노드 선택.
선택된 노드를 MST에 추가하고 가중치 갱신.
최종 출력: MST의 총 가중치를 출력
"""




