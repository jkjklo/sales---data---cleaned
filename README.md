# sales-data-cleaned

## Overview

This repository contains cleaned sales data, along with the Python script (`clean_sales_data.py`) used for cleaning, and the output files in both Excel and CSV formats.

## Tasks Performed

- **Identified and handled missing values**  
    - Filled missing SalesPerson with 'Unknown'
    - Filled missing Amounts with 0
    - Filled missing Product and Region with 'Unknown' if any missing

- **Removed duplicate rows** to ensure each sales record is unique

- **Standardized text values**  
    - Made SalesPerson, Product, and Region title case with no extra spaces (e.g., North, South)
  
- **Converted all date formats** to a single standard: `dd-mm-yyyy`

- **Renamed columns** to consistent lowercase and underscore format (e.g., `orderid`, `salesperson`)

- **Checked and fixed data types**  
    - Amounts are integer numbers (no currency symbols or commas)
    - Dates are formatted as `dd-mm-yyyy` strings

## How To Run

1. Install dependencies:  
   `pip install pandas openpyxl`
2. Place `sales-data-raw.xlsx` and `clean_sales_data.py` in the same folder.
3. Run the script:  
   `python clean_sales_data.py`
4. The cleaned files will be generated:
    - `sales_data_cleaned.xlsx`
    - `sales_data_cleaned.csv`

## Files

- `sales_data_cleaned.xlsx` — Cleaned sales data (Excel)
- `sales_data_cleaned.csv` — Cleaned sales data (CSV)
- `clean_sales_data.py` — Python script used for cleaning
- `sales-data-raw.xlsx` — The raw sales data (for reference)

