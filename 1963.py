from copy import deepcopy
from sys import stdin 
from collections import deque
import math
input = stdin.readline

def primary(n):
    a = int(math.sqrt(n))
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True

p = dict()
for i in range(1000,10000):
    if primary(i)==True:
        p[str(i)]=-1

T = int(input())
for TT in range(T):
    pri = deepcopy(p)
    n,m = map(int,input().rsplit())
    m = str(m)
    n = str(n)
    result = -1
    q = deque()
    q.append(n)
    pri[n]=0
    while(q):
        arr = q.popleft()
        cnt = pri[arr]
        if arr==m:
            result = cnt
            break
        for i in range(4):
            for j in range(10):
                if i==0 and j==0:
                    continue 
                temp = list(deepcopy(arr))
                temp[i]=str(j)
                temp=''.join(map(str,temp)) 
                if pri.get(temp)==None:
                    continue
                if pri[temp]!=-1:
                    continue 
                pri[temp]=cnt+1
                q.append(temp)
    print(result if result!=-1 else "Impossble")
