# 연구소2 와 마찬가지로 바이러스 위치를 따와서 조합을 이용해 모든 경우의 수를 탐색
# 이 문제에서는 비활성되어있던 바이러스 위치가 활성화를 만나면 해당 위치가 활성화 된다는 점.
# 이를 통해 총 맞춰야할 전체 갯수를 +1 씩 해줘야함.

from itertools import combinations
from collections import deque
from sys import stdin

dx = [0,0,-1,1]
dy = [-1,1,0,0]
input = stdin.readline

n,m = map(int,input().rsplit())
gr = [[0]*n for i in range(n)]
temp = []
cnt = 0
for i in range(n):
    gr[i] = list(map(int,input().rsplit()))
    for j in range(n):
        if gr[i][j]==2:
            temp.append([i,j])
        if gr[i][j]==0:
            cnt+=1
        
com = list(combinations(temp,m))
result = int(1e9)


def bfs(paths):
    visited = [[-1]*n for i in range(n)]
    q = deque()
    t = 0
    c = 0
    for path in paths:
        q.append(path)
        visited[path[0]][path[1]]=0
    num = cnt
    while(q):
        x,y = q.popleft()
        if num==c:
            for i in range(n):
                t = max(max(visited[i]),t)
            return t
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue 
            if gr[nx][ny] == 1:
                continue
            if visited[nx][ny] != -1:
                continue
            if gr[nx][ny]==2:
                visited[nx][ny]=visited[x][y]+1
                c+=1
                num+=1
                q.append((nx,ny))
            if gr[nx][ny]==0:
                visited[nx][ny] = visited[x][y]+1
                c+=1
                q.append((nx,ny))
    return -1
    
for path in com:
    a = bfs(path)
    if a!=-1:
        result = min(result,a)

print(result if result!=int(1e9) else -1)
