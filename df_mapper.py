#!/usr/bin/env python3
import sys
import csv

# Use the CSV module to handle CSV parsing
csv_reader = csv.reader(sys.stdin)

for line in csv_reader:
    # Check if the line has at least 2 columns
    if len(line) >= 2:
        # Extract article_id and section_text from the CSV line
        article_id, section_text = line[0], line[1]
        words = section_text.split()
        for word in words:
            # Emit the word, the article_id, and a count of 1
            print(f'{word}\t{article_id}\t1')

