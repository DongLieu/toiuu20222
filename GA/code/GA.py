import Solution

N = 6
M = 4
K = 2
a = 2
b = 4
c = 1
d = 3
e = 1
f = 1

t = [1, 3, 4, 2, 2, 3]

s = [
    [0,2,4,1,2,5],
    [2,0,5,5,3,5],
    [4,5,0,4,3,5],
    [1,5,4,0,3,2],
    [2,3,3,3,0,3],
    [5,5,5,2,3,0],
]

g = [
    [3,5,1,5],
    [5,2,5,3],
    [3,1,3,3],
    [5,5,1,3],
    [4,5,4,1],
    [5,3,4,5],
]

sol = Solution.Solution(N,M,K,t,s,g,a,b,c,d,e,f)
while(1):
    sol.init_Sol()
    if sol.rang_buoc():
        break
print(sol.x)
print(sol.y)