def knapsack01_optimized(dataset: dict, budget: int) -> tuple[list, int, int]:
    """
    Select the best shares combination in such a way that the total investment produces the maximum profit.
    A Dynamic Programming solution for the 0-1 knapsack problem.
    """

    prices = [share_data["price"] for share_data in dataset.values()]
    profits = [share_data["profit"] for share_data in dataset.values()]
    shares_id = list(dataset.keys())
    investments = []
    total_cost = 0

    # create 2D array to store intermediate profits values (memoization)
    known_profits = [[0 for _ in range(budget + 1)]
                     for _ in range(len(dataset) + 1)]

    for n in range(len(dataset)):  # loop over the shares list
        # for each new share considered, go through all budget possibilities (0 -> maximum budget)
        for curr_budget in range(budget + 1):
            best_profit_without_the_share = known_profits[n][curr_budget]
            if prices[n] <= curr_budget:  # the share is affordable for the current budget
                # to get the best profit considering the current share inclusion, we reuse one of the best profits
                # calculation : the one where the budget = current budget - price of the current share
                best_profit_with_the_share = profits[n] + known_profits[n][curr_budget - prices[n]]
                known_profits[n+1][curr_budget] = max(best_profit_with_the_share,
                                                      best_profit_without_the_share)  # we keep the best option
            else:
                # as the share is not affordable, we can ignore it in the best profit calculation (for the curr. budget)
                # the best profit with the list of shares [0 -> n] is the same as [0 -> n - 1]
                known_profits[n+1][curr_budget] = best_profit_without_the_share

    # find the selected shares
    remaining_budget = budget
    for n in range(len(dataset), 0, -1):
        # if the vertically adjacent cells are different (for the max remaining budget column, going decreasing)
        # it means that we chose to include the share n-1 in the final solution
        if known_profits[n][remaining_budget] != known_profits[n-1][remaining_budget]:
            investments.insert(0, shares_id[n-1])
            total_cost += prices[n-1]
            remaining_budget = remaining_budget - prices[n-1]

    # return the solution data
    return investments, total_cost, known_profits[-1][budget]
