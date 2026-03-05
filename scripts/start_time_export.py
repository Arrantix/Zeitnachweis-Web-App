#!/usr/bin/env python3

import sys
import argparse
import json
from load_work_data import load_work_data
from export_with_holidays import export_with_holidays
from process_work_day_data import process_work_day_data

DEFAULT_OUTPUT_DIR = "../output"
EXIT_CODE_ERROR = 1


def start_time_export():
    parser = argparse.ArgumentParser(
        description="Export work data to Excel files with holiday integration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Usage examples:
  python start_time_export.py
  python start_time_export.py /path/to/data.json""",
    )

    parser.add_argument("data_file", nargs="?", help="Path to data file (JSON)")
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory path (default: ../output)",
    )

    args = parser.parse_args()

    # State code hardcoded to DE since API now only accepts DE
    state_code = "DE"

    data_file = args.data_file
    if data_file is None:
        print("No data file specified. Please paste your JSON data below:")
        print("Paste the JSON array of work days and press Enter twice to finish:")
        pasted_lines = []
        while True:
            line = input()
            if line == "":
                break
            pasted_lines.append(line)
        pasted_json = "\n".join(pasted_lines)
        try:
            data = json.loads(pasted_json)
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON data: {e}")
            sys.exit(EXIT_CODE_ERROR)
        work_days = process_work_day_data(data, "json")
    else:
        try:
            work_days = load_work_data(data_file)
        except (ValueError, FileNotFoundError) as e:
            print(f"❌ Error loading data file: {e}")
            sys.exit(EXIT_CODE_ERROR)

    if not work_days:
        print("❌ No valid work data found. Exiting.")
        sys.exit(EXIT_CODE_ERROR)

    print("=== Excel Export ===")
    print("State: DE")
    print(f"Output: {args.output_dir}/ZEITNACHWEIS_[year]_[month].xlsx")
    if data_file is None:
        print("Data: Pasted JSON")
    else:
        print(f"Data: {data_file}")

    try:
        output_files = export_with_holidays(
            work_days, state_code, output_dir=args.output_dir
        )

        if output_files:
            print("✅ Export completed successfully!")
            for file in output_files:
                print(f"📁 Generated: {file}")
        else:
            print("❌ Export failed!")
            sys.exit(EXIT_CODE_ERROR)

    except (ValueError, RuntimeError, OSError) as e:
        print(f"❌ Error: {e}")
        sys.exit(EXIT_CODE_ERROR)
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(EXIT_CODE_ERROR)


if __name__ == "__main__":
    start_time_export()
