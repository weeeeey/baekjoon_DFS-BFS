'''
처음에는 큐에 단순하게 rot를 넣어서 변환 횟수를 샜다.
이럴 경우 동일 경로인데 변환 횟수가 더 적은 로직은 지나치게 됨( visit가 단순하게 True False 가 되기 떄문에)

visit 그래프를 변환 횟수를 입력 시켜줌.
그런데 이전 좌표 visit에 +1 시켜줄 경우 우리가 알고 있는것은 nextNUM 이므로 로직이 꼬이게 됨
따라서 큐에 변환 횟수 또한 넣어주고 이 값을 다음 좌표 visit 함수와 비교하여 적을 visit 보다 작을 경우에 탐색 해줌 

'''

from sys import stdin 
from collections import deque
INF = int(1e9)
input = stdin.readline
DIR = [[]for i in range(3)]
DIR[0] = [[-1,-1],[-1,1],[1,-1],[1,1]]
DIR[1] = [[-1,0],[1,0],[0,-1],[0,1]]
DIR[2] = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]

n = int(input())
MAXN = (n**2+1)
gr = []
a,b=-1,-1

for i in range(n):
    gr.append(list(map(int,input().rsplit())))
    if [a,b]==[-1,-1]:
        for j in range(n):
            if gr[i][j]==1:
                a,b=i,j

q = deque()
q.append((a,b,2,0,0,0)) 
q.append((a,b,2,1,0,0))
q.append((a,b,2,2,0,0))

visited = [[[[INF]*(MAXN+1) for i in range(3)]for j in range(n)]for k in range(n)]
visited[a][b][0][1] = 0
visited[a][b][1][1] = 0
visited[a][b][2][1] = 0

result = INF
answer = INF
while(q):
    x,y,nextNUM,HT,cnt,rot = q.popleft()
    if nextNUM==MAXN:
        if result>cnt:
            result = cnt 
            answer=rot
        if result==cnt:
            if answer>rot:
                answer = rot
        continue

    extend=n+1 if HT!=2 else 2 #룩,비숍 떔시 넣어줌
    NUM = len(DIR[HT]) # 뻗치는 방향 수 (룩,비숍 4 // 나이트 8 ) 
    for i in range(NUM):
        for j in range(1,extend):
            nx = x + DIR[HT][i][0]*j
            ny = y + DIR[HT][i][1]*j 
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            t = nextNUM if gr[nx][ny]!=(nextNUM) else nextNUM+1 
            if visited[nx][ny][HT][t] <= rot:
                continue 
            visited[nx][ny][HT][t]=rot
            q.append((nx,ny,t,HT,cnt+1,rot))
            
    for i in [0,1,2]:
        if i==HT:
            continue
        if (rot+1) >= visited[x][y][i][nextNUM]:
            continue
        visited[x][y][i][nextNUM]=rot+1
        q.append((x,y,nextNUM,i,cnt+1,rot+1))

print(result,answer)    

