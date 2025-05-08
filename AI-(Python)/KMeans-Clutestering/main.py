import random

WIDTH = 40
HEIGHT = 20
NUM_POINTS = 100
NUM_CLUSTERS = 10
ITERATIONS = 10
DATA_FILE = "data.txt"

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

points = [(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)) for _ in range(NUM_POINTS)]
clusters = [(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)) for _ in range(NUM_CLUSTERS)]

with open(DATA_FILE, "w") as f:
    f.write("POINTS:\n")
    for p in points:
        f.write(f"{p}\n")
    f.write("CLUSTERS:\n")
    for c in clusters:
        f.write(f"{c}\n")

for _ in range(ITERATIONS):
    cluster_assignments = [[] for _ in range(NUM_CLUSTERS)]

    for point in points:
        distances = [manhattan(point, cluster) for cluster in clusters]
        closest_index = distances.index(min(distances))
        cluster_assignments[closest_index].append(point)

    for i in range(NUM_CLUSTERS):
        if cluster_assignments[i]:
            xs = [p[0] for p in cluster_assignments[i]]
            ys = [p[1] for p in cluster_assignments[i]]
            new_x = round(sum(xs) / len(xs))
            new_y = round(sum(ys) / len(ys))
            clusters[i] = (new_x, new_y)

grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

for x, y in points:
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        grid[y][x] = '*'

for x, y in clusters:
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        grid[y][x] = 'C'

print("\nClustered Data Visualization:\n")
for row in reversed(grid):
    print(''.join(row))
