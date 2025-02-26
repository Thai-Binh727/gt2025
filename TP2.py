from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = defaultdict(set)

    def add_edge(self, src, dest):
        self.adj_list[src].add(dest)

    def get_adj_matrix(self):
        return [[1 if j in self.adj_list[i] else 0 for j in range(1, self.n + 1)] for i in range(1, self.n + 1)]

    def count_weak_components(self):
        visited = set()
        components = 0
        undirected_graph = {node: set(neighbors) for node, neighbors in self.adj_list.items()}
        for src, neighbors in self.adj_list.items():
            for dest in neighbors:
                undirected_graph.setdefault(dest, set()).add(src)

        def bfs(start):
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in undirected_graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        for node in range(1, self.n + 1):
            if node not in visited:
                components += 1
                visited.add(node)
                bfs(node)

        return components

    def count_strong_components(self):
        visited, finish_order = set(), []

        def dfs(node):
            visited.add(node)
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
            finish_order.append(node)

        for node in range(1, self.n + 1):
            if node not in visited:
                dfs(node)

        transposed = Graph(self.n)
        for src, neighbors in self.adj_list.items():
            for dest in neighbors:
                transposed.add_edge(dest, src)

        visited.clear()
        components = 0

        def dfs_transposed(node):
            visited.add(node)
            for neighbor in transposed.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs_transposed(neighbor)

        while finish_order:
            node = finish_order.pop()
            if node not in visited:
                components += 1
                dfs_transposed(node)

        return components


n = 9
graph = Graph(n)
edges = [(1, 2), (1, 4), (2, 3), (2, 6), (5, 4), (5, 9), (5, 5),
         (6, 3), (6, 4), (7, 3), (7, 5), (7, 6), (7, 8), (8, 3), (8, 9)]
for src, dest in edges:
    graph.add_edge(src, dest)

print("Adjacency Matrix:")
for row in graph.get_adj_matrix():
    print(row)

print("\nNumber of Weakly Connected Components:", graph.count_weak_components())
print("Number of Strongly Connected Components:", graph.count_strong_components())
