import os
import glob
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

def process_excel(excel_path):
    try:
        xls = pd.ExcelFile(excel_path)
        sheet_names = xls.sheet_names

        for sheet_name in sheet_names:
            out = Path(excel_path).parent / f"{os.path.splitext(os.path.basename(excel_path))[0]}_{sheet_name}.csv"
            print(f"   Reading sheet: {sheet_name}")
            df = pd.read_excel(excel_path, sheet_name=sheet_name, engine='openpyxl')
            
            print(f"   Writing CSV: {out}")
            df.to_csv(out, index=False)
            
        print(f"Excel file processing complete: {excel_path}\n")
        
    except Exception as e:
        print(f"Error processing Excel file {excel_path}: {e}\n")

def process_files_in_directory(directory):
    excel_files = sorted(glob.glob(os.path.join(directory, '**', '*.xlsx'), recursive=True), key=os.path.getsize)

    with ProcessPoolExecutor() as executor:
        executor.map(process_excel, excel_files)

if __name__ == "__main__":
    user_directory = input("Enter the directory path: ")
    
    if os.path.isdir(user_directory):
        process_files_in_directory(user_directory)
    else:
        print("Invalid directory path.")
