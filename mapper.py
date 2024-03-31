#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    # Split by comma for CSV file
    parts = line.split(',')
    if len(parts) >= 2:
        article_id = parts[0]
        section_text = ','.join(parts[1:])  # Re-join the remaining parts to form the complete section text
        # Process each word in the section_text
        words = section_text.split()
        for word in words:
            print(f'{word}\t{article_id}\t1')
