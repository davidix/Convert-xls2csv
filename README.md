# Excel to CSV Converter

A simple Python script to convert Excel files (.xlsx) to CSV files using parallel processing.

## Overview

This script uses the `concurrent.futures.ProcessPoolExecutor` to parallelize the conversion of multiple Excel sheets within Excel files in a specified directory. Each sheet is saved as a separate CSV file.

## Features

- Converts Excel files to CSV format
- Utilizes parallel processing for efficient conversion
- Handles errors gracefully and provides error messages for failed conversions

## Requirements

- Python 3.x
- pandas
- openpyxl

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/excel-to-csv-converter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd excel-to-csv-converter
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:

    ```bash
    python excel_to_csv_converter.py
    ```

5. Enter the directory path when prompted.

## Example

```bash
Enter the directory path: /path/to/excel/files
