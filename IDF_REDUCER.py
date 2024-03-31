#!/usr/bin/env python3
from collections import defaultdict
import sys
import math

# Reducer code for IDF calculation
current_word = None
document_count = 0
total_documents = 1000000  # Assuming a total document count; this should be replaced with the actual number

for line in sys.stdin:
    line = line.strip()
    word, article_id = line.split('\t', 1)

    if current_word == word:
        document_count += 1
    else:
        if current_word:
            # Calculate and print the IDF value for the word
            idf = math.log(total_documents / document_count)
            print(f'{current_word}\t{idf}')

        current_word = word
        document_count = 1

# Don't forget the last word
if current_word == word:
    idf = math.log(total_documents / document_count)
    print(f'{current_word}\t{idf}')
