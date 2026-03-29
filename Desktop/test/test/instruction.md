# CSV Cleaner CLI Task

## Task Description

Create a Python command-line tool that cleans messy CSV data.

### Input
- A dirty CSV file located at `/task/dirty_data.csv`
- The file contains various data quality issues

### Output
- Clean the CSV data and save to `/task/clean_data.csv`

### Data Issues to Handle
1. **Empty rows** - Remove completely empty rows
2. **Whitespace** - Strip leading/trailing whitespace from all fields
3. **Invalid characters** - Remove or handle special characters
4. **Missing values** - Handle empty fields appropriately
5. **Inconsistent formatting** - Normalize data formats

### Requirements
1. Create a Python CLI tool (script)
2. The tool should accept input and output file paths as arguments
3. Process the dirty_data.csv and produce clean_data.csv
4. Handle edge cases gracefully

### Usage Example
```bash
python cleaner.py /task/dirty_data.csv /task/clean_data.csv
```

### Verification
Run `tests/test.sh` to verify your solution works correctly.
