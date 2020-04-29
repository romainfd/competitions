import json
import os
from pathlib import Path

from stucture import Dataset


def get_project_root() -> Path:
    return Path(__file__).parent  # nb of .parent calls depends on file location


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
