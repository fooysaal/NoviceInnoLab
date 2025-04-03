# Graph Coloring Using Backtracking

## Description

This Python program solves the **Graph Coloring** problem using a backtracking algorithm. Given an undirected graph with `N` vertices and `M` edges, it determines whether it's possible to color the graph using `K` colors such that no two adjacent vertices share the same color.

### Problem Statement
- **Input**: 
  - `N`: Number of vertices (labeled from 0 to `N-1`).
  - `M`: Number of edges in the graph.
  - `K`: Number of available colors.
  - A list of `M` edges, each represented by a pair of vertices `u` and `v` (indicating an undirected edge between vertex `u` and vertex `v`).

- **Output**:
  - The program checks if it's possible to color the graph using the given `K` colors and outputs:
    - If it's possible: the color assignment for each vertex.
    - If it's not possible: a message indicating that the coloring is not feasible with the given `K` colors.

## Algorithm

The program uses a **backtracking algorithm** to try to color each vertex in the graph. For each vertex, it attempts to assign one of the available `K` colors while ensuring that no two adjacent vertices share the same color. If no valid coloring is found, the program backtracks and tries a different color for previous vertices.
