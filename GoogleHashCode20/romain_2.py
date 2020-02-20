import numpy as np; np.random.seed(21)
from tqdm import tqdm
import os


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


# Helper function to score a single library for the remaining days
def score_lib(scanned_books, nb_days, book_ids, l_id):
    score = 0
    next_book_to_scan_rank = 0
    for _ in range(nb_days):
        books_scanned_today = 0
        while next_book_to_scan_rank < len(book_ids) and books_scanned_today < libraries[l_id]['rate']:
            next_book = book_ids[next_book_to_scan_rank]
            assert next_book in libraries[l_id]['books'],\
                f"Book {next_book} not in library {l_id}. Check your index management, you should't update the collected inputs. Please copy them before updating them."
            if next_book not in scanned_books:
                score += scores[next_book]
                scanned_books.add(next_book)
            # Going in the else loop is bad for performances
            # Increases even if we have already scanned the book!!
            books_scanned_today += 1
            next_book_to_scan_rank += 1
    return score, scanned_books


def take_books_in_order(scanned_books, nb_days, book_ids, l_id):
    next_book_to_scan_rank = 0
    books_taken = []
    for _ in range(nb_days):
        books_scanned_today = 0
        while next_book_to_scan_rank < len(book_ids) and books_scanned_today < libraries[l_id]['rate']:
            next_book = book_ids[next_book_to_scan_rank]
            assert next_book in libraries[l_id]['books'],\
                f"Book {next_book} not in library {l_id}. Check your index management, you should't update the collected inputs. Please copy them before updating them."
            if next_book not in scanned_books:
                books_taken.append(next_book)
                scanned_books.add(next_book)
                books_scanned_today += 1
            next_book_to_scan_rank += 1
    return books_taken, scanned_books


# COMPUTE LIBRARY DISTRIBUTION
NB_LOOPS_1MIN = np.array([0, 50, 11, 32, 3.4, 135, 240])

top_score = 0
top_lib_data = []
for i in tqdm(range(int(10 * NB_LOOPS_1MIN[int(os.environ['NB'])]))):
    permutation = np.random.permutation(L)
    lib_data = []
    scanned_books = set()
    remaining_days = D
    for l in range(L):
        l_id = permutation[l]
        remaining_days -= libraries[l_id]['tps']
        nb = libraries[l_id]['nb']
        books_to_scan_through = np.random.permutation(libraries[l_id]['books'])  # TODO: make this smarter by ordering by value for example
        l_book_ids, scanned_books = take_books_in_order(scanned_books, remaining_days, books_to_scan_through, l_id)
        lib_data.append([l_id, len(l_book_ids), l_book_ids])
    score = scorer(lib_data)
    if score > top_score:
        top_score = score
        top_lib_data = lib_data

# print(top_score)
output(top_lib_data)

