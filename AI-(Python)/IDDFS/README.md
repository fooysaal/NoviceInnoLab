# Iterative Deepening Depth First Search (IDDFS) Pathfinding

This Python program implements the **Iterative Deepening Depth First Search (IDDFS)** algorithm to find a path from a starting point to a target point in a 2D grid. The grid is composed of cells that are either walkable (represented by `0`) or blocked (represented by `1`). The program performs a depth-limited DFS and iterates through increasing depths until a path is found or the maximum depth is reached.

## Features

- Implements **IDDFS** for pathfinding in a 2D grid.
- The grid is customizable via user input (number of rows, columns, and the grid layout).
- The program considers only **walkable** cells (`0`).
- Outputs the path found (if any) and the traversal order of cells.

## How It Works

1. The user is prompted to input a grid of integers (where `0` represents a walkable cell and `1` represents a blocked cell).
2. The user inputs the start and target positions (as coordinates in the grid).
3. The program performs **Iterative Deepening Depth First Search (IDDFS)** starting from the initial depth of `0` and increasing depth limits until the path is found or the maximum depth is reached.
4. If a path is found, the program prints the path and the traversal order. If no path is found, the program outputs a message indicating failure.

## Usage

### Input Format

1. Enter the number of rows and columns of the grid.
2. Enter each row of the grid as a space-separated list of integers (`0` for walkable cells, `1` for blocked cells).
3. Enter the start and target positions as `x y` coordinates.
