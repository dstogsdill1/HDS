import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Convert a worksheet from an Excel workbook to CSV.")
    parser.add_argument("--input", "-i", required=True, help="Path to the input Excel workbook")
    parser.add_argument("--sheet", "-s", required=True, help="Name of the worksheet to export")
    parser.add_argument("--output", "-o", required=True, help="Path to the output CSV file")
    args = parser.parse_args()

    # Read the specified sheet from the Excel file
    df = pd.read_excel(args.input, sheet_name=args.sheet)

    # Write to CSV without the index
    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
