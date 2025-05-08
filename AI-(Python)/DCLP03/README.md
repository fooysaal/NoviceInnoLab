# 🎯 Genetic Algorithm: Find List with Target Product

This project uses a **Genetic Algorithm** to find a list of `k` integers (from 1 to 9) such that their **product equals a given target number `T`**.

---

## 🧠 Problem Statement

Given:
- A **target number** `T`
- A **list length** `k`

The goal is to find a list of `k` numbers (1 to 9) such that:

number1 × number2 × ... × number_k = T


---

## 📌 Example

### Case 1

Input:
T = 12
k = 3

Possible Output:
2 2 3


### Case 2

Input:
T = 18
k = 3

Possible Output:
3 3 2


---

## 🧬 How It Works (Genetic Algorithm)

1. **Initialization**: Start with a random population of lists.
2. **Fitness Function**: Measures how close the product of a list is to `T`.
3. **Selection**: Choose the best-performing lists (closest to `T`).
4. **Crossover**: Combine two lists to create a new one.
5. **Mutation**: Occasionally change elements to introduce variation.
6. **Repeat**: Continue for several generations or until a solution is found.

---