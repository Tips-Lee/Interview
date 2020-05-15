from collections import deque


def dfs(graph, vertex):
    stack = deque([vertex])
    found = {vertex}
    parent = {vertex: None}
    rst = []
    while stack:
        cur_vertex = stack.pop()
        rst.append(cur_vertex)
        for node in graph[cur_vertex]:
            if node not in found:
                stack.append(node)
                found.add(node)
                parent[node] = cur_vertex
    return rst, parent


if __name__ == '__main__':
    g = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'E'],
         'D': ['B', 'C', 'E', 'F'],
         'E': ['C', 'D'],
         'F': ['D']}
    rst, parent = dfs(g, 'A')
    vertex = 'E'
    while vertex:
        print(vertex)
        vertex = parent[vertex]

