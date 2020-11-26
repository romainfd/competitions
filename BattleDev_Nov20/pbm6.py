# *******
# * Read input from STDIN
# * Use print to output your result to STDOUT.
# * Use sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def len_sub_seq(str1, str2):
    # returns the length of the longest subsequence of str1 in str2
    if len(str2) == 0:
        return 0, ''
    if len(str1) == 1:
        return int(str1[0] in str2), str1
    i = str2.find(str1[0])
    if i == -1:
        return len_sub_seq(str1[1:], str2)
    with_i, str_with_i = len_sub_seq(str1[1:], str2[i + 1:])
    without_i, str_without_i = len_sub_seq(str1[1:], str2)
    if 1 + with_i > without_i:
        return 1 + with_i, str1[0] + str_with_i
    else:
        return without_i, str_without_i


def extract_all_matches(str1, str2):
    lengths = []
    while True:
        length, match = len_sub_seq(str1, str2)
        print(match)
        if length == 0:
            break
        str1 = list(str1)
        str2 = list(str2)
        for c in match:
            str1.remove(c)
            str2.remove(c)
        str1 = ''.join(str1)
        str2 = ''.join(str2)
        lengths.append(length)
    return lengths


fake = False
for str1, str2 in map(lambda line: line.split(' '), lines[1:]):
    l = sorted(extract_all_matches(str1, str2), reverse=True)
    print(l)
    if (len(l) == 4 and l[0] == 1) or \
            (len(l) == 2 and l[0] == 2) or \
            (len(l) == 1 and l[0] == 1):
        fake = True
        # Actually more complex as taking a 2 in 2 2 1 could throw on 2 1 1 1
        # dacbe ceabd
        # acbe ceab  # removing the 1 ie the d
        # Instead of ab and ce (2 2) it can be seen as cb a e (2 1 1) which wins by putting on 1 1
        # ea ea      # removing cb => we loose
print('FAKE' if fake else 'DEBUNK')
