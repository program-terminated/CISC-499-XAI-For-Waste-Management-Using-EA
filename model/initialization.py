import numpy as np

def pop_init(pop_size, bin_info, bin_count):
    population = []
    while len(population) < pop_size:
        # Each individual is represented by a list of bin indices
        indiv = []
        b = random.randint(0,bin_count-1)
        # actions is a list of at most 4 bins, representing the nearest
        # bin in each direction from the current one.
        actions = bin_info.get_actions(b)
        indiv.append(b)

        while(len(actions) > 0):
            b = random.choice(actions)
            indiv.append(b)
            actions = bin_info.get_actions(b)
            # Removes actions that would lead to previously visited states (bins in indiv)
            temp = actions.copy()
            for a in temp:
                if a in indiv:
                    actions.remove(a)
        population.append(indiv)

    return population

if __name__ ==  "__main__":
    import environment as en
    bin_info = en.BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')
    bin_count = len(bin_info.bins)
    print(pop_init(5,bin_info,bin_count))