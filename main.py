import argparse
from csv import DictReader
from algorithms import algorithms_list


def read_dataset_file(dataset_filename):
    dataset = {}
    with open(dataset_filename) as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            dataset[row["name"]] = {"price": float(row["price"]), "profit": float(row["profit"])}
    return dataset


def print_results(investments, total_cost, total_return):
    print("Investments:")
    for investment in investments:
        print(investment)
    print(f"\nTotal cost: {total_cost:.2f}€\nTotal return: {total_return:.2f}€")


def main(algorithm_choice, dataset_filename):
    dataset = read_dataset_file(dataset_filename)
    results = algorithms_list[algorithm_choice](dataset)
    if results is None:
        print("No possibility")
    else:
        print_results(*results)


if __name__ == "__main__":
    # Program entry point
    algorithms_choices = list(algorithms_list.keys())
    parser = argparse.ArgumentParser(description="Chess Tournament Manager")
    parser.add_argument('--algo', default=algorithms_choices[0], choices=algorithms_choices, help="Select a solver")
    parser.add_argument("-d", "--dataset", required=True, help="Provide shares data set in CSV format")
    args = parser.parse_args()
    main(args.algo, args.dataset)
