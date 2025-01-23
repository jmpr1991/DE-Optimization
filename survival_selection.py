import constants
import functions

import numpy as np

def survival_selection_function(mutated_vector, parent_vector):

    # initialize the mutated vector
    survival_vector = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)

    for i in range(constants.POPULATION_SIZE):

        if constants.FUNCTION == 'SPHERE':
            mutated_adaptation_value = functions.shifted_sph_fun(mutated_vector[:,i])
            parent_adaptation_value = functions.shifted_sph_fun(parent_vector[:,i])

            if mutated_adaptation_value <= parent_adaptation_value:
                survival_vector[:, i] = mutated_vector[:,i]
            else:
                survival_vector[:, i] = parent_vector[:, i]

        if constants.FUNCTION == 'SCHWEFEL':
            mutated_adaptation_value = functions.schwefel_fun(mutated_vector[:, i], constants.DIM)
            parent_adaptation_value = functions.schwefel_fun(parent_vector[:, i], constants.DIM)

            if mutated_adaptation_value <= parent_adaptation_value:
                survival_vector[:, i] = mutated_vector[:, i]
            else:
                survival_vector[:, i] = parent_vector[:, i]

    return survival_vector