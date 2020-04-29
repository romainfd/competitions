def getScore(solution, dataset):
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
