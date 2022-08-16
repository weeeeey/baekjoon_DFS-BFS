'''
문제
상근이는 1층 빌딩에 침입해 매우 중요한 문서를 훔쳐오려고 한다. 상근이가 가지고 있는 평면도에는 문서의 위치가 모두 나타나 있다. 빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 열쇠가 필요하다. 상근이는 일부 열쇠를 이미 가지고 있고, 일부 열쇠는 빌딩의 바닥에 놓여져 있다. 상근이는 상하좌우로만 이동할 수 있다.

상근이가 훔칠 수 있는 문서의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.

각 테스트 케이스의 첫째 줄에는 지도의 높이와 너비 h와 w (2 ≤ h, w ≤ 100)가 주어진다. 다음 h개 줄에는 빌딩을 나타내는 w개의 문자가 주어지며, 각 문자는 다음 중 하나이다.

'.'는 빈 공간을 나타낸다.
'*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
'$'는 상근이가 훔쳐야하는 문서이다.
알파벳 대문자는 문을 나타낸다.
알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다.
마지막 줄에는 상근이가 이미 가지고 있는 열쇠가 공백없이 주어진다. 만약, 열쇠를 하나도 가지고 있지 않는 경우에는 "0"이 주어진다.

상근이는 처음에는 빌딩의 밖에 있으며, 빌딩 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎을 드나들 수 있다. 각각의 문에 대해서, 그 문을 열 수 있는 열쇠의 개수는 0개, 1개, 또는 그 이상이고, 각각의 열쇠에 대해서, 그 열쇠로 열 수 있는 문의 개수도 0개, 1개, 또는 그 이상이다. 열쇠는 여러 번 사용할 수 있다.

출력
각 테스트 케이스 마다, 상근이가 훔칠 수 있는 문서의 최대 개수를 출력한다.

예제 입력 1 
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony
예제 출력 1 
3
1
0

'''
# 논리를 제대로 못짜면 시간 초과가 뜰거 같아서 깊게 고민함

# 큐에는 좌표 값만 넣어주고 visited 함수는 False,True 체크
# [대문자를 만났을때]
# 열쇠 리스트 True 체크를 해서 없을시 door 리스트에 좌표 저장해둠
# 열쇠 있다면 기존 방식대로 탐색
# [소문자를 만났을때]
# 해당되는 대문자 door를 체크해줘서 탐색은 가능했는데 아직 못한거니 큐 왼쪽에 넣어줌
# key 리스트도 트루 체크 


#ord() , 'a'-'A' = 32
from collections import deque
from sys import stdin 
input = stdin.readline

dx = [0,-1,0,1]
dy = [-1,0,1,0]
min_a = ord('a')
max_a = min_a+25
min_A = ord('A') 
max_A = min_A+25

# if __name__=='__main__':
T = int(input().rstrip())    
while(T):
    T-=1
    n,m = map(int,input().rsplit())
    N,M = n+2,m+2
    result = 0
    gr = [[]for i in range(n+2)]
    gr[0]='.'*M
    gr[N-1]='.'*M
    visited = [[False]*(M) for i in range(N)]
    visited[0][0]=True
    for i in range(1,n+1):
        gr[i]='.'+(input().rstrip())+'.'
    key = [False]*26        
    temp = list(input().rstrip())
    if temp!=['0']:
        for t in temp:
            a = ord(t)-ord('a')
            key[a]=True
    door = [[]for i in range(26)] # 통과 못한 대문자 저장
    q = deque()
    q.append((0,0))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue 
            if gr[nx][ny]=='*':
                continue 
            if visited[nx][ny]==True:
                continue
            if gr[nx][ny]=='.':
                visited[nx][ny]=True
                q.append((nx,ny))
            if gr[nx][ny]=='$':
                visited[nx][ny]=True 
                result+=1
                q.append((nx,ny))
            num = ord(gr[nx][ny])
            if min_a <= num <=max_a:
                key[num-min_a]=True 
                visited[nx][ny]=True
                q.append((nx,ny))
                while(door[num-min_a]):
                    aa,bb=door[num-min_a].pop()
                    if visited[aa][bb]==False:
                        q.appendleft((aa,bb))
            if min_A<=num<=max_A:
                if key[num-min_A]==True:
                    visited[nx][ny]=True 
                    q.append((nx,ny))
                else:
                    door[num-min_A].append([nx,ny])
    print(result)
