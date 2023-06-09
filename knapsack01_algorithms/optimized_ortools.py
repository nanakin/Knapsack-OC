from ortools.algorithms.pywrapknapsack_solver import KnapsackSolver
from knapsack01_algorithms.cp import ortools_solve


def knapsack01_optimized_ortools(dataset, budget):
    return ortools_solve(KnapsackSolver.KNAPSACK_DYNAMIC_PROGRAMMING_SOLVER, dataset, budget)
