from collections import deque


def bfs(graph, vertex):
    queue = deque([vertex])
    found = {vertex}
    rst = []
    while queue:
        cur_vertex = queue.popleft()
        rst.append(cur_vertex)
        for node in graph[cur_vertex]:
            if node not in found:
                queue.append(node)
                found.add(node)
    return rst


if __name__ == '__main__':
    g = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'E'],
         'D': ['B', 'C', 'E', 'F'],
         'E': ['C', 'D'],
         'F': ['D']}
    print(bfs(g, 'A'))
