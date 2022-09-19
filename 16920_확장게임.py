# 문제
# 구사과와 친구들이 확장 게임을 하려고 한다. 이 게임은 크기가 N×M인 격자판 위에서 진행되며, 각 칸은 비어있거나 막혀있다. 각 플레이어는 하나 이상의 성을 가지고 있고, 이 성도 격자판 위에 있다. 한 칸 위에 성이 두 개 이상인 경우는 없다.

# 게임은 라운드로 이루어져 있고, 각 라운드마다 플레이어는 자기 턴이 돌아올 때마다 성을 확장해야 한다. 제일 먼저 플레이어 1이 확장을 하고, 그 다음 플레이어 2가 확장을 하고, 이런 식으로 라운드가 진행된다.

# 각 턴이 돌아왔을 때, 플레이어는 자신이 가지고 있는 성을 비어있는 칸으로 확장한다. 플레이어 i는 자신의 성이 있는 곳에서 Si칸 만큼 이동할 수 있는 모든 칸에 성을 동시에 만든다. 위, 왼쪽, 오른쪽, 아래로 인접한 칸으로만 이동할 수 있으며, 벽이나 다른 플레이어의 성이 있는 곳으로는 이동할 수 없다. 성을 다 건설한 이후엔 다음 플레이어가 턴을 갖는다.

# 모든 플레이어가 더 이상 확장을 할 수 없을 때 게임이 끝난다. 게임판의 초기 상태가 주어졌을 때, 최종 상태를 구해보자.


# 처음에는 cnt가 move[num] 보다 작고 이동 가능하면 appendleft를 해주고 넘었을시 append를 해줌
# 이럴 경우 겹치는 동선에서 방문처리 하기 힘들었음
# 사람에 따라 최대 이동하고 넘었을시 다음번에 다시 방문할 수 있도록 저장해둠

# 최고 반복문을 탈출하는 방법을 start에 +1 을 해주면서 end와 동일시 되면 나오도록 해줌
# 이럴 경우 덧셈 연산을 너무 많이해서 시간 초과 뜸
# 사람들이 이동할 방법 즉 len(people)이 모두 0일 경우 탈출로 했더니 통과함

from sys import stdin 
from collections import deque
from copy import deepcopy
input = stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

start = 0
end = 0
n,m,p = map(int,input().rsplit())
move = list(map(int,input().rsplit()))
move = [0]+move
gr = [[] for i in range(n)]
people = [[] for i in range(p+1)]
result = [0]*(p+1)
visited = [[-1]*m for i in range(n)]

for i in range(n):
    gr[i]=list(input().rstrip())
    for j in range(m):
        if gr[i][j]=='#':
            continue
        if gr[i][j] !='.':
            num = int(gr[i][j])
            people[num].append([i,j])
            result[num]+=1
        
num=1
while(1):
    q = deque()
    flag = False 
    for i in range(1,p+1):
        k=len(people[i])
        if k!=0:
            flag = True
            break
    if flag==False:
        break
    while(people[num]):
        a,b = people[num].pop()
        q.append((a,b))
        visited[a][b]=0
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if gr[nx][ny]=='#':
                continue
            if visited[nx][ny]!=-1 or gr[nx][ny]!='.':
                continue
            if visited[x][y]+1<move[num]:
                q.append((nx,ny))
            else:
                people[num].append([nx,ny])
            visited[nx][ny]=visited[x][y]+1
            gr[nx][ny]=str(num)
            result[num]+=1

    if num==p:
        num=1
    else:
        num+=1

result = result[1:]
for i in result:
    print(i, end = ' ')
