def knapsack01_optimized(dataset: dict, budget: int):
    prices = [share_data["price"] for share_data in dataset.values()]
    profits = [share_data["profit"] for share_data in dataset.values()]
    shares_id = list(dataset.keys())
    investments = []
    total_cost = 0

    known_profits = [[0 for _ in range(budget + 1)]
                     for _ in range(len(dataset) + 1)]
    for n in range(len(dataset)):
        for curr_budget in range(1, budget + 1):
            previous_row_profit = known_profits[n][curr_budget]
            if prices[n] <= curr_budget:
                known_profits[n+1][curr_budget] = max(profits[n] + known_profits[n][curr_budget - prices[n]],
                                                      previous_row_profit)
            else:
                known_profits[n+1][curr_budget] = previous_row_profit

    remaining_budget = budget
    for n in range(len(dataset), 0, -1):
        if known_profits[n][remaining_budget] != known_profits[n-1][remaining_budget]:
            investments.insert(0, shares_id[n-1])
            total_cost += prices[n-1]
            remaining_budget = remaining_budget - prices[n-1]

    return investments, total_cost, known_profits[-1][budget]