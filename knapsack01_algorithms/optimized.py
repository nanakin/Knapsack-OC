def knapsack01_optimized(dataset: dict, budget: int):
    print("optimized")
    prices = [share_data["price"] for share_data in dataset.values()]
    profits = [share_data["profit"] for share_data in dataset.values()]
    shares_id = list(dataset.keys())

    returns_by_budget = [0 for _ in range(budget + 1)]
    investments = []
    total_cost = 0
    for n_shares in range(len(prices)):
        best_value_for_row_items = returns_by_budget[budget]
        for curr_budget in range(budget, 0, -1):
            if prices[n_shares] <= curr_budget:
                returns_by_budget[curr_budget] = max(profits[n_shares] + returns_by_budget[curr_budget - prices[n_shares]], returns_by_budget[curr_budget])
            else:
                break
        if returns_by_budget[budget] != best_value_for_row_items:
            share_id = shares_id[n_shares]
            investments.append(share_id)
            total_cost += dataset[share_id]["price"]

    return investments, total_cost, returns_by_budget[budget]