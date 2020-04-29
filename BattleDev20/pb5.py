#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def preprocess(raw_letters):
    # on compte le nombre de lettres consécutives pour chaque lettre
    counts = {}
    old_l = raw_letters[0]
    c = 1
    for l in raw_letters[1:]:
        if l == old_l:
            c += 1
        else:
            if old_l not in counts:
                counts[old_l] = set()
            counts[old_l].add(c)
            old_l = l
            c = 1
    if old_l not in counts:
        counts[old_l] = set()
    counts[old_l].add(c)
    # on remplace avec moins de lettres
    for l, l_counts in counts.items():
        diff_count_nb = len(l_counts)
        for i, count in enumerate(sorted(list(l_counts), reverse=True)):
            raw_letters = raw_letters.replace(count * l, (diff_count_nb - i) * l)
    return raw_letters, counts


def post_process(raw_answer, counts):
    # on remplace avec plus de lettres
    for l, l_counts in counts.items():
        diff_count_nb = len(l_counts)
        for i, count in enumerate(sorted(list(l_counts), reverse=True)):
            raw_answer = raw_answer.replace((diff_count_nb - i) * l, count * l.upper())
    return raw_answer.lower()


def is_palyndrome(l):
    for i in range(len(l) // 2):
        if l[i] != l[-i-1]:
            return False
    return True

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

taille, nb_invite = map(int, lines[0].split(" "))
letters, counts = preprocess(lines[1])

current_palyndromes = [{0: []}]
n = len(letters)
for i in range(n):  # nb of letters taken so far
    new_values = {}
    # tous les autres palyndromes possibles depuis cette lettre
    for j in range(1, i+2):  # nb of letters we take
        word = letters[-(i+1):n-(i+1)+j]
        if is_palyndrome(word):
            for nb, rest in current_palyndromes[-j].items():
                if nb < nb_invite <= nb + (n - i):  # pour augmenter les perfs, oublier les mauvais chemins
                    new_values[nb+1] = [word] + rest  # osef d'overwrite
    current_palyndromes.append(new_values)

if nb_invite not in current_palyndromes[n].keys():
    print("IMPOSSIBLE")
else:
    # Reconstruire le chemin
    print(post_process(" ".join(current_palyndromes[n][nb_invite]), counts))


# NB: pre/proxessing not working. It might affect the dynamic programming search of the palyndrom decomposition
