#!/usr/bin/env python3
import csv
import os

def test_cleaned_file_exists():
    assert os.path.exists('/task/clean_data.csv'), "clean_data.csv not found"

def test_not_empty():
    with open('/task/clean_data.csv', 'r', encoding='utf-8') as f:
        content = f.read()
        assert len(content) > 0, "clean_data.csv is empty"

def test_no_completely_empty_rows():
    with open('/task/clean_data.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        for row in rows:
            assert not all(field.strip() == '' for field in row), "Found empty row"

def test_whitespace_stripped():
    with open('/task/clean_data.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for field in row:
                assert field == field.strip(), f"Whitespace not stripped: '{field}'"

def test_output_differs_from_input():
    with open('/task/dirty_data.csv', 'r', encoding='utf-8') as f:
        dirty = f.read()
    with open('/task/clean_data.csv', 'r', encoding='utf-8') as f:
        clean = f.read()
    assert dirty != clean, "Output same as input - cleaning didn't happen"

if __name__ == '__main__':
    tests = [
        test_cleaned_file_exists,
        test_not_empty,
        test_no_completely_empty_rows,
        test_whitespace_stripped,
        test_output_differs_from_input,
    ]

    failed = []
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except AssertionError as e:
            print(f"FAIL: {test.__name__} - {e}")
            failed.append(test.__name__)

    if failed:
        print(f"\n{len(failed)} test(s) failed")
        exit(1)
    else:
        print("\nAll tests passed!")
        exit(0)
