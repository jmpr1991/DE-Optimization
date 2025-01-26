import constants
import functions

import numpy as np

def survival_selection_function(recombined_vector, objective_vector):
    """
    This function computes the survival vector and adaptation value from the recombined vector and parent vector
    :param recombined_vector: recombined vector
    :param objective_vector: parent vector
    :return: survival_vector: survival vector
    :return: survival_adaptation_value: adaptation value of the survival vectors
    """
    # initialize the survival vector and adaptation value
    survival_vector = np.full(shape=(constants.DIM, constants.POPULATION_SIZE), fill_value=np.nan)
    survival_adaptation_value = np.full(shape=(constants.POPULATION_SIZE, 1), fill_value=np.nan)

    #compute the survival vectors and survival adaptation value by comparing the adaptation value of the recombined_vector and parent_vector
    for i in range(constants.POPULATION_SIZE):

        #sphere case
        if constants.FUNCTION == 'SPHERE':
            recombined_adaptation_value = functions.shifted_sph_fun(recombined_vector[:, i])
            objective_adaptation_value = functions.shifted_sph_fun(objective_vector[:, i])

            #compare adaptation values
            if recombined_adaptation_value <= objective_adaptation_value:
                survival_vector[:, i] = recombined_vector[:, i]
                survival_adaptation_value[i] = recombined_adaptation_value
            else:
                survival_vector[:, i] = objective_vector[:, i]
                survival_adaptation_value[i] = objective_adaptation_value

        # schwefel case
        if constants.FUNCTION == 'SCHWEFEL':
            recombined_adaptation_value = functions.schwefel_fun(recombined_vector[:, i], constants.DIM)
            objective_adaptation_value = functions.schwefel_fun(objective_vector[:, i], constants.DIM)

            # compare adaptation values
            if recombined_adaptation_value <= objective_adaptation_value:
                survival_vector[:, i] = recombined_vector[:, i]
                survival_adaptation_value[i] = recombined_adaptation_value
            else:
                survival_vector[:, i] = objective_vector[:, i]
                survival_adaptation_value[i] = objective_adaptation_value

    return survival_vector, survival_adaptation_value