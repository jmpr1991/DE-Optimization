"""
This file contain the constants of the tsp problem
"""

# random seed
import numpy as np
import random
np.random.seed(2) #seed of the random function to avoid errors in the vector generator
random.seed(2)

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
ALGO_TYPE = 'DE/best/1/bin' # type of Differential Evolution algorithm selected 'DE/rand/1/bin' or 'DE/best/1/bin'

# constant parameters
N_EXECUTIONS = 10 #number of executions
N_GENERATIONS = 1200 #number of generations
DIM = 10 # function dimension
POPULATION_SIZE = 30 # population size
MUTATION_FACTOR = 0.5 #mutation factor
CROSS_PROB = 0.5 # cross probability
ERROR = 1e-3 # allowed error to converge

