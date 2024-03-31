import csv
import re
import sys

# Increase the maximum field size limit
csv.field_size_limit(sys.maxsize)

def clean_text(text):
    """
    Perform basic text cleaning.
    Remove special characters, numbers, and convert text to lowercase.
    """
    text = re.sub(r'\W+', ' ', text)  # Remove special characters.
    text = re.sub(r'\d+', '', text)  # Remove numbers.
    text = text.lower()  # Convert to lowercase.
    return text

def process_dataset(file_path):
    """
    Process the dataset to focus on ARTICLE_ID and SECTION_TEXT.
    Clean the SECTION_TEXT for each article.
    """
    processed_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            article_id = row['ARTICLE_ID']
            section_text = clean_text(row['SECTION_TEXT'])
            processed_data.append((article_id, section_text))
    return processed_data

# Example usage
file_path = '/home/ebraheem/Documents/cleen/input.csv'  # Update this to the path of your dataset
processed_data = process_dataset(file_path)

# Optionally, save the processed data to a new CSV file for indexing
with open('/home/ebraheem/Documents/cleen/cleaned.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ARTICLE_ID', 'SECTION_TEXT'])  # Writing headers
    writer.writerows(processed_data)
