#!/usr/bin/env python3
"""Small example: read the first sheet of an Excel file and print the first rows.

Usage:
    python python_study/read_excel_example.py path/to/file.xlsx
"""
import argparse
import sys
from pathlib import Path

import pandas as pd


def main() -> int:
    parser = argparse.ArgumentParser(description="Read first sheet of an Excel file and print the first rows")
    parser.add_argument("file", nargs="?", help="Path to .xlsx file")
    args = parser.parse_args()

    if not args.file:
        print("Usage: python python_study/read_excel_example.py <file.xlsx>")
        return 1

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    try:
        df = pd.read_excel(path, sheet_name=0)
    except Exception as e:
        print("Error reading Excel file:", e)
        return 3

    # Print a small, readable preview
    if df.empty:
        print("Excel sheet is empty")
    else:
        print(df.head().to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
