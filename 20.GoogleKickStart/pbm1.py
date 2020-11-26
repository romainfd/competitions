def collect_substring_positions(book):
    # find all KICK and START positions
    kicks = []
    starts = []
    for pos in range(len(book) - 3):
        if book[pos] == 'K':
            if book[pos:pos+4] == "KICK":
                kicks.append(pos)
        elif book[pos] == 'S':
            if book[pos:pos+5] == "START":
                starts.append(pos)
    return kicks, starts


def find_windows(beginnings, endings):
    # We go through endings ("START") and count the number of beginnings ("KICK") before each
    beginings_before = 0
    windows_count = 0
    for end_position in endings:
        while beginings_before < len(beginnings) and beginnings[beginings_before] < end_position:
            beginings_before += 1
        windows_count += beginings_before
    return windows_count


nb_cases = int(input())
for case in range(nb_cases):
    book = input()
    kicks, starts = collect_substring_positions(book)
    print("Case #" + str(case + 1) + ": " + str(find_windows(kicks, starts)))
