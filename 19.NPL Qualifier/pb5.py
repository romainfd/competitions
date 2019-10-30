def char_index(char):
    return ord(char) - 96


def word_analyser(word):
    cpt = 0
    for c in word:
        cpt += 1 << (4 * char_index(c))
    return cpt


anas = []
t = int(input())
for _ in range(t):
    word = input()
    anas.append(word_analyser(word))

q = int(input())
for _ in range(q):
    l, r = map(int, str.split(input()))
    print(len(set(anas[l-1:r])))
