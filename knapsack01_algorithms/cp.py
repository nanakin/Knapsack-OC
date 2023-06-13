from ortools.algorithms import pywrapknapsack_solver


def ortools_solve(selected_algorithm, dataset, budget):
    # create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(selected_algorithm, 'Knapsack solver')

    # initialize the solver
    values = [share_data["profit"] for share_data in dataset.values()]
    weights = [[share_data["price"] for share_data in dataset.values()]]
    shares_id = list(dataset.keys())
    capacities = [budget]
    solver.Init(values, weights, capacities)

    # launch the ortools solver
    total_return = solver.Solve()

    # analyze and return the results
    investments = []
    total_cost = 0
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            investments.append(shares_id[i])
            total_cost += weights[0][i]
    return investments, total_cost, total_return
