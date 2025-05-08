import random

N = 8  # Number of queens and size of the board (N x N)
POPULATION_SIZE = 100
MUTATION_RATE = 0.03
MAX_GENERATIONS = 1000


def generate_individual():
    """Generates a random individual (a board configuration)."""
    return [random.randint(0, N - 1) for _ in range(N)]

def generate_population():
    """Creates the initial population of individuals."""
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def fitness(individual):
    """
    Calculates the fitness score of an individual.
    The score is based on the number of non-attacking queen pairs.
    """
    non_attacking = 0
    total_pairs = N * (N - 1) // 2  # Max number of non-attacking pairs
    for i in range(N):
        for j in range(i + 1, N):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking / total_pairs  # Normalize to range [0, 1]

def selection(population):
    """
    Selects an individual from the population using roulette wheel selection.
    """
    weighted = [(ind, fitness(ind)) for ind in population]
    total_fitness = sum(f for _, f in weighted)
    r = random.uniform(0, total_fitness)
    cumulative = 0
    for ind, f in weighted:
        cumulative += f
        if cumulative >= r:
            return ind
    return population[0]  # fallback

def crossover(parent1, parent2):
    """
    Performs single-point crossover between two parents.
    """
    point = random.randint(0, N - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual):
    """
    Randomly mutates an individual with a small probability.
    """
    if random.random() < MUTATION_RATE:
        index = random.randint(0, N - 1)
        value = random.randint(0, N - 1)
        individual[index] = value
    return individual

def genetic_algorithm():
    population = generate_population()

    for generation in range(MAX_GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)

        if fitness(population[0]) == 1.0:
            print(f"\n Solution found in generation {generation}")
            return population[0]

        next_generation = []

        for _ in range(POPULATION_SIZE):
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)

        population = next_generation

    print("\n No solution found within the generation limit.")
    return None

if __name__ == "__main__":
    solution = genetic_algorithm()
    if solution:
        print("\n🧩 Solution (row positions of queens in columns):")
        print(solution)

        # Display the board
        print("\n Chessboard:")
        for row in range(N):
            line = ""
            for col in range(N):
                if solution[col] == row:
                    line += " Q "
                else:
                    line += " . "
            print(line)
