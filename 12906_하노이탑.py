'''
A 막대에는 A 만
B 막대에는 B 만
C 막대에는 C 만
남기게 하는 최소 이동횟수를 출력하면 됨
'''
# 딕셔너리로 방문체크 하는 것은 생각할 수 있었음
# 하지만 visited를 총 3개 둬서 각 막대기의 체크를 다 해서 하나라도 False 라면 큐에 넣는 생각을 함
# 이럴 경우 해당 경우의 수에 대한 방문체크 하기 번거로워짐

# 각 막대를 한줄로 묶어서 스트링 구분을 , 로 해두고 그것을 키 값으로 방문체크함 

from collections import deque
from sys import stdin 
input = stdin.readline
dx = {0:'A', 1:'B', 2:'C'}

sen = [[]for i in range(3)]
sen[0] = input().rstrip()
sen[1] = input().rstrip()
sen[2] = input().rstrip()
for i in range(3):
    C = sen[i].split(' ')
    if len(C)==1:
        sen[i] = ''
    else:
        sen[i] = C[1]
    
visited = dict()
visited[','.join(sen)] = 1

def checkStr(x,y,z):
    xx = ''.join(x)
    yy = ''.join(y)
    zz = ''.join(z)
    t = ','.join([xx,yy,zz])
    if visited.get(t):
        return False 
    else:
        visited[t]=1
        return True 

for i in range(3):
    sen[i] = list(map(str,sen[i]))
q = deque()
q.append((sen,0))

while(q):
    sentence, move = q.popleft()
    tri = True 
    for i in range(3):
        maxt = len(sentence[i])
        cnt = sentence[i].count(dx[i])
        if maxt!=cnt:
            tri = False 
            break 
    if tri == True :
        print(move)
        break 
    a,b,c = sentence
    
    if len(a)>0:
        cha = a[-1]
        if checkStr(a[:-1],b+[cha],c):
            q.append(([a[:-1],b+[cha],c],move+1))
        if checkStr(a[:-1],b,c+[cha]):
            q.append(([a[:-1],b,c+[cha]],move+1))
    if len(b)>0:
        cha = b[-1]
        if checkStr(a,b[:-1],c+[cha]):
            q.append(([a,b[:-1],c+[cha]],move+1))
        if checkStr(a+[cha],b[:-1],c):
            q.append(([a+[cha],b[:-1],c],move+1))
    if len(c)>0:
        cha = c[-1]
        if checkStr(a,b+[cha],c[:-1]):
            q.append(([a,b+[cha],c[:-1]],move+1))
        if checkStr(a+[cha],b,c[:-1]):
            q.append(([a+[cha],b,c[:-1]],move+1))
        
