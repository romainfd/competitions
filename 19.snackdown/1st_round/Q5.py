from numpy import array, unique
from operator import itemgetter

T = int(input())

# for each test case
for t in range(T):
    # we collect the data
    N = int(input())
    ppl = array(list(map(int, str.split(input(), " "))))

    # Initialisation
    uniqueRanks, counts = unique(ppl, return_counts=True)
    dic = dict(zip(uniqueRanks, counts))
    orderedDic = sorted(dic.items(), key=itemgetter(0), reverse=True)
    orderedList = list(map(list, orderedDic))  # we convert the tuples (rank, nb) to list to be able to modify them

    possibilities = 1
    for i in range(len(orderedList)):  # no -1 required because N is even => nb will be even for the last bucket
        rank, nb = orderedList[i]
        if nb % 2 == 1:
            # one of them is going to pair with one of a lower rank
            possibilities *= nb  # nb choice for this guy
            possibilities %= 1000000007
            nb -= 1  # he is paired now
            # he can choose any guy with the rank directly below
            possibilities *= orderedList[i + 1][1]
            possibilities %= 1000000007
            # so a guy from this rank is already paired
            orderedList[i + 1][1] -= 1
        # all our guys (even nb) can pair = C(nb, 2)
        if nb > 0:  # nb >= 2 because it's even now
            possibilities *= (((nb // 2) * (nb - 1)) % 1000000007)
        possibilities %= 1000000007
    print(possibilities)
