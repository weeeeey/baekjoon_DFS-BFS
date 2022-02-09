'''
n*m 그래프 상에서 0인 부분을 바다라고 표시하고 나머지 숫자는 빙산의 높이를 표시함.
1년 마다 빙산을 둘러싼 바다의 개수만큼 빙산의 높이는 깍임 (상하좌우 기준)
이때 연결된 빙산들은 한 덩어리로 본다.
빙산이 두 덩어리 이상으로 쪼개지는 최초의 년도를 표시하기
'''
# 처음에는 빙산의 덩어리 갯수를 체크하는 BFS 함수와 빙산을 녹이는 함수를 따로 만듬
# 시간초과
# 처음부터 BFS를 돌리면서 빙산을 녹이고 전체 그래프를 체크 하면서 BFS가 두번 발생하면 덩어리가 
# 두개 이상인 것이므로 동작을 멈추고 년도를 출력하면 끝
# 메모리 초과를 받음
# 아마 BFS함수를 짤때 그래프를 매개변수로 넘기면서 복사하는 과정 때문에 메모리 초과를 받은거 같음
 


from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
gr = [[0]*m for i in range(n)]
for i in range(n):
  gr[i] = list(map(int,input().split()))

def BFS(a,b):
  global gr
  global visit
  q= deque()
  q.append((a,b))
  visit[a][b] = True
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  while(q):
    x,y = q.popleft()
    count = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i] 
      if gr[nx][ny] == 0 and visit[nx][ny] ==False:
        count +=1 
      if gr[nx][ny]>0 and visit[nx][ny] == False:
        q.append((nx,ny))
        visit[nx][ny] = True
    gr[x][y] = max(gr[x][y] - count , 0)

answer = 0
while(True):
  cnt = 0
  visit = [[False]*m for i in range(n)]
  for i in range(n):
    for j in range(m):
      if gr[i][j]>0 and visit[i][j] == False:
        cnt+=1 
        if cnt>=2:
          print(answer)
          exit() 
        BFS(i,j)
  if cnt == 0: 
    print(0)
    break
  answer+=1
  
