from knapsack01_algorithms import bruteforce, bruteforce_ortools, optimized_ortools, optimized

algorithms_list = {
    "bruteforce": bruteforce.knapsack01_bruteforce,
    "bruteforce-ortools": bruteforce_ortools.knapsack01_bruteforce_ortools,
    "optimized-ortools": optimized_ortools.knapsack01_optimized_ortools,
    "optimized": optimized.knapsack01_optimized
}
