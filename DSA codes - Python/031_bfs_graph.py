from collections import deque


class Vertex:

    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
    
    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)
    
    def print_adjacent_vertices(self):
        print(self.value, " : ", [i.value for i in self.adjacent_vertices])


# BFS for searching a vertex    
def bfs(starting_vertex, search_value, visited_vertices= {}):

    queue = deque()

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True

    queue.append(starting_vertex)

    while queue:

        current_vertex = queue.popleft()
        if current_vertex.value == search_value:
            print("We found the vertex: ", current_vertex)
            return search_value
        
        print(current_vertex.value)

        for adjacent_vertex in current_vertex.adjacent_vertices:
            
            if not visited_vertices.get(adjacent_vertex.value):
                visited_vertices[adjacent_vertex.value] = True

                queue.append(adjacent_vertex)
    
    print("We did not find the vertex: ", search_value)
    return None



def bfs_traverse(starting_vertex):

    queue = deque()

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True

    queue.append(starting_vertex)

    while queue:

        current_vertex = queue.popleft()

        print(current_vertex.value)

        for adjacent_vertex in current_vertex.adjacent_vertices:
            
            if not visited_vertices.get(adjacent_vertex.value):
                visited_vertices[adjacent_vertex.value] = True

                queue.append(adjacent_vertex)



alice = Vertex("alice")
bob = Vertex("bob")
cynthia = Vertex("cynthia")
derek = Vertex("DEREK")
elaine = Vertex("ELAINE")
frank = Vertex("FRANK")
gina = Vertex("GINA")
hank = Vertex("HANK")
irene = Vertex("IRENE")


alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)

bob.add_adjacent_vertex(frank)
frank.add_adjacent_vertex(hank)
hank.add_adjacent_vertex(cynthia)

derek.add_adjacent_vertex(elaine)
derek.add_adjacent_vertex(gina)
gina.add_adjacent_vertex(irene)

# dfs_traverse(alice)
print(bfs(alice, "GINA"))

# bfs_traverse(alice)

# cynthia.print_adjacent_vertices()
# alice.print_adjacent_vertices()
# bob.print_adjacent_vertices()