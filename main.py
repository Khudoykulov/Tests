import argparse
from processor import process_csv
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(description="CSV faylni filtrlash va agregatsiya qilish")

    parser.add_argument("path", help="CSV faylga yo‘l")
    parser.add_argument("--where", help="Filtr: column=value | column>value | column<value")
    parser.add_argument("--aggregate", help="Agregatsiya: column=avg|min|max")

    args = parser.parse_args()

    try:
        result = process_csv(args.path, args.where, args.aggregate)
        if isinstance(result, list):
            print(tabulate(result, headers="keys"))
        else:
            print(result)
    except Exception as e:
        print(f"Xatolik: {e}")

if __name__ == "__main__":
    main()
