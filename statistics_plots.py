import constants
import functions

import numpy as np
import matplotlib.pyplot as plt

def statistics(success_rate, pex, best_adaptation_value_vector, gen_converge):
    """
    This function print the statistics of the evolution strategy
    :param success_rate: number of successful executions
    :param pex: number of generations to succeed
    :param best_adaptation_value_vector: vector compiling the best adaptation values of each execution
    :param gen_converge: vector compiling the number of generations needed to converge of each execution
    """

    # Success rate computation
    print("\n Statistics:")

    print("TE = ", success_rate / constants.N_EXECUTIONS * 100, "%")
    if success_rate == 0:
        print("PEX = n/a")

    else:
        print("PEX = ", np.mean(pex), " +/-", np.std(pex))

    # VAMM computation
    vamm = sum(best_adaptation_value_vector) / constants.N_EXECUTIONS
    vamm_std = np.std(best_adaptation_value_vector)
    print('VAMM = ', vamm, '+/-', vamm_std)
    print("Generations to converge = ", np.mean(gen_converge), '+/-', np.std(gen_converge))

def graphics(best_adaptation_value, mean_adaptation_value, std_adaptation_value):
    """
    This function prints the progress curve
    :param best_adaptation_value: vector with the best adaptation value in each generation
    :param mean_adaptation_value: vector with the mean adaptation value in each generation
    :param std_adaptation_value: vector with the std of the adaptation value vector in each generation
    :return:
    """
    # print the convergence of the best individual
    plt.plot(np.array(best_adaptation_value), linewidth=0.6)
    plt.plot(np.array(mean_adaptation_value), linewidth=0.6, color='darkred')
    plt.fill_between(x=[i for i in range(len(np.array(mean_adaptation_value)))], y1=np.array(mean_adaptation_value) - np.array(std_adaptation_value),
                     y2=np.array(mean_adaptation_value) + np.array(std_adaptation_value), color='gray', alpha=0.2)
    plt.title('Progress curve '
              '\n Best individual and population mean for each generation')
    plt.xlabel('Generation')
    plt.ylabel('Adaptation function - f(x)')
    plt.legend(['best individual', 'population mean', 'standard deviation'])
    plt.show()