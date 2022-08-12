'''
문제
크기가 N×M인 격자판에 크기가 H×W인 직사각형이 놓여 있다. 격자판은 크기가 1×1인 칸으로 나누어져 있다. 격자판의 가장 왼쪽 위 칸은 (1, 1), 가장 오른쪽 아래 칸은 (N, M)이다. 직사각형의 가장 왼쪽 위칸은 (Sr, Sc)에 있을 때, 이 직사각형의 가장 왼쪽 위칸을 (Fr, Fc)로 이동시키기 위한 최소 이동 횟수를 구해보자.

격자판의 각 칸에는 빈 칸 또는 벽이 있다. 직사각형은 벽이 있는 칸에 있을 수 없다. 또한, 직사각형은 격자판을 벗어날 수 없다.

직사각형은 한 번에 왼쪽, 오른쪽, 위, 아래 중 한 방향으로 한 칸 이동시킬 수 있다.

입력
첫째 줄에 격자판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 격자판의 각 칸의 정보가 주어진다. 0은 빈 칸, 1은 벽이다.

마지막 줄에는 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc가 주어진다.

격자판의 좌표는 (r, c) 형태이고, r은 행, c는 열이다. 1 ≤ r ≤ N, 1 ≤ c ≤ M을 만족한다.

출력
첫째 줄에 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

제한
2 ≤ N, M ≤ 1,000
1 ≤ H ≤ N
1 ≤ W ≤ M
1 ≤ Sr ≤ N-H+1
1 ≤ Sc ≤ M-W+1
1 ≤ Fr ≤ N-H+1
1 ≤ Fc ≤ M-W+1
입력으로 주어진 직사각형은 격자판을 벗어나지 않고, 직사각형이 놓여 있는 칸에는 벽이 없다.
예제 입력 1 
4 5
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
2 2 1 1 1 4
예제 출력 1 
7
아래, 아래, 오른쪽, 오른쪽, 오른쪽, 위, 위

예제 입력 2 
6 7
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
0 0 0 0 0 0 0
2 3 1 1 5 5
예제 출력 2 
8
아래, 아래, 오른쪽, 오른쪽, 오른쪽, 아래, 아래, 오른쪽
'''
-오류가 났던 부분
 한줄에 있는 벽을 체크할 때 발견시 continue를 해줌으로써 방문 체크를 건너뛰는게 아닌 무조건적으로 실행되는 코드를 짜버림
  

from collections import deque
from sys import stdin
input = stdin.readline
# 왼,위,오,아
dx = [0,-1,0,1] 
dy = [-1,0,1,0]

if __name__=='__main__':
    n,m = map(int,input().rsplit())
    gr = [[0]*m for i in range(n)]
    for i in range(n):
        gr[i]=list(map(int,input().rsplit()))
    h,w,sx,sy,ex,ey=map(int,input().rsplit())
    h-=1
    w-=1
    sx-=1
    sy-=1
    ex-=1
    ey-=1
    q=deque()
    visited=[[-1]*m for i in range(n)]
    visited[sx][sy]=0 
    q.append((sx,sy))
    answer=-1
    while(q):
        x,y=q.popleft()
        if [x,y]==[ex,ey]:
            answer=visited[x][y]
            break 
        for i in range(4):  
            nx = x + dx[i]
            ny = y + dy[i]
            hx = nx + h 
            wy = ny + w
            if nx<0 or ny<0 or hx>=n or wy>=m:
                continue 
            if visited[nx][ny]!=-1:
                continue
            trigger = False
            if i==0:                    #왼 위 오 아
                for j in range(nx,hx+1):
                    if gr[j][ny]==1:
                        trigger=True
                        break
            if i==1:
                for j in range(ny,wy+1):
                    if gr[nx][j]==1:
                        trigger=True
                        break
            if i==2:
                for j in range(nx,hx+1):
                    if gr[j][wy]==1:
                        trigger=True
                        break
            if i==3:
                for j in range(ny,wy+1):
                    if gr[hx][j]==1:
                        trigger=True
                        break
            if trigger==True:
                continue
            visited[nx][ny]=visited[x][y]+1
            q.append((nx,ny))
    print(answer)
