import constants
import initialization
import mutation
import recombination
import survival_selection
import statistics_plots

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

            # Survival selection
            parent_population, parent_adaptation_value = survival_selection.survival_selection_function(recombined_vector,
                                                                                                        parent_population)

            #save the best adaptation value
            best_adaptation_value[gen] = np.min(parent_adaptation_value)
            mean_adaptation_value[gen] = np.mean(parent_adaptation_value)
            std_adaptation_value[gen] = np.std(parent_adaptation_value)

            # compute the first termination condition (optimum found)
            if abs(best_adaptation_value[gen] - constants.MIN) < constants.ERROR:
                success_rate = success_rate + 1
                best_adaptation_value_vector.append(best_adaptation_value[gen])
                pex.append(gen)
                gen_converge.append(gen)
                break

            # compute the second termination condition (algorithm blocked in a local minimum)
            if (abs(best_adaptation_value[gen] - best_adaptation_value[gen-1]) < constants.ERROR**2 and
                    abs(best_adaptation_value[gen] - best_adaptation_value[gen-1]) != 0): #this termination condition is injected to avoid false terminations when elitism is applied
                best_adaptation_value_vector.append(best_adaptation_value[gen])
                gen_converge.append(gen)
                break

            # jump to next generation
            gen = gen + 1

    # print statistics
    statistics_plots.statistics(success_rate, pex, best_adaptation_value_vector, gen_converge)

    # print progress curve of the last execution
    statistics_plots.graphics(best_adaptation_value, mean_adaptation_value, std_adaptation_value)

if __name__ == "__main__":
    main()
