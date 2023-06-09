from ortools.algorithms.pywrapknapsack_solver import KnapsackSolver
from knapsack01_algorithms.cp import ortools_solve


def knapsack01_bruteforce_ortools(dataset, budget):
    return ortools_solve(KnapsackSolver.KNAPSACK_BRUTE_FORCE_SOLVER, dataset, budget)
