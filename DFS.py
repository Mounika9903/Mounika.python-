def initiateDFS(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFS(neighbour, visited, adj, result)
 
 
def printDFSTraversal(adj, n):
    result = []
    visited = [False] * n 
 
    for i in range(n):
        if visited[i] == False:
            initiateDFS(i, visited, adj, result)
 
    print("DFS traversal is:", result)
 
# adjacency list construction
 
n, m = map(int, input().split())
adj = []
for i in range(n): 
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
printDFSTraversal(adj, n)

