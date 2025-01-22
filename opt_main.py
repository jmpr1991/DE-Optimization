import constants
import initialization
import mutation
import recombination

import numpy as np

def main():

    # raise an error in case some of these constants are not properly set
    assert 'SPHERE' or 'SCHWEFEL' == constants.FUNCTION


    # initialize success rate and success mean evaluations number (pex) parameters
    success_rate = 0
    pex = []
    gen_converge= []
    best_adaptation_value_vector = []

    for execution_i in range(constants.N_EXECUTIONS):

        print("execution {}".format(execution_i+1), "on going")

        # Initialization of variables
        best_adaptation_value = np.full(shape=constants.N_GENERATIONS, fill_value=np.nan)
        mean_adaptation_value = np.full(shape=constants.N_GENERATIONS, fill_value=np.nan)
        std_adaptation_value = np.full(shape=constants.N_GENERATIONS, fill_value=np.nan)

        # Initialization of the population
        parent_population = initialization.initialization_function()

        # Evolution Strategy loop
        gen = 0
        while gen < constants.N_GENERATIONS:

            # Mutation
            mutated_vector = mutation.mutation_function(parent_population)

            # Recombination
            recombined_vector = recombination.recombination_function(parent_population, mutated_vector)

            # Parent selection and recombination




            # Survival selection

            #save the best adaptation value


            # compute the first termination condition (optimum found)

            # compute the second termination condition (algorithm blocked in a local minimum)


            # jump to next generation
            gen = gen + 1

    # print statistics


    # print progress curve of the last execution


if __name__ == "__main__":
    main()
