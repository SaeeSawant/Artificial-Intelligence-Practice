graph = {
    'A' : ['G', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'D'],
    'D' : ['A', 'E', 'F'],
    'E' : ['F', 'G'],
    'F' : ['C', 'B'],
    'G' : ['A', 'D']
}

vis = []
queue = []

def bfs(vis, graph, node):
    vis.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in vis:
                vis.append(neighbour)
                queue.append(neighbour)

bfs(vis, graph, 'A')