import sys
import os
import argparse

try:
    import pandas as pd
except Exception:
    sys.exit("pandas (and openpyxl) are required. Install with: pip install pandas openpyxl")


def main():
    parser = argparse.ArgumentParser(description="Convert an Excel file to CSV (default: series.xlsx -> series.csv)")
    parser.add_argument("-i", "--input", default="series.xlsx", help="Input Excel file (default: series.xlsx)")
    parser.add_argument("-o", "--output", default="series.csv", help="Output CSV file (default: series.csv)")
    parser.add_argument("-s", "--sheet", default=None, help="Sheet name or 0-based index (default: first sheet)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        sys.exit(f"Input file not found: {args.input}")

    # Interpret sheet argument
    sheet_arg = None
    if args.sheet is not None:
        # try to convert to int (0-based index)
        try:
            sheet_arg = int(args.sheet)
        except Exception:
            sheet_arg = args.sheet

    try:
        if sheet_arg is None:
            df = pd.read_excel(args.input, engine="openpyxl")
        else:
            df = pd.read_excel(args.input, sheet_name=sheet_arg, engine="openpyxl")
    except Exception as e:
        sys.exit(f"Failed to read Excel file: {e}")

    try:
        df.to_csv(args.output, index=False)
    except Exception as e:
        sys.exit(f"Failed to write CSV file: {e}")

    print(f"Wrote {args.output}")


if __name__ == '__main__':
    main()
