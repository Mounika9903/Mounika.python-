n,m=map(int,input().split())
adj=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    adj.append(row)
for i in range(m):
    u,v =map(int,input().split())
    adj[u][v]=1
    adj[v][u]=1
print(adj)
