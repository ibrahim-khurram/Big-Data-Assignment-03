#!/usr/bin/env python3
import sys
import re

# Mapper code for IDF calculation
seen = set()  # Keep track of seen word-article pairs to ensure uniqueness

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) >= 4:
        article_id, section_text = parts[0], parts[3]

        section_text = section_text.lower()
        section_text = re.sub(r'\W+', ' ', section_text)

        words = set(section_text.split())  # Use a set to ensure words are unique per document

        for word in words:
            pair = (word, article_id)
            if pair not in seen:
                seen.add(pair)
                print(f'{word}\t{article_id}')
