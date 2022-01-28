from chromosome import Chromosome
from params import *

class Population:
    def __init__(self):
        self.chromosomes = []
        i = 0
        while i < POPULATION_SIZE :
            self.chromosomes.append( Chromosome() )
            i += 1

        self.chromosomes.sort(key=lambda x: x.get_fitness(), reverse=False) # low to high
    
    def get_chromosomes(self):
        return self.chromosomes

    def print_population(self, gen_number):
        print("\n-----------------------Generation Summary---------------------------")
        print("--------------------------------------------------------------------")
        print("Generation #", gen_number, "| Fittest chromosome fitness:", self.get_chromosomes()[0].get_fitness())
        print("Target chromosome", TARGET_CHROMOSOME)
        print("--------------------------------------------------------------------")
        i = 0
        for x in self.get_chromosomes():
            print("Chromosome #",i," :",x,"| Fitness", x.get_fitness())
            i += 1    
