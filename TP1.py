class Graph:
    def __init__(self):
        self.graph = {}

    # Add an edge to the graph
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    # DFS to check if a path exists from source to destination
    def dfs(self, start, end, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)

        if start == end:
            return True

        # Explore all neighbors of the current node
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                if self.dfs(neighbor, end, visited):
                    return True
        return False

    # Function to check if a path exists from source to destination
    def path_exists(self, start, end):
        return self.dfs(start, end)

# Main function to get user input and test path existence
def main():
    g = Graph()

    # Add edges to the graph (can be modified as needed)
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'd')
    g.add_edge('a', 'd')
    g.add_edge('d', 'e')

    # Get user input for two nodes
    start = input("Enter the start node: ")
    end = input("Enter the end node: ")

    # Check if a path exists and print the result
    if g.path_exists(start, end):
        print(f"Path exists from {start} to {end}.")
    else:
        print(f"No path exists from {start} to {end}.")

if __name__ == "__main__":
    main()
