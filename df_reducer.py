#!/usr/bin/env python3
import sys
from itertools import groupby
from operator import itemgetter

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 2)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    # Data is grouped by word
    for word, group in groupby(data, itemgetter(0)):
        unique_docs = set(doc_id for _, doc_id, _ in group)
        # Document frequency is the count of unique article_ids
        df = len(unique_docs)
        print(f"{word}{separator}{df}")

if __name__ == "__main__":
    main()
