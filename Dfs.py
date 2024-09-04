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

def dfs(vis, graph, node):
    if node not in vis:
        print(node, end = " ")
        vis.append(node)
        for neighbour in graph[node]:
            dfs(vis, graph, neighbour)

dfs(vis, graph, 'A')