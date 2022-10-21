# for BFS
from queue import Queue


# class for Graph
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    def add_node(self, node):
        self.nodes.append(node)
        self.adj_list[node] = []

    def print_list(self):
        print("Adjacency list:")
        for node in self.nodes:
            print(node, "->", self.adj_list[node])

    def delete_node(self, node):
        flag = 1
        count = 0
        deleted_edges = 0
        for nodee in self.nodes:
            if nodee == node:
                flag = 0
            if self.adj_list[nodee].__contains__(node):
                if flag == 1:
                    count = count + 1
                self.adj_list[nodee].remove(node)
                deleted_edges = deleted_edges + 1
        self.nodes.pop(count)
        return deleted_edges

    def delete_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


# getting node count
nodes = []
n = int(input("Enter no.of nodes:"))
# adding node to graph
for i in range(n):
    node = input(f"Enter node {i + 1}:")
    nodes.append(node)

# initializing graph using nodes as an argument
graph = Graph(nodes)

# getting node count
e = int(input("Enter no.of edges:"))
# getting node details
for i in range(e):
    u, v = input(f"Enter edge {i + 1}: ").split(" ")
    graph.add_edge(u, v)  # adding node into graph


# function for DFS
def dfs(graph, start_node, target_node):
    stack.append(start_node)
    visited.add(start_node)

    if start_node == target_node:
        return 1

    for neighbour in graph.adj_list[start_node]:
        if neighbour not in visited:
            print(i, end=" ")
            result = dfs(graph, neighbour, target_node)

            if result == 1:
                return 1
              


# function for BFS
def bfs(graph, start_node, target_node):
    visited.add(start_node)
    queue.put(start_node)

    while not queue.empty():
        m = queue.get()
        print(m, end=" ")

        if m == target_node:
            break

        for neighbour in graph.adj_list[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.put(neighbour)


# loop for option choosing
while True:
    choice = int(input(
        "\n ---- Menu ----\n1. Add node\n2. Add edge\n3. Delete node\n4. Delete edge\n5. Display graph\n6. BFS\n7. "
        "DFS\n8. Exit\n"))
    if choice == 1:
        node = input(f"Enter node {n + 1}: ")
        graph.add_node(node)
        n = n + 1
    elif choice == 2:
        u, v = input(f"Enter edge {e + 1}: ").split(" ")
        graph.add_edge(u, v)
        e = e + 1
    elif choice == 3:
        d_node = input("Enter node to delete: ")
        deleted = graph.delete_node(d_node)
        n = n - 1
        e = e - deleted
    elif choice == 4:
        e1, e2 = input("Enter edge to delete: ").split(" ")
        graph.delete_edge(e1, e2)
        e = e - 1
    elif choice == 5:
        graph.print_list()
    elif choice == 6:
        visited = set()
        path = []
        queue = Queue()

        start_node = input("Enter start node:")
        target_node = input("Enter target node:")

        bfs(graph, start_node, target_node)
    elif choice == 7:
        start_node = input("Enter start node:")
        target_node = input("Enter target node:")

        visited = set()
        stack = []

        dfs(graph, start_node, target_node)
    elif choice == 8:
        break
    else:
        print("Enter valid option")
