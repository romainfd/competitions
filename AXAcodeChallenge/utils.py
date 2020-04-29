import json

from stucture import Dataset


def load_dataset(i):
    """ Load and return Dataset nb i """
    with open(f'data/{i:d}.json') as f:
        data = json.load(f)
        quotas = data['quotas']
        workers = data['workers']
        dataset = Dataset(i, quotas, workers)
    return dataset


def load_datasets():
    """ Load and return the list of the 6 Datasets """

    datasets = []
    for i in range(1, 7):
        datasets.append(load_dataset(i))
    return datasets
