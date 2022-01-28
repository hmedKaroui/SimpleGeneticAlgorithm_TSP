import random
from params import *
class Chromosome:
    def __init__(self):
        self.genes = []
        i=0
        while i<NB_GENES:
            self.genes.append(random.randint(0,1))
            i+=1

    def get_genes(self):
        return self.genes

    def get_fitness(self):
        # this init is very important , 
        #diffrence minimisation
        fitness = 0
        for i in range(NB_GENES):
            if(self.genes[i] != TARGET_CHROMOSOME[i]):
                fitness += 1
        return fitness

    def __str__(self):
        return self.genes.__str__()