# ㅗ 모양을 제외한 다른 도형들의 모든 경로를 합체하면 한점에서부터 4번 이동할수 있는 모든 경로를 더하면 됨
# ㅗ 모양은 대칭회전 다 하면 기준점 4방향에서 한점만 뺴면 됨
# 모두 계산 후 최대값 도출

# visited 그래프를 매점마다 생성하는 것이 바깥에서 한번 생성후 True False로 초기화 해주면 됨
# 매번 생성했다가 시간 초과 뜸


from sys import stdin
input = stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m = map(int,input().rsplit())
gr = [[0]*m for i in range(n)]

for i in range(n):
    gr[i] = list(map(int,input().rsplit()))
answer = 0

def dfs(x,y,cnt,num):
    global answer
    if cnt==4:
        answer = max(answer,num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<(n+1) and 0<=ny<(m+1):
            if visited[nx][ny]==False:
                visited[nx][ny]=True
                dfs(nx,ny,cnt+1,num+gr[nx][ny])
                visited[nx][ny]=False 


for i in range(n):
    gr[i]=[0]+gr[i]+[0]
gr = [[0]*(m+2)] + gr + [[0]*(m+2)] 

visited = [[False]*(m+2) for i in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        visited[i][j]=True
        dfs(i,j,1,gr[i][j])
        visited[i][j]=False
for i in range(1,n+1):
    for j in range(1,m+1):
        temp = gr[i][j] + gr[i-1][j] + gr[i][j-1] + gr[i+1][j] + gr[i][j+1]
        for k in range(4):
            answer = max(answer,temp-gr[i+dx[k]][j+dy[k]])


print(answer)
