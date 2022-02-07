'''
start와 end가 주어졌을때 둘의 촌수를 계산하는 프로그램 짜기

'''
# 처음에는 start의 부모 노드의 자식들만 생각하면서 DFS를 짜서 틀림
# start의 자식인 경우에도 end가 있을 수 있음
# 결국 모든 것이 다 연결되어있는 양방향 그래프인거니까
# 그 점을 활용해서 짬.

n = int(input())
start, end = map(int, input().split())
m = int(input())
family = [[] for i in range(n + 1)]
visit = [-1]*(n+1)
visit[start] = 0
for i in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

def DFS(node):
  global end
  global family
  global visit
  for n in family[node]:
    if visit[n] != -1:
      continue
    visit[n] = visit[node]+1
    DFS(n)
  
DFS(start)
print(visit[end] if visit[end]>0 else -1)
