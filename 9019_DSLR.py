'''
주어진 규칙에 따라 수가 계산되면서 n이 m이 됐을때의 과정을 출력하면 됨.
'''
# 처음에 자릿수를 이동할때 문자열로 변환 후 새로 만들어줌
# 이럴 경우 시간 초과 발생
# 수학적으로 접근했을때 밑에와 같은 점화식이 나옴 

from sys import stdin 
from collections import deque

input = stdin.readline
for k in range(int(input())):
    n,m = map(int,input().rsplit())
    q = deque()
    q.append((n,''))
    visited = [False]*10000
    visited[n]=True
    while(q):
        x,temp = q.popleft()
        if x==m:
            print(temp)
            break

        d = (x*2)%10000
        if not visited[d]:
            visited[d]=True
            q.append((d,temp+'D'))
        
        
        s = (x-1)%10000 if x!=0 else 9999
        if not visited[s]:
            visited[s]= True 
            q.append((s,temp+'S')) 
        
        l = (10*(x%1000) + x//1000)%10000
        if not visited[l]:
            visited[l]=True 
            q.append((l,temp+'L'))
            
        r = (1000*(x%10) + x//10)%10000
        if not visited[r]:
            visited[r]=True 
            q.append((r,temp+'R'))
        
        
