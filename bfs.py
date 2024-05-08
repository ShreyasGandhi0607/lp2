g = {
  0 : [1, 2],
  1 : [0 , 3, 4],
  2 : [0, 3],
  3 : [1, 2, 4],
  4 : [3 ,1]
}

def bfs(g , s):
  q = [s]
  vis = [s]
  while q:
    curr = q.pop(0)
    print(curr)
    for c in g[curr]:
      if c not in  vis:
        vis.append(c)
        q.append(c)



bfs(g , 0)


g2 = {
    'A': ['B', 'C'],
    'B': ['E', 'D'],
    'C': [],
    'D': [],
    'E': []
}

bfs(g2 , 'A')