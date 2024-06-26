import random
import pmx
import edge_crossover

def crossover_main(parent1, parent2, rate, crossover_type=0):
    crossover_rate = rate # The probability that crossover will occur.
    crossover_occurs = random.random()

    # Perform partially mapped crossover (PMX). PMX chosen for adjacency preservation.
    if crossover_rate > crossover_occurs:
        # Perform PMX on offspring1.
        if crossover_type == 0:
            offspring1 = pmx.pmx(parent1, parent2)
            # Perform PMX on offspring2, with the role of the parents reversed from offspring1.
            offspring2 = pmx.pmx(parent2, parent1)
        else:
            offspring1 = edge_crossover.crossover(parent1, parent2)
    # Crossover does not occur, directly copy parents as offspring.
    else:
        offspring1 = parent1
        offspring2 = parent2

    if crossover_type == 0:
        offsprings = [offspring1, offspring2]
        return offsprings
    else:
        return offspring1