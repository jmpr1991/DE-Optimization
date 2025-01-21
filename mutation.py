import constants
import functions

import numpy as np
import random

def mutation_function(parent_vector):
    """
    This function mutates the offspring vector. 2 types of mutation are implemented: non correlated 1 step and
    non correlated n steps
    :param parent_vector: vector compiling the offspring individuals
    :return: mutated_vector: vector with the mutated offspring
    """
    # initialize the mutated vector
    mutated_vector = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)

    # compute the mutates vector depending on the selected configuration
    if constants.ALGO_TYPE == 'DE/rand/1/bin':
        mutated_vector = mutation_rand(parent_vector)

    if constants.ALGO_TYPE == 'DE/best/1/bin':
        mutated_vector = mutation_best(parent_vector)

    return mutated_vector

def mutation_rand(parent_vector):
    """
    This function mutates the offspring vector. 2 types of mutation are implemented: non correlated 1 step and
    non correlated n steps
    :param parent_vector: vector compiling the offspring individuals
    :return: mutated_vector: vector with the mutated offspring
    """
    #initialize the mutated vector
    mutated_vector = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)

    #create the index vector for identification
    index_vector = np.linspace(0, constants.POPULATION_SIZE - 1, num=constants.POPULATION_SIZE, dtype=int)

    # create the mutated vector
    for i in range(constants.POPULATION_SIZE):
        # select 3 random indexes to make the differences to develop the mutated vector
        selected_indexes = random.sample(list(index_vector), 3)

        for j in range(constants.DIM):
            mutated_vector[j,i] = parent_vector[j, selected_indexes[2]] + constants.FACTOR * (parent_vector[j, selected_indexes[0]]
                                                                                    - parent_vector[j, selected_indexes[1]])

    return mutated_vector

def mutation_best(parent_vector):

    # initialize the mutated vector and adaptation value
    mutated_vector = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)
    adaptation_value = np.full(shape=(constants.POPULATION_SIZE, 2), fill_value=np.nan)

    # evaluate parent vector
    for i in range(constants.POPULATION_SIZE):
        # save the index to support on the sort process
        adaptation_value[i, 1] = i

        #compute the adaptation value of the function
        if constants.FUNCTION == 'SPHERE':
            adaptation_value[i, 0] = functions.shifted_sph_fun(parent_vector[:, i])

        if constants.FUNCTION == 'SCHWEFEL':
            adaptation_value[i, 0] = functions.schwefel_fun(parent_vector[:, i], constants.DIM)

    # sort the adaptation value to pick the minimum
    sorted_adaptation_value = adaptation_value[np.argsort(adaptation_value[:, 0]), :]

    #create the index vector for identification
    index_vector = np.linspace(0, constants.POPULATION_SIZE - 1, num=constants.POPULATION_SIZE, dtype=int)

    # create the mutated vector
    for i in range(constants.POPULATION_SIZE):
        # select 3 random indexes to make the differences to develop the mutated vector
        selected_indexes = random.sample(list(index_vector), 2)

        for j in range(constants.DIM):
            mutated_vector[j,i] = parent_vector[j, sorted_adaptation_value[0, 1]] + constants.FACTOR * (parent_vector[j, selected_indexes[0]]
                                                                                    - parent_vector[j, selected_indexes[1]])


    return mutated_vector