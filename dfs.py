def dfs(g, s, vis):
    vis[s] = 1
    print(s)
    for c in g[s]:
        if not vis[c]:
            dfs(g, c, vis)

g1 = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3, 1]
}

vis = [0, 0, 0, 0, 0]
dfs(g1, 0, vis)  # Starting DFS from node 0

# Reset vis list
vis = [0, 0, 0]

# g2 = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': [],
#     'D': [],
#     'E': []
# }

# # Reset vis list for the string-indexed graph
# vis = {'A': 0, 'B': 0, 'C': 0, 'D': 0 , 'E': 0}

# dfs(g2, 'A', vis)  # Starting DFS from node 'A'
