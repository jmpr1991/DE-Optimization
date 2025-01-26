import constants
import functions

import numpy as np
import random

def mutation_function(parent_vector):
    """
    This function mutates the input vector. 2 types of mutation are implemented: 'DE/rand/1/bin' or 'DE/best/1/bin'
    :param parent_vector: vector compiling the input individuals
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
    function implementing the 'DE/rand/1/bin' mutation algorithm
    :param parent_vector: vector compiling the input individuals
    :return: mutated_vector: vector with the mutated offspring
    """
    #initialize the mutated vector
    mutated_vector = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)

    # create the mutated vector
    for i in range(constants.POPULATION_SIZE):

        # create the index vector for identification
        index_vector = list(np.linspace(0, constants.POPULATION_SIZE - 1, num=constants.POPULATION_SIZE, dtype=int))
        #remove objective vector from the list
        index_vector.pop(i)

        # select 3 random indexes to make the differences to develop the mutated vector
        selected_indexes = random.sample(list(index_vector), 3)

        for j in range(constants.DIM):
            mutated_vector[j,i] = parent_vector[j, selected_indexes[2]] + constants.MUTATION_FACTOR * (parent_vector[j, selected_indexes[0]]
                                                                                    - parent_vector[j, selected_indexes[1]])

            # bounce-back method to repair values outside the function space
            # sphere function case
            if constants.FUNCTION == 'SPHERE':
                if mutated_vector[j,i] < constants.SHIFTED_SPH_START:
                    mutated_vector[j, i] = (parent_vector[j, selected_indexes[2]] + np.random.uniform(0,1) *
                                            (constants.SHIFTED_SPH_START -  parent_vector[j, selected_indexes[2]]))
                if mutated_vector[j,i] > constants.SHIFTED_SPH_STOP:
                    mutated_vector[j, i] = (parent_vector[j, selected_indexes[2]] + np.random.uniform(0, 1) *
                                            (constants.SHIFTED_SPH_STOP - parent_vector[j, selected_indexes[2]]))

            # Schwefel function case
            if constants.FUNCTION == 'SCHWEFEL':
                if mutated_vector[j, i] < constants.SCHWEFEL_START:
                    mutated_vector[j, i] = (parent_vector[j, selected_indexes[2]] + np.random.uniform(0, 1) *
                                            (constants.SCHWEFEL_START - parent_vector[j, selected_indexes[2]]))
                if mutated_vector[j, i] > constants.SCHWEFEL_STOP:
                    mutated_vector[j, i] = (parent_vector[j, selected_indexes[2]] + np.random.uniform(0, 1) *
                                            (constants.SCHWEFEL_STOP - parent_vector[j, selected_indexes[2]]))

    return mutated_vector

def mutation_best(parent_vector):
    """
    function implementing the 'DE/best/1/bin' mutation algorithm
    :param parent_vector: vector compiling the input individuals
    :return: mutated_vector: vector with the mutated offspring
    """

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

    # create the mutated vector
    for i in range(constants.POPULATION_SIZE):

        # create the index vector for identification
        index_vector = list(np.linspace(0, constants.POPULATION_SIZE - 1, num=constants.POPULATION_SIZE, dtype=int))
        #remove best vector from the list
        index_vector.pop(int(sorted_adaptation_value[0,1]))

        # select 2 random indexes to make the differences to develop the mutated vector
        selected_indexes = random.sample(list(index_vector), 2)

        for j in range(constants.DIM):
            mutated_vector[j,i] = parent_vector[j, int(sorted_adaptation_value[0, 1])] + constants.MUTATION_FACTOR * (parent_vector[j, selected_indexes[0]]
                                                                                    - parent_vector[j, selected_indexes[1]])

            # bounce-back method to repair values outside the function space
            # sphere function case
            if constants.FUNCTION == 'SPHERE':
                if mutated_vector[j,i] < constants.SHIFTED_SPH_START:
                    mutated_vector[j, i] = (parent_vector[j, int(sorted_adaptation_value[0, 1])] + np.random.uniform(0,1) *
                                            (constants.SHIFTED_SPH_START -  parent_vector[j, int(sorted_adaptation_value[0, 1])]))
                if mutated_vector[j,i] > constants.SHIFTED_SPH_STOP:
                    mutated_vector[j, i] = (parent_vector[j, int(sorted_adaptation_value[0, 1])] + np.random.uniform(0, 1) *
                                            (constants.SHIFTED_SPH_STOP - parent_vector[j, int(sorted_adaptation_value[0, 1])]))

            # Schwefel function case
            if constants.FUNCTION == 'SCHWEFEL':
                if mutated_vector[j, i] < constants.SCHWEFEL_START:
                    mutated_vector[j, i] = (parent_vector[j, int(sorted_adaptation_value[0, 1])] + np.random.uniform(0, 1) *
                                            (constants.SCHWEFEL_START - parent_vector[j, int(sorted_adaptation_value[0, 1])]))
                if mutated_vector[j, i] > constants.SCHWEFEL_STOP:
                    mutated_vector[j, i] = (parent_vector[j, int(sorted_adaptation_value[0, 1])] + np.random.uniform(0, 1) *
                                            (constants.SCHWEFEL_STOP - parent_vector[j, int(sorted_adaptation_value[0, 1])]))

    return mutated_vector