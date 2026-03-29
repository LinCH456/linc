#!/usr/bin/env python3
import csv
import sys
import re

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as f_in:
        reader = csv.reader(f_in)
        rows = list(reader)

    cleaned_rows = []
    for row in rows:
        if not row or all(field.strip() == '' for field in row):
            continue

        cleaned_row = []
        for field in row:
            cleaned_field = field.strip()
            cleaned_field = re.sub(r'[^\x00-\x7F]+', '', cleaned_field)
            cleaned_row.append(cleaned_field)

        if cleaned_row and any(f for f in cleaned_row):
            cleaned_rows.append(cleaned_row)

    with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        writer.writerows(cleaned_rows)

if __name__ == '__main__':
    input_file = '/task/dirty_data.csv'
    output_file = '/task/clean_data.csv'

    try:
        clean_csv(input_file, output_file)
        print(f"Cleaned data saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
