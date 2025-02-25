# Graph Traversal

This folder contains a Python program that generates a random **N×N grid** (with N between 4 and 7) to simulate a graph traversal problem. The goal of the program is to find a path from a **source** state to a **goal** state using **Depth-First Search (DFS)**.

## Problem Description

The program generates an N×N grid where:

- **Source** and **Goal** are non-obstacle states.
- The program uses **DFS** to find a path from the source to the goal.
- The following are printed:
  - The generated grid with source, goal, and obstacles.
  - The **source** and **goal** positions.
  - The **DFS path** from the source to the goal.
  - The **topological order** of the node traversal during DFS.

## How it Works

1. **Grid Generation**: The program generates a random N×N grid with a source and goal position (both non-obstacles).
2. **DFS Traversal**: Using DFS, the program explores the grid from the source node to find a path to the goal, traversing nodes in depth-first order.

3. **Output**:
   - The generated grid with the source, goal, and obstacles displayed.
   - The DFS path showing the sequence of nodes from source to goal.
   - The order of node traversal during DFS.
   
## How to Use

1. Clone this repository or navigate to the **Graph Traversal** subfolder.
2. Run the script to generate a random grid and perform DFS traversal.
3. The program will print the generated grid, DFS path, and topological traversal order.