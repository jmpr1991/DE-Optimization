"""
This file contain the constants of the tsp problem
"""

# random seed
import numpy as np
np.random.seed(2) #seed of the random function to avoid errors in the vector generator

# function constants
PLOT_2D = False

SHIFTED_SPH_CTE = 10 # shifter sphere constant
SHIFTED_SPH_START = -100 # shifted sphere function limits
SHIFTED_SPH_STOP = 100 # shifted sphere function limits

SCHWEFEL_CTE = 418.9829 # Schwefel constant
SCHWEFEL_START = -500 # Schwefel function limits
SCHWEFEL_STOP = 500 # Schwefel function limits

MIN = 0 # Minimum of the function. The minimum is shared by Sphere and Schwefel functions with this configuration

#problem characteristics
FUNCTION = 'SCHWEFEL' # parameter to indicate the function to optimize 'SPHERE' or 'SCHWEFEL'

N_EXECUTIONS = 1 #number of executions
N_GENERATIONS = 1200 #number of generations
DIM = 10 # function dimension
POPULATION_SIZE = 30 # population size
ALGO_TYPE = 'DE/best/1/bin' # type of Differential Evolution algorithm selected 'DE/rand/1/bin' or 'DE/best/1/bin'
FACTOR = 0.8 #mutation factor

