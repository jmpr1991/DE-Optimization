import random

import constants

import numpy as np

def recombination_function(parent_vector, mutated_vector):

    # vector initialization
    recombined_vector = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)

    # create the recombined vector
    for i in range(constants.POPULATION_SIZE):
        #random index crate to share at least one gen of the mutated vector to the recombined vector, independently from the croos probability
        alpha_i = random.randint(0,constants.DIM-1)

        for j in range(constants.DIM):
            if np.random.uniform(0, 1) <= constants.CROSS_PROB or alpha_i == j:
                recombined_vector[j, i] = mutated_vector[j, i]
            else:
                recombined_vector[j, i] = parent_vector[j, i]

    return recombined_vector