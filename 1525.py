'''
문제
3×3 표에 다음과 같이 수가 채워져 있다. 오른쪽 아래 가장 끝 칸은 비어 있는 칸이다.

1	2	3
4	5	6
7	8	 
어떤 수와 인접해 있는 네 개의 칸 중에 하나가 비어 있으면, 수를 그 칸으로 이동시킬 수가 있다. 물론 표 바깥으로 나가는 경우는 불가능하다. 우리의 목표는 초기 상태가 주어졌을 때, 최소의 이동으로 위와 같은 정리된 상태를 만드는 것이다. 다음의 예를 보자.

1	 	3
4	2	5
7	8	6
1	2	3
4	 	5
7	8	6
1	2	3
4	5	 
7	8	6
1	2	3
4	5	6
7	8	 
가장 윗 상태에서 세 번의 이동을 통해 정리된 상태를 만들 수 있다. 이와 같이 최소 이동 횟수를 구하는 프로그램을 작성하시오.

입력
세 줄에 걸쳐서 표에 채워져 있는 아홉 개의 수가 주어진다. 한 줄에 세 개의 수가 주어지며, 빈 칸은 0으로 나타낸다.

출력
첫째 줄에 최소의 이동 횟수를 출력한다. 이동이 불가능한 경우 -1을 출력한다.

예제 입력 1 
1 0 3
4 2 5
7 8 6
예제 출력 1 
3
예제 입력 2 
3 6 0
8 1 2
7 4 5
예제 출력 2 
-1
'''

# 중복되는 것을 어떻게 체크할지 고민
# 최대 횟수는 9! 
# 큐에다가 방문 리스트를 넣어줄까 했지만 그럴 경우 메모리 초과될 수 있다고 생각

# 딕셔너리를 이용해 방문체크 하면 된다는걸 알게됨

# [알게 된점]
# 딕셔너리 키 값에는 리스트가 들어갈수 없지만 문자열은 입력 가능
# 문자열을 처음 선언했을때 []와 ''은 다르다는걸 알게됨
# 문자열은 바로 인덱스 접근해서 변환 못해서 replace 또는 리스트로 변환하면 된다는걸 알게됨
# 문자열 인덱스 검색=>find, 리스트 인덱스 검색=>index 
# 문자열을 리스트 변환 -> list()
# 리스트를 문자열로 변환 -> ''.join()
# 딕셔너리에서 없는 키 값을 접근했을시 에러가 뜸
# get 함수를 통해서 없는 키 값 또한 접근 가능 


from collections import deque
from copy import deepcopy
from dataclasses import replace
from sys import stdin 
input = stdin.readline
dx = [0,0,-1,1] #왼,오,위,아
dy = [-1,1,0,0]
if __name__=='__main__':
    gr=''
    visited=dict()
    for i in range(3):
        gr+=''.join(input().rsplit())
    result='123456780'
    visited[gr]=0
    q= deque()
    q.append(gr)
    answer=-1 if gr!=result else 0
    while(q):
        temp=q.popleft()
        idx = temp.find('0')
        x,y = idx//3,idx%3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=3 or ny>=3:
                continue 
            g = deepcopy(temp)
            next = nx*3+ny
            g=list(g)
            g[next],g[idx]=g[idx],g[next]
            g=''.join(g)
            if visited.get(g):
                continue 
            visited[g]=visited[temp]+1
            if g==result:
                answer=visited[g]
                break
            q.append(g)
        if answer!=-1:
            break 
    print(answer)
