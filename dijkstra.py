from collections import deque
import math
from collections import Iterator, Iterable
import heapq

'''
def dijkstra(graph, vertex):
    heap = [(0, vertex)]
    seen = []
    parent = {vertex: None}
    distance = {vertex: math.inf for vertex in graph}
    distance[vertex] = 0
    print(heap)
    while heap:
        cur_dist, cur_vertex = heapq.heappop(heap)
        if cur_vertex in seen:
            continue
        seen.append(cur_vertex)
        # distance[cur_vertex] = cur_dist
        for vertex in graph[cur_vertex]:
            if vertex not in seen:
                dist = graph[cur_vertex][vertex] + distance[cur_vertex]
                if dist < distance[vertex]:
                    heapq.heappush(heap, (dist, vertex))
                    print(heap)
                    parent[vertex] = cur_vertex
                    distance[vertex] = dist
    return seen, parent, distance
'''

'''
def dijkstra(graph, vertex):
    heap = [(0, vertex)]
    seen = []
    parent = {vertex: None}
    distance = {vertex: math.inf for vertex in graph}
    distance[vertex] = 0
    while heap:
        # print(heap)
        item = min(heap)
        cur_dist, cur_vertex = item
        heap.remove(item)
        if cur_vertex in seen:
            continue
        seen.append(cur_vertex)
        # distance[cur_vertex] = cur_dist
        for vertex in graph[cur_vertex]:
            if vertex not in seen:
                dist = graph[cur_vertex][vertex] + distance[cur_vertex]
                if dist < distance[vertex]:
                    heap.append((dist, vertex))
                    parent[vertex] = cur_vertex
                    distance[vertex] = dist
    return seen, parent, distance
'''


def dijkstra(graph, vertex):
    heap = OrderList([(0, vertex)])
    seen = []
    parent = {vertex: None}
    distance = {vertex: math.inf for vertex in graph}
    distance[vertex] = 0
    while heap:
        # print(heap)
        item = heap.pop()
        cur_dist, cur_vertex = item
        if cur_vertex in seen:
            continue
        seen.append(cur_vertex)
        # distance[cur_vertex] = cur_dist
        for vertex in graph[cur_vertex]:
            if vertex not in seen:
                dist = graph[cur_vertex][vertex] + distance[cur_vertex]
                if dist < distance[vertex]:
                    heap.binary_insert((dist, vertex))
                    parent[vertex] = cur_vertex
                    distance[vertex] = dist
    return seen, parent, distance


class OrderList(list):
    def __init__(self, iterable, reverse=True):
        iterable = sorted(iterable, reverse=reverse)
        self.reverse = reverse
        super(OrderList, self).__init__(iterable)

    def binary_insert(self, val):
        left = 0
        right = len(self)-1
        while left <= right:
            mid = (left + right)//2
            if self[mid] == val:
                self.insert(mid + 1, val)
            elif self[mid] > val:
                if self.reverse:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if self.reverse:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            self.insert(left, val)

    def binary_remove(self, val):
        idx = self.binary_find(val)
        del self[idx]

    def binary_find(self, val):
        left = 0
        right = len(self)-1
        while left <= right:
            mid = (left + right)//2
            if self[mid] == val:
                return mid
            elif self[mid] > val:
                if self.reverse:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if self.reverse:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            raise ValueError


if __name__ == '__main__':
    g = {'A': {'B': 5, 'C': 1},
         'B': {'A': 5, 'C': 5, 'D': 1},
         'C': {'A': 1, 'B': 5, 'D': 4, 'E': 8},
         'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
         'E': {'C': 8, 'D': 3},
         'F': {'D': 6}}

    print(dijkstra(g, 'A'))

    # li = OrderList((1, 2, 3, 4))
    # print(li)
    # li.binary_remove(3)
    # print(li)
