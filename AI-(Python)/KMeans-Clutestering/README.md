# 🧠 K-Means Clustering with Manhattan Distance (Python Project)

This project implements a simple version of the **K-Means clustering algorithm** using the **Manhattan distance** metric. It generates random data points and cluster centers, performs clustering, and then visualizes the result using a text-based 2D matrix printed in the terminal.

---

## 📌 Objectives

- Generate and save **100 random Cartesian points** and **10 initial cluster centers**.
- Implement a **modified K-Means algorithm** using **Manhattan distance**.
- Visualize clustered data using a **text-based 2D matrix**, printed using only the `print()` function.

---

## 📊 Example Visualization (Terminal Output)

Each cell represents a grid coordinate:

    *   *     *     C      *      
 *   *    * *     *     * *   *   

     *     *C   *   *     *   *  

  *    *   *  *  * *     *   *    
*   *      * *    *  *C      *    
     *     * *    * *      *    * 


Legend:
- `*` = Data point
- `C` = Cluster center

---

## 🧮 Algorithm Overview

1. **Generate Data**:
   - 100 random 2D points.
   - 10 random initial cluster centers.
   - Save to `data.txt`.

2. **Clustering**:
   - Use **Manhattan distance**:  
     \[
     d(p_1, p_2) = |x_1 - x_2| + |y_1 - y_2|
     \]
   - Assign each point to the closest cluster.
   - Recalculate cluster centers using the average of assigned points (rounded).

3. **Visualization**:
   - Render a 2D matrix (40x20).
   - Display using `print()` with symbols `*` and `C`.

---