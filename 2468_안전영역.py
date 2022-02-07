'''
n*n 2차원 그래프에 각각의 칸에 높이가 주어진다.
이때 장마로 인해 수면의 높이보다 낮은 칸들은 잠긴다고 가정했을때
잠기지 않은 영역 끼리 묶어서 안전 지역이라고 지칭하는데
장마철에 물에 잠기지 않는 안전 지역의 최대 개수를 계산하는 프로그램을 짜기
'''
# BFS로 안전 지역의 개수를 구함
# 체크 하는 영역은 높이 최솟값 부터 최대값까지
# 만약 전체 영역이 잠기지 않는다면 0 이 나오므로 이때에는 그래프 자체가 안전영역의 한 덩어리 이므로 1을 출력
from collections import deque
import copy
import sys
input = sys.stdin.readline

n = int(input())
gr = [[0]*n for i in range(n)]
gr[0] = list(map(int,input().split()))
max_value = max(gr[0])
min_value = min(gr[0])

for i in range(1,n):
  gr[i] = list(map(int,input().split()))
  if max_value < max(gr[i]):
    max_value = max(gr[i])
  if min_value > min(gr[i]):
    min_value = min(gr[i])

c = [0]*(max_value+1)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def BFS(a,b,graph,num):
  graph[a][b] = num
  q = deque()
  q.append((a,b))
  while(q):
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
      if graph[nx][ny] > num:
        q.append((nx,ny))
        graph[nx][ny] = num

  
for k in range(min_value,max_value):
  cnt = 0
  check = k
  gr_c = copy.deepcopy(gr)
  for i in range(n):
    for j in range(n):
      if gr_c[i][j]>check:
        cnt+=1
        BFS(i,j,gr_c,check)
  c[check] = cnt

result = max(c)
print(result if result != 0 else 1 )
