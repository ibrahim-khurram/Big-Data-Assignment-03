#!/usr/bin/env python3
import sys
import re

# Mapper code for document indexing
for line in sys.stdin:
    # Split the input from CSV, focusing on ARTICLE_ID and SECTION_TEXT
    line = line.strip()
    parts = line.split(',')
    if len(parts) >= 4:  # Ensure there are enough parts to include ARTICLE_ID and SECTION_TEXT
        article_id, section_text = parts[0], parts[3]
       
        # Basic text cleaning
        section_text = section_text.lower()  # Convert to lowercase
        section_text = re.sub(r'\W+', ' ', section_text)  # Remove punctuation
       
        # Emit words with their article ID
        words = section_text.split()
        for word in words:
            print(f'{word}\t{article_id}')
