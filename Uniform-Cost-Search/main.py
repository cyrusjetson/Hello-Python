from collections import defaultdict
# for BFS
from queue import Queue

# getting node count
nodes = []


class Graph2:
    def __init__(self):
        self.graph = defaultdict(list)
        self.path = []

    def display(self):
        for i in self.graph.keys():
            print(i + " -> ", end="")
            print("[", end="")
            for (node, cost) in self.graph[i]:
                print(" (", end="")
                print(node + ", ", cost, end=") ")
            print("]")

    def delete_node(self, u):
        for i in self.graph.keys():
            for (node, cost) in self.graph[i]:
                if node == u:
                    self.graph[i].remove((node, cost))
        if self.graph.__contains__(u):
            self.graph.pop(u)

    def delete_edge(self, u, v):
        for (node, cost) in self.graph[u]:
            if node == v:
                self.graph[u].remove((node, cost))
        for (node, cost) in self.graph[v]:
            if node == u:
                self.graph[v].remove((node, cost))

    def add_node(self, node):
        value = ()
        self.graph[node].append(value)

    def add_edgee(self, u, v):
        value = (v, 1)
        self.graph[u].append(value)
        value = (u, 1)
        self.graph[v].append(value)

    def get_size(self):
        count = 0
        for i in self.graph.keys():
            count = count + 1
        return count

    def add_edge(self, u, v, c):
        value = (v, c)
        for m in self.graph.keys():
            if m == u:
                for (node, cost) in self.graph[m]:
                    if node == v:
                        self.graph[m].remove((node, cost))
                        self.graph[m].append((node, c))
                break

        flag = 1
        for m in self.graph.keys():
            if m == v:
                for (node, cost) in self.graph[m]:
                    if flag == 1:
                        if node == u:
                            flag = 0
                            self.graph[m].remove((node, cost))
                            self.graph[m].append((node, c))

        if flag == 1:
            self.graph[u].append(value)
            value = (u, c)
            self.graph[v].append(value)


# function for DFS
def dfs(adj_list, start_node, target_node):
    stack.append(start_node)
    visited.add(start_node)

    if start_node == target_node:
        return 1

    for neighbour in adj_list[start_node]:
        if neighbour not in visited:
            print(neighbour, end=" ")
            result = dfs(adj_list, neighbour, target_node)
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

        for (neighbour, cost) in graph.graph[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.put(neighbour)


g = Graph2()


def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost

    return total_cost


def ucs(g, start, goal):
    visited2 = []
    queue2 = [[(start, 0)]]

    while queue2:
        queue2.sort(key=path_cost)
        path = queue2.pop(0)
        node = path[-1][0]

        if node in visited2:
            continue

        visited2.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = g.graph.get(node, [])
            for (node1, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node1, cost))
                queue2.append(new_path)


n = 0

e = 0

# loop for option choosing
while True:
    choice = int(input(
        "\n ---- Menu ----\n1. Add node\n2. Add edge\n3. Delete node\n4. Delete edge\n5. Display graph\n6. BFS\n7. "
        "DFS\n8. Add cost\n9. Uniformed cost search\n10. Exit\n"))
    if choice == 1:
        node = input(f"Enter node {n + 1}: ")
        g.add_node(node)
        n = n + 1
    elif choice == 2:
        u, v = input(f"Enter edge {e + 1}: ").split(" ")
        g.add_edgee(u, v)
        e = e + 1
    elif choice == 3:
        d_node = input("Enter node to delete: ")
        g.delete_node(d_node)
        n = n - 1
    elif choice == 4:
        e1, e2 = input("Enter edge to delete: ").split(" ")
        g.delete_edge(e1, e2)
        e = e - 1
    elif choice == 5:
        g.display()
    elif choice == 6:
        visited = set()
        path = []
        queue = Queue()

        start_node = input("Enter start node:")
        target_node = input("Enter target node:")

        bfs(g, start_node, target_node)
    elif choice == 7:
        start_node = input("Enter start node:")
        target_node = input("Enter target node:")
        visited = set()
        stack = []
        print(start_node, end=" ")
        # DFS
        nodes = []
        adjacent_list = {}
        for m in g.graph.keys():
            nodes.append(m)
            adjacent_list[m] = []
            for (x, y) in g.graph[m]:
                adjacent_list[m].append(x)

        dfs(adjacent_list, start_node, target_node)  # =-------implement

    elif choice == 8:
        # add cost
        e = int(input("Enter no.of edges: "))
        for i in range(e):
            u, v = input(f"Enter edge {i + 1}: ").split(" ")
            c = int(input(f"Enter cost for edge {i + 1}: "))
            # print("u: ", u)
            # print("v: ", v)
            # print("c: ", c)
            g.add_edge(u, v, c)
    elif choice == 9:
        # UCS
        start_node = input("Enter start node:")
        target_node = input("Enter target node:")

        result = ucs(g, start_node, target_node)

        print("UCS: ", result)
        print("Cost: ", path_cost(result))
    elif choice == 10:
        # exit--
        break
    else:
        print("Enter valid option")
