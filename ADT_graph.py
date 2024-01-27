

class Vertex:
    def __init__(self, key):
        self.id = key
        self.collected_to = {}

    def add_neighbor(self, nbr, weight=1):
        self.collected_to[nbr] = weight

    def get_collections(self):
        return self.collected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.collected_to[nbr]

    def __str__(self):
        return str([self.id]) + ' --> ' + str([nbr.id for nbr in self.collected_to])


class Graph:
    def __init__(self):
        self.vert_dict = {}

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex
        # return new_vertex

    def get_vertex(self, key):
        if key in self.vert_dict:
            return self.vert_dict[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vert_dict

    def add_edge(self, f, t, weight):
        if f not in self:
            self.add_vertex(f)
        if t not in self:
            self.add_vertex(t)
        self.vert_dict[f].add_neighbor(self.vert_dict[t], weight)

    def get_vertices(self):
        return self.vert_dict.keys()

    def __iter__(self):
        return self.vert_dict.values()

    def __len__(self):
        return len(self.vert_dict)



if __name__ == '__main__':
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    A.add_neighbor(B, 2)
    A.add_neighbor(C, 3)
    print(A.get_collections())
    print(A.get_id())
    print(A.get_weight(B))
    print(A.collected_to)