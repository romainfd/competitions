from numpy import array

T = int(input())

# for each test case
for t in range(T):
    # we collect the data
    N = int(input())
    ppl = array(list(map(int, str.split(input(), " "))))

    # Initialisation
    nbTurns = 1
    i = 0  # the first person knows about it
    s = ppl[0]  # fine because N >= 2
    # i is the index of the last person told about the event
    # s is the number of persons who are gonna learn about the event at the next turn (= sum(ppl[:,i + 1])

    while i + s < N - 1:  # when i + s >= N-1, everyone knows about it
        i += s  # we spread the world to s person
        s += sum(ppl[i - s + 1: i + 1])  # they will also spread the world at the next turn
        nbTurns += 1
    print(nbTurns)

