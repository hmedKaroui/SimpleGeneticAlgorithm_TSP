from population import Population
from ga import GeneticAlgorithm

generation_number = 0
population = Population()
population.print_population(generation_number)

while population.get_chromosomes()[0].get_fitness() > 0 :
    generation_number += 1
    population = GeneticAlgorithm.evolve(population)
    population.print_population(generation_number)