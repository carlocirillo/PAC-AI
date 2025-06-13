from collections import deque

class node():
    def __init__(self,id,x,y):
        self.id = id
        self.up_node = None
        self.down_node = None
        self.left_node = None 
        self.right_node = None 
        self.adjacent_nodes = []
        self.x = x
        self.y = y
        self.weight = 1

    
    def add_up_node(self,node):
        self.up_node = node
        self.add_adjacent_nodes()

    def add_down_node(self,node):
        self.down_node = node
        self.add_adjacent_nodes()

    def add_left_node(self,node):
        self.left_node = node
        self.add_adjacent_nodes()

    def add_right_node(self,node):
        self.right_node = node
        self.add_adjacent_nodes()

    def __repr__(self):
        return f"Node {self.id}"

    def add_adjacent_nodes(self):
        if self.right_node:
            self.adjacent_nodes.append(self.right_node)
        if self.left_node:
            self.adjacent_nodes.append(self.left_node)
        if self.up_node:
            self.adjacent_nodes.append(self.up_node)
        if self.down_node:
            self.adjacent_nodes.append(self.down_node)

def bfs_shortest_path(source, dest):
    visited = set()
    prev = {}
    queue = deque([source])
    visited.add(source)

    while queue:
        current = queue.popleft()

        if current == dest:
            break

        for neighbor in current.adjacent_nodes:
            if neighbor not in visited:
                visited.add(neighbor)
                prev[neighbor] = current
                queue.append(neighbor)

    # Ricostruzione del percorso
    path = []
    node = dest
    while node != source:
        path.append(node)
        node = prev.get(node)
        if node is None:
            return None  # Nessun percorso trovato
    #path.append(source)
    path.reverse()
    return path

