import json
import os
from pathlib import Path

import numpy as np

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


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def write_solution(solution, i, prefix=''):
    with open(os.path.join(get_project_root(), f'solution/{prefix}_{i:d}.json'), 'w') as file:
        file.write(json.dumps(solution, cls=NpEncoder))


def write_solutions(solutions, prefix=''):
    for i, solution in enumerate(solutions):
        write_solution(solution, i + 1, prefix)
