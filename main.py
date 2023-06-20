import argparse
from csv import DictReader
from knapsack01_algorithms import algorithms_list

DEFAULT_BUDGET = 500


def decimal_to_integer_x100(decimal: str) -> int:
    """Convert a string repr. of a decimal number 'WW.FF' to an integer x100 bigger WWFF."""
    whole, point, fractional = decimal.partition(".")
    return int(f"{whole}{fractional:0<2}")


def integer_x100_to_decimal(number: int) -> str:
    """Convert an integer WWFF repr. a decimal number (2 digits precision) to its string repr. 'WW.FF'."""
    return f"{number//pow(10, 2):.2f}"


def read_dataset_file(dataset_filename: str) -> dict:
    """Read the given CSV file, then return a structured dataset."""
    dataset = {}
    with open(dataset_filename) as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            price_x100 = decimal_to_integer_x100(row["price"])
            if price_x100 >= 0:
                dataset[row["name"]] = {"price": price_x100,
                                        "profit": float(row["profit"]) * float(row["price"]) / 100}
    return dataset


def print_results(investments: list, total_cost: int, total_return: int):
    """Print the algorithm result."""
    print(f"{len(investments)} Investments:")
    for investment in investments:
        print(investment)
    print(f"\nTotal cost: {integer_x100_to_decimal(total_cost)}€"
          f"\nTotal return: {total_return:.2f}€")


def main(algorithm_choice: str, dataset_filename: str, budget: int):
    """Read the given input dataset, solve the problem with the given algorithm then print the result."""
    dataset = read_dataset_file(dataset_filename)
    results = algorithms_list[algorithm_choice](dataset, budget * 100)
    if results is None:
        print("No possibility")
    else:
        print_results(*results)


if __name__ == "__main__":
    # program entry point
    algorithms_choices = list(algorithms_list.keys())
    parser = argparse.ArgumentParser(description="Best Investments Finder")
    parser.add_argument('--algo', default=algorithms_choices[0], choices=algorithms_choices, help="Select a solver")
    parser.add_argument("-d", "--dataset", required=True, help="Provide shares data set in CSV format")
    parser.add_argument("-b", "--budget", type=int, default=DEFAULT_BUDGET, help="Provide the maximum budget")
    args = parser.parse_args()
    main(args.algo, args.dataset, args.budget)
