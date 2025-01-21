import constants

import numpy as np

def shifted_sph_fun(x_vector):
    """
    Shifted sphere function
    :param x_vector: input vector
    :return: f(x_vector)
    """

    sph = 0
    for i in range(len(x_vector)):
        sph = sph + (x_vector[i] - constants.SHIFTED_SPH_CTE)**2

    return sph

def schwefel_fun(x_vector, dim):
    """
    schwefel function
    :param x_vector: input vector
    :param dim: space dimension
    :return: f(x_vector)
    """

    schwefel_i = 0
    for i in range(len(x_vector)):
        schwefel_i = schwefel_i + (-x_vector[i] * np.sin(np.sqrt(abs(x_vector[i]))))
    schwefel = schwefel_i + constants.SCHWEFEL_CTE * dim

    return schwefel
