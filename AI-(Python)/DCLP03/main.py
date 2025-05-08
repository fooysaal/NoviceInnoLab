import random
import math

# This function checks how close the product of the list is to the target
def fitness(individual, target):
    product = math.prod(individual)  # Multiply all numbers in the list
    return 1 / (1 + abs(product - target))  # Smaller difference = better fitness

# Create a random list of k numbers between 1 and 9
def generate_individual(k):
    return [random.randint(1, 9) for _ in range(k)]

# Combine two parents to make a child
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)  # Random crossover point
    return parent1[:point] + parent2[point:]     # Mix the genes

# Randomly change some numbers in the list
def mutate(individual, mutation_rate=0.1):
    new_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            new_individual.append(random.randint(1, 9))  # Mutate
        else:
            new_individual.append(gene)  # Keep the same
    return new_individual

# Main algorithm to find the list
def genetic_algorithm(target, k, population_size=100, generations=1000):
    # Start with random population
    population = [generate_individual(k) for _ in range(population_size)]

    for generation in range(generations):
        # Sort population by how good they are (fitness)
        population.sort(key=lambda x: fitness(x, target), reverse=True)

        # Check if the best one is a perfect match
        if math.prod(population[0]) == target:
            return population[0]

        # Select the best 20% to be parents
        best = population[:population_size // 5]

        # Make new population using crossover and mutation
        new_population = []
        while len(new_population) < population_size:
            parent1 = random.choice(best)
            parent2 = random.choice(best)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population  # Replace old population

    return None  # No exact match found

# ---- Main Program Starts Here ----

# Ask the user for input
try:
    T = int(input("Enter the target product (T): "))
    k = int(input("Enter how many numbers should be in the list (k): "))

    # Run the genetic algorithm
    result = genetic_algorithm(T, k)

    # Show the result
    if result:
        print("A list with product", T, "is:", *result)
    else:
        print("Sorry, no solution found.")
except ValueError:
    print("Please enter valid whole numbers for T and k.")
