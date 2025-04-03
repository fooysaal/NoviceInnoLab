def is_safe(graph, colors, vertex, color):
    # Check if any adjacent vertex has the same color
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, colors, vertex, K):
    # If all vertices are assigned a color then return True
    if vertex == len(graph):
        return True

    # Try different colors for vertex
    for color in range(1, K + 1):
        if is_safe(graph, colors, vertex, color):
            colors[vertex] = color
            if graph_coloring_util(graph, colors, vertex + 1, K):
                return True
            # Backtrack
            colors[vertex] = 0

    return False

def graph_coloring(graph, N, M, K):
    # Initialize all vertices as uncolored (0)
    colors = [0] * N

    # Call the utility function to solve the problem
    if graph_coloring_util(graph, colors, 0, K):
        print(f"Coloring Possible with {K} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {K} Colors")

def main():
    # Take user input
    N, M, K = map(int, input("Enter number of vertices, edges, and colors (N M K): ").split())
    
    # Initialize the graph as an empty adjacency list
    graph = {i: [] for i in range(N)}
    
    print(f"Enter {M} edges (u v) pairs:")
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Call the function to check for graph coloring
    graph_coloring(graph, N, M, K)

if __name__ == "__main__":
    main()
