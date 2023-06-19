from itertools import chain, combinations


def powerset(id_list: list):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)."""

    # we want all combinations for all possible size (from 0 to the size of the given list)
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    return chain.from_iterable(combinations(id_list, size) for size in range(len(id_list) + 1))


def knapsack01_bruteforce(dataset: dict, budget: int) -> tuple[list, int, int] | None:
    """
    Select the best shares combination in such a way that the total investment produces the maximum profit.
    A bruteforce solution for the 0-1 knapsack problem.
    """
    best_combination = {"total_return": -1}

    for combination in powerset(list(dataset.keys())):
        # for each shares combination evaluate the total price and profit
        total_cost = sum(dataset[share_id]["price"] for share_id in combination)
        if total_cost <= budget:  # if the combination cost fits in the budget
            total_return = sum(dataset[share_id]["profit"] for share_id in combination)
            # if the total profit of the combination is better than the old one
            if total_return > best_combination["total_return"]:
                # backup the current best combination (with the current best profit)
                best_combination = {
                    "investments": combination,
                    "total_cost": total_cost,
                    "total_return": total_return
                }

    # return the solution data
    return best_combination.values() if "investments" in best_combination else None
