import argparse
from csv import DictReader
from knapsack01_algorithms import algorithms_list

BUDGET = 500


def decimal_to_integer_x100(decimal: str) -> int:
    """Convert a string repr. of a decimal number 'WW.FF' to an integer x100 bigger WWFF."""
    whole, point, fractional = decimal.partition(".")
    return int(f"{whole}{fractional:0<2}")


def integer_x100_to_decimal(number: int) -> str:
    """Convert an integer WWFF repr. a decimal number (2 digits precision) to its string repr. 'WW.FF'."""
    return f"{number//100:.2f}"


def read_dataset_file(dataset_filename: str) -> dict:
    """Read the given CSV file, then return a structured dataset."""
    dataset = {}
    with open(dataset_filename) as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            dataset[row["name"]] = {"price": decimal_to_integer_x100(row["price"]),
                                    "profit": decimal_to_integer_x100(row["profit"])}
    return dataset


def print_results(investments: list, total_cost: int, total_return: int):
    """Print the algorithm result."""
    print("Investments:")
    for investment in investments:
        print(investment)
    print(f"\nTotal cost: {integer_x100_to_decimal(total_cost)}€"
          f"\nTotal return: {integer_x100_to_decimal(total_return)}€")


def main(algorithm_choice: str, dataset_filename: str):
    """Read the given input dataset, solve the problem with the given algorithm then print the result."""
    dataset = read_dataset_file(dataset_filename)
    results = algorithms_list[algorithm_choice](dataset, BUDGET * 100)
    if results is None:
        print("No possibility")
    else:
        print_results(*results)


if __name__ == "__main__":
    # program entry point
    algorithms_choices = list(algorithms_list.keys())
    parser = argparse.ArgumentParser(description="Chess Tournament Manager")
    parser.add_argument('--algo', default=algorithms_choices[0], choices=algorithms_choices, help="Select a solver")
    parser.add_argument("-d", "--dataset", required=True, help="Provide shares data set in CSV format")
    args = parser.parse_args()
    main(args.algo, args.dataset)
