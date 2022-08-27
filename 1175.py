'''
문제
어제 선물을 모두 포장한 민식이는 이제 선물을 배달하려고 한다. 민식이가 선물을 배달할 곳은 이 문제를 읽는 사람들이 앉아 있는 교실이다. 교실은 직사각형모양이고, 모두 같은 크기의 정사각형 블록으로 나누어져 있다.

입력으로 교실의 지도가 주어진다. 각각의 정사각형 블록은 다음과 같이 4가지 종류가 있다.

S: 지금 민식이가 있는 곳이다. 이곳이 민식이가 배달을 시작하는 곳이고 1개만 있다.
C: 민식이가 반드시 선물을 배달해야 하는 곳이다. 이러한 블록은 정확하게 2개 있다.
#: 민식이가 갈 수 없는 곳이다.
.: 민식이가 자유롭게 지나갈 수 있는 곳이다.
민식이가 한 블록 동서남북으로 이동하는데는 1분이 걸린다. 민식이는 네가지 방향 중 하나로 이동할 수 있으며, 교실을 벗어날 수 없다. 민식이가 선물을 배달해야 하는 곳에 들어갈 때, 민식이는 그 곳에 있는 사람 모두에게 선물을 전달해야 한다. 이 상황은 동시에 일어나며, 추가적인 시간이 소요되지 않는다.

민식이는 어느 누구도 자신을 보지 않았으면 하기 때문에, 멈추지 않고 매 시간마다 방향을 바꿔야 한다. 이 말은 같은 방향으로 두 번 연속으로 이동할 수 없다는 말이다. 민식이가 선물을 모두 배달하는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 교실의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 교실의 지도가 주어진다.

출력
첫째 줄에 민식이가 선물을 모두 배달하는데 걸리는 시간의 최솟값을 출력한다. 만약 불가능 할 때는 -1을 출력한다.

예제 입력 1 
2 3
SCC
...
예제 출력 1 
4
예제 입력 2 
1 5
C.C.S
예제 출력 2 
-1
예제 입력 3 
3 3
#.#
CSC
#.#
예제 출력 3 
5
예제 입력 4 
10 7
#.#....
##...#.
C#...#.
.....#.
..#....
..#S.#.
.##..#.
###..##
..C.#.#
###.#..
예제 출력 4 
24
예제 입력 5 
3 36
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#C
.................S..................
C#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
예제 출력 5 
155
'''

# start ->c1 ->c2
# start =>c2 =>c1
# 둘 중에 작은 값을 찾는 로직을 짰는데 43%에서 틀렸음
# .C. .C. S.. 답이 3인데 4가 나오는 반례를 통해 도착지점에 왔었을때 모든 방향의 경우의 수를 고려해야 한다는걸 깨달음
# 리스트에 도착할 수 있는 모든 경우의 수 최대4 를 리턴시켜 반복문을 통해 모두 뒤져봄


from sys import stdin 
from collections import deque
input = stdin.readline
INF = int(1e9)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(sa,sb,ea,eb,dic):
    visited = [[[-1]*5 for j in range(m)] for i in range(n)]
    visited[sa][sb][dic]=0
    result = []
    q = deque()
    q.append((sa,sb,dic))
    while(q):
        x,y,dir = q.popleft()
        for i in range(4):
            if i==dir:
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if gr[nx][ny]=='#':
                continue 
            if [nx,ny]==[ea,eb]:
                result.append([visited[x][y][dir]+1,i])
                continue
            if visited[nx][ny][i]!=-1:
                continue
            if gr[nx][ny]=='.':
                visited[nx][ny][i]=visited[x][y][dir]+1
                q.append((nx,ny,i))
    return result
if __name__=='__main__':
    n,m = map(int,input().rsplit())
    gr = [[]for i in range(n)]
    sx,sy = 0,0
    C = []
    answer = INF
    for i in range(n):
        gr[i]=list(input().rstrip())
        for j in range(m):
            if gr[i][j]=='S':
                gr[i][j]='.'
                sx,sy = i,j
            if gr[i][j]=='C':
                gr[i][j]='.'
                C.append([i,j])
    cx_1,cy_1 = C[0]
    cx_2,cy_2 = C[1]

    r = bfs(sx,sy,cx_1,cy_1,4)
    for a_1,d_1 in r:
        R=bfs(cx_1,cy_1,cx_2,cy_2,d_1)
        for A,B in R:
            answer = min(a_1+A,answer)
    
    r = bfs(sx,sy,cx_2,cy_2,4)
    for a_2,d_2 in r:
        R=bfs(cx_2,cy_2,cx_1,cy_1,d_2)
        for A,B in R:
            answer = min(a_2+A,answer)
    print(answer if answer!= INF else -1)
