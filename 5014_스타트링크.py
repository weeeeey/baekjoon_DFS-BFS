'''
전체 층, 시작 층, 도착 층, up층, down 층 이 주어졌을때
시작층에서부터 도착층에 도착하는 최소한의 횟수를 출력하기
'''
# down처리 할때 *-1을 안해줘서 처음에 틀림; 
from collections import deque 
import sys
input = sys.stdin.readline 
f,start,target,u,d = map(int,input().split())
distant = [-1]*(f+1)
distant[start] = 0 
q = deque()
q.append(start)
dx = [u,(-1)*d]
while(q):
  x = q.popleft()
  if x==target:
    print(distant[x])
    exit() 
    
  for i in range(2):
    nx = x + dx[i] 
    if nx<1 or nx>f:
      continue 
    if distant[nx]==-1:
      distant[nx] = distant[x]+1 
      q.append(nx)

print("use the stairs")
