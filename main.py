import argparse
from algorithms import algorithms_list


def main(algorithm_choice, dataset):
    results = algorithms_list[algorithm_choice](dataset)
    print(*results)


if __name__ == "__main__":
    # Program entry point
    algorithms_choices = list(algorithms_list.keys())
    parser = argparse.ArgumentParser(description="Chess Tournament Manager")
    parser.add_argument('--algo', default=algorithms_choices[0], choices=algorithms_choices, help="Select a solver")
    parser.add_argument("-d", "--dataset", required=True, help="Provide shares data set in CSV format")
    args = parser.parse_args()
    main(args.algo, args.dataset)
