# 문제 자체는 쉬웠는데 변수명 실수로 시간 잡아먹음
# 이진수로 고치는 쉬운 방법 알게됨
# 벽 하나 뚫어서 최대 영역 찾는건 영역 별로 나눠주고 다른 영역을 만났을때 그 값을 더해서 최대값 표출

from sys import stdin
from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

dir = [] # 2진수 미리 변환
for i in range(16):
    dir.append(list(map(int, list(str(bin(i))[2:]))))
    dir[i] = [0]*(4-len(dir[i])) + dir[i]
    for j in range(4):
        dir[i][j] = True if dir[i][j]==1 else False

result_1=0
result_2=0
result_3=0

input = stdin.readline
m,n = map(int,input().rsplit())
temp = [[0]*m for i in range(n)]
for i in range(n):
    temp[i] = list(map(int,input().rsplit()))

gr = [[[False]*4 for i in range(m)]for i in range(n)]
area = [[-1]*m for i in range(n)]
result = []
answer = 0

for i in range(n):
    for j in range(m):
        gr[i][j]=dir[temp[i][j]]

c = 0
for i in range(n):
    for j in range(m):
        if area[i][j]!=-1:
            continue 
        area[i][j]=c
        q=deque()
        q.append((i,j))
        cnt=1
        while(q):
            x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if area[nx][ny]!=-1:
                    continue
                if gr[x][y][k]==True:
                    continue
                area[nx][ny]=c
                q.append((nx,ny))
                cnt+=1
        result.append(cnt)
        c+=1

for i in range(n):
    for j in range(m):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<=ni<n and 0<=nj<m:
                if area[i][j]!=area[ni][nj]:
                    result_3 = max(result_3,result[area[i][j]]+result[area[ni][nj]])

print(c)
print(max(result))
print(result_3)
