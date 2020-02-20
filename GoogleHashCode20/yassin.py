import numpy as np
from tqdm import tqdm
import pandas as pd
# returns a list of scores of each library
B, L, D = map(int, input().split())
scores = list(map(int, input().split()))
libraries = []
for i in range(L):
    nb, tps, rate = map(int, input().split())
    books = list(map(int, input().split()))
    libraries.append({
        'nb': nb,
        'tps': tps,
        'rate': rate,
        'books': books
    })

libraries_df = pd.DataFrame(libraries)

def score_():
    pass

def example_score_(libraries):
    tps = [library['tps'] for library in libraries]
    return tps

# returns the sorted list of libraries
def sort_(library_scores):
    return np.argsort(library_scores)[::-1]

# returns the sorted list of books
def sort_books_(library_books, books):
    sorted_books = np.argsort(books)[::-1]
    res = []
    library_books = set(library_books)
    for book in sorted_books:
        if book in library_books:
            res.append(book)
    return res

def output(sorted_libraries):
    print(len(sorted_libraries))
    for library in tqdm(sorted_libraries):
        print(library, libraries[library]['nb'])
        l_book_ids = sort_books_(libraries[library]['books'], scores)
        print(" ".join(map(str, l_book_ids)))

library_scores = example_score_(libraries)
sorted_libraries = sort_(library_scores)
output(sorted_libraries)