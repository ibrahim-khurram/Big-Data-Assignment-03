#!/usr/bin/env python3
from collections import defaultdict
import sys

# Reducer code for document indexing
current_word = None
article_count = defaultdict(int)  # Keep track of document frequency for each word

for line in sys.stdin:
    line = line.strip()
    word, article_id = line.split('\t', 1)
   
    if current_word == word:
        # Increment the count for the word-article_id pair
        article_count[article_id] += 1
    else:
        if current_word:
            # Word has changed; print the previous word's count for each article
            for art_id, count in article_count.items():
                print(f'{current_word}\t{art_id}\t{count}')
            # Reset for the new word
            article_count.clear()

        current_word = word
        article_count[article_id] = 1

# Output the last word if needed
if current_word:
    for art_id, count in article_count.items():
        print(f'{current_word}\t{art_id}\t{count}')
