import constants

import numpy as np

def initialization_function():
    """
    This function initializes the first population to start with the evolution strategy
    :return: initial_population: initial population vector
    """
    # vector initialization, depends on the mutation type
    initial_population = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)

    # initialization of the population depending on the function to analyze
    for i in range(constants.POPULATION_SIZE):
        for j in range(constants.DIM):
            if constants.FUNCTION == 'SPHERE':
                initial_population[j, i] = np.random.uniform(0, 1) * (constants.SHIFTED_SPH_STOP -
                                                                      constants.SHIFTED_SPH_START) + constants.SHIFTED_SPH_START

            if constants.FUNCTION == 'SCHWEFEL':
                initial_population[j, i] = np.random.uniform(0, 1) * (constants.SCHWEFEL_STOP -
                                                                      constants.SCHWEFEL_START) + constants.SCHWEFEL_START

    return initial_population
