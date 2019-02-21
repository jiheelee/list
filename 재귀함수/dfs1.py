def dfs(n, v):
    stack = []
    visited = [0] * (v+1)
    visited[n] = 1

    stack.append(n)
    while(len(stack) != 0):
        n = stack.pop()
        print(n, end=" ")
        for i in range(v, 0, -1):
            if(adj[n][i] == 1 and visited[i] == 0): #n과 i가 인접이고 방문하지 않은 노드면
                stack.append(i)
                visited[i] = 1



V, E = map(int, input().split())
edge = list(map(int,input().split()))
adj = [[0]*(V+1) for i in range(V+1)]
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
for i in adj:
    print(i)
dfs(1,V)