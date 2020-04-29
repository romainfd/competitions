import os

import numpy as np;
import pandas as pd

# INPUT CONSTRUCTION
B, L, D = map(int, input().split())
scores = list(map(int, input().split()))
libraries = []
for _ in range(L):
    nb, tps, rate = map(int, input().split())
    books = list(map(int, input().split()))
    libraries.append({
        'nb': nb,
        'tps': tps,
        'rate': rate,
        'books': books
    })


def score(book_list, scores=scores):
    s = np.zeros(len(book_list), dtype=int)
    for i, b in enumerate(book_list):
        s[i] = scores[b]
    return s


idf = np.zeros(B, dtype=int)

for lib in libraries:
    idf[lib['books']] += 1

idf = np.clip(idf, a_min=1, a_max=+np.inf)


def score_idf(books, idf=idf, scores=scores):
    return np.sum(scores[books] / idf[books])


lib_pd = pd.DataFrame(libraries)
lib_pd['scores'] = lib_pd['books'].apply(lambda x: score(x, scores))
lib_pd['mean_scores'] = lib_pd['books'].apply(np.mean)
lib_pd['sum_scores'] = lib_pd['scores'].apply(np.sum)
lib_pd['sum_scores_norm'] = (lib_pd['sum_scores'] - lib_pd['sum_scores'].mean()) / lib_pd['sum_scores'].std()
lib_pd['rate_norm'] = (lib_pd['rate'] - lib_pd['rate'].mean()) / lib_pd['rate'].std()
lib_pd['tps_norm'] = (lib_pd['tps'] - lib_pd['tps'].mean()) / lib_pd['tps'].std()
lib_pd['lib_scores'] = lib_pd['rate'] * lib_pd['books'].apply(score_idf) / np.sqrt(lib_pd['tps'])
lib_pd = lib_pd.sort_values(by='lib_scores', ascending=False)
permutation = np.array(list(lib_pd.index))


# HELPER FUNCTIONS
# Based on lib_data = list of [l_id, nb_books_taken, [taken_books_ids]]

# Format and print output
def output(lib_data):
    lib_data = list(filter(
        lambda lib_datum: lib_datum[1] > 0,
        lib_data
    ))
    print(len(lib_data))
    for l_id, nb, l_book_ids in lib_data:
        print(l_id, nb)
        print(" ".join(map(str, l_book_ids)))


# Helper function to score a single library for the remaining days
def score_lib(scanned_books, nb_days, book_ids, l_id):
    score = 0
    next_book_to_scan_rank = 0
    for _ in range(nb_days):
        books_scanned_today = 0
        while next_book_to_scan_rank < len(book_ids) and books_scanned_today < libraries[l_id]['rate']:
            next_book = book_ids[next_book_to_scan_rank]
            assert next_book in libraries[l_id]['books'], \
                f"Book {next_book} not in library {l_id}. Check your index management, you should't update the collected inputs. Please copy them before updating them."
            if next_book not in scanned_books:
                score += scores[next_book]
                scanned_books.add(next_book)
            # Going in the else loop is bad for performances
            # Increases even if we have already scanned the book!!
            books_scanned_today += 1
            next_book_to_scan_rank += 1
    return score, scanned_books


# Score a library distribution
def scorer(lib_data):
    total_score = 0
    scanned_books = set()
    remaining_days = D
    for i in range(len(lib_data)):
        l_id, nb, l_book_ids = lib_data[i]
        remaining_days -= libraries[l_id]['tps']
        assert nb == len(l_book_ids), "You might miss data otherwise"
        score, scanned_books = score_lib(scanned_books, remaining_days, l_book_ids, l_id)
        total_score += score
    return total_score


def take_books_in_order(scanned_books, nb_days, book_ids, l_id):
    next_book_to_scan_rank = 0
    books_taken = []
    for _ in range(nb_days):
        books_scanned_today = 0
        while next_book_to_scan_rank < len(book_ids) and books_scanned_today < libraries[l_id]['rate']:
            next_book = book_ids[next_book_to_scan_rank]
            assert next_book in libraries[l_id]['books'], \
                f"Book {next_book} not in library {l_id}. Check your index management, you should't update the collected inputs. Please copy them before updating them."
            if next_book not in scanned_books:
                books_taken.append(next_book)
                scanned_books.add(next_book)
                books_scanned_today += 1
            next_book_to_scan_rank += 1
    return books_taken, scanned_books


top_lib_data = []
lib_data = []
scanned_books = set()
remaining_days = D
for lib in range(L):
    l_id = permutation[lib]
    remaining_days -= libraries[l_id]['tps']
    nb = libraries[l_id]['nb']
    # Greedy approach of sorting
    books_to_scan_through = sorted(
        libraries[l_id]['books'],
        key=lambda book_id: scores[book_id],
        reverse=True
    )
    l_book_ids, scanned_books = take_books_in_order(scanned_books, remaining_days, books_to_scan_through, l_id)
    lib_data.append([l_id, len(l_book_ids), l_book_ids])
score = scorer(lib_data)

output(top_lib_data)
print(score)
