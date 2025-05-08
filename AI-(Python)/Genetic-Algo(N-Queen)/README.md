# 🧬 N-Queen Problem using Genetic Algorithm

This project implements a **Genetic Algorithm** to solve the **N-Queen Problem** — a classic combinatorial problem where the goal is to place `N` queens on an `N×N` chessboard such that no two queens threaten each other.

---

## 🧠 Problem Statement

Place `N` queens on a chessboard of size `N x N` so that:

- No two queens are in the same row
- No two queens are in the same column
- No two queens are on the same diagonal

Traditional backtracking solutions work, but become inefficient for larger `N`. This project uses a **Genetic Algorithm** approach for better scalability.

---

## 🚀 Features

- Adjustable `N` for different board sizes
- Fitness-based selection using roulette wheel
- Crossover and mutation operators
- Chessboard output visualization
- Simple and customizable code

---

## 🧬 Genetic Algorithm Overview

| Step           | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Encoding**   | Each individual is a list of integers; index = column, value = row of queen |
| **Fitness**    | Measures number of non-attacking queen pairs                                |
| **Selection**  | Roulette wheel based on fitness                                              |
| **Crossover**  | Single-point crossover between two parents                                   |
| **Mutation**   | Randomly alters a queen’s position with a low probability                   |

---

## 📦 Requirements

- Python 3.x
- No external libraries required

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/n-queen-genetic-algorithm.git
cd n-queen-genetic-algorithm
