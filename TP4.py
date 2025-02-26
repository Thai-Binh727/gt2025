import heapq


def construct_adjacency_matrix(edges, n):
    return [[1 if (i + 1, j + 1) in edges else 0 for j in range(n)] for i in range(n)]


def inorder_traversal(tree, node):
    if node not in tree:
        return []

    left = inorder_traversal(tree, tree[node][0]) if tree[node] else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []

    return left + [node] + right


# Input Graph Data
edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
n = 8  # Number of nodes

# Step 1: Construct Adjacency Matrix
adj_matrix = construct_adjacency_matrix(edges, n)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Step 2: Convert Graph to Adjacency List for Tree
tree = {
    1: [2, 3],
    2: [5, 6],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}

# Input: Node label (x)
x = int(input("Enter the node label to print subtree in Inorder: "))

# Step 3: Perform Inorder Traversal
inorder_result = inorder_traversal(tree, x)
print(f"Inorder Traversal of subtree rooted at node {x}: {inorder_result}")


def prim(graph, root):
    num_nodes = len(graph)
    mst_edges = []
    visited = [False] * num_nodes
    min_heap = [(0, root, -1)]  # (weight, current_node, parent_node)
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        total_weight += weight
        if parent != -1:
            mst_edges.append((parent + 1, node + 1, weight))  # Convert to 1-based index

        for adj in range(num_nodes):
            if not visited[adj] and graph[node][adj] != float('inf'):
                heapq.heappush(min_heap, (graph[node][adj], adj, node))

    return mst_edges, total_weight


graph = [
    [0, 4, float('inf'), float('inf'), 1, float('inf'), 2, float('inf'), float('inf')],
    [4, 0, 7, float('inf'), float('inf'), 5, float('inf'), float('inf'), float('inf')],
    [float('inf'), 7, 0, 1, float('inf'), 8, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 1, 0, float('inf'), 6, 4, 3, float('inf')],
    [1, float('inf'), float('inf'), float('inf'), 0, 9, 10, float('inf'), float('inf')],
    [float('inf'), 5, 8, 6, 9, 0, float('inf'), float('inf'), 2],
    [2, float('inf'), float('inf'), 4, 10, float('inf'), 2, float('inf'), 8],
    [float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, 8, 1, 0]
]

root_node = int(input("Enter the root node (1-9): ")) - 1  # 1-based to 0-based index
mst_edges, total_weight = prim(graph, root_node)
print("\nPrim's Algorithm - MST edges and weights:")
for edge in mst_edges:
    print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total weight of MST: {total_weight}")


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False


def kruskal(graph):
    num_nodes = len(graph)
    edges = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if graph[i][j] != float('inf'):
                edges.append((graph[i][j], i, j))  # (weight, node1, node2)

    edges.sort()
    uf = UnionFind(num_nodes)
    mst_edges = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((u + 1, v + 1, weight))  # Convert to 1-based index
            total_weight += weight

    return mst_edges, total_weight


mst_edges_kruskal, total_weight_kruskal = kruskal(graph)
print("\nKruskal's Algorithm - MST edges and weights:")
for edge in mst_edges_kruskal:
    print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total weight of MST: {total_weight_kruskal}")