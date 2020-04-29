import json
import os
from pathlib import Path

from stucture import Dataset


def get_project_root() -> Path:
    return Path(__file__).parent  # nb of .parent calls depends on file location


def load_dataset_raw(i):
    """ Load and return Dataset nb i """
    with open(os.path.join(get_project_root(), f'data/{i:d}.json')) as f:
        data = json.load(f)
    return data


def load_datasets_raw(i):
    """ Load and return Datasets """
    datasets = []
    for i in range(1, 7):
        datasets.append(load_dataset_raw(i))
    return datasets


def load_dataset(i):
    """ Load and return Dataset nb i """
    with open(os.path.join(get_project_root(), f'data/{i:d}.json')) as f:
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


def get_score(solution, dataset):
    import collections
    peoplePerTrain = collections.Counter()
    for worker in solution:
        morningOptions = dataset['workers'][worker['name']]['morningOptions']
        for train in morningOptions[worker['morningOptionIndex']]:
            peoplePerTrain[train] += 1
        eveningOptions = dataset['workers'][worker['name']]['eveningOptions']
        for train in eveningOptions[worker['eveningOptionIndex']]:
            peoplePerTrain[train] += 1
    return sum(v * (v - 1) for v in peoplePerTrain.values())


def write_solutions(solutions):
    for i, solution in enumerate(solutions):
        with open(os.path.join(get_project_root(), f'solution/{i+1:d}.txt'), 'w') as file:
            file.write(json.dumps(solution))
