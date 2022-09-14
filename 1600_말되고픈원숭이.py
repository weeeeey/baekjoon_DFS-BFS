# 나이트가 될 수 있는 횟수에 따라 방문 체크를 하면 됐는데 말로 이동했냐 그냥 이동했냐로 체크해서 중복을 못 넘겼음


from collections import deque
from sys import stdin

input = stdin.readline
knight = [[-2,-1],[-1,-2],[-2,1],[-1,2],[2,-1],[1,-2],[2,1],[1,2]]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer = -1
k = int(input())
m,n = map(int,input().rsplit())
gr = [[0]*m for i in range(n)]
visited = [[[-1]*(k+1) for j in range(m)] for i in range(n)]
for i in range(n):
    gr[i] = list(map(int,input().rsplit()))
q = deque()
q.append((0,0,0)) #x,y,k,이전 이동방법
visited[0][0][0] = 0 
while(q):
    x,y,cnt = q.popleft()
    if [x,y]==[n-1,m-1]:
        answer = visited[x][y][cnt]
        break
    if cnt<k:
        for i in range(8):
            nx = x + knight[i][0]
            ny = y + knight[i][1]
            if 0<=nx<n and 0<=ny<m:
                if gr[nx][ny]==1:
                    continue
                if visited[nx][ny][cnt+1]==-1:
                    visited[nx][ny][cnt+1] = visited[x][y][cnt]+1
                    q.append((nx,ny,cnt+1))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if gr[nx][ny]==1:
                continue
            if visited[nx][ny][cnt]==-1:
                visited[nx][ny][cnt] = visited[x][y][cnt]+1
                q.append((nx,ny,cnt))
print(answer)
# 1
# 4 5
# 0 0 1 1
# 0 0 1 1
# 0 0 1 1
# 0 0 1 1
# 1 1 0 0
