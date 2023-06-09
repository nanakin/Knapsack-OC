from itertools import chain, combinations


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    dataset = list(iterable)
    return chain.from_iterable(combinations(dataset, size) for size in range(len(dataset) + 1))


def knapsack01_bruteforce(dataset, budget):
    best_combination = {"total_return": -1}
    for combination in powerset(dataset.keys()):
        # for each combination evaluate the total price and profit
        total_cost = sum(dataset[share_id]["price"] for share_id in combination)
        if total_cost <= budget:
            total_return = sum(dataset[share_id]["profit"] for share_id in combination)
            if total_return > best_combination["total_return"]:
                # backup the current best combination (with the best profit)
                best_combination = {
                    "investments": combination,
                    "total_cost": total_cost,
                    "total_return": total_return
                }
    return best_combination.values() if "investments" in best_combination else None

