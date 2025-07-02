import csv

def process_csv(path: str, where: str = None, aggregate: str = None):
    with open(path, newline='', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))

    if not reader:
        return []

    if where:
        reader = apply_filter(reader, where)

    if aggregate:
        return apply_aggregation(reader, aggregate)

    return reader

def apply_filter(rows: list[dict], condition: str) -> list[dict]:
    if '>' in condition:
        col, val = condition.split('>')
        return [r for r in rows if float(r[col.strip()]) > float(val)]
    elif '<' in condition:
        col, val = condition.split('<')
        return [r for r in rows if float(r[col.strip()]) < float(val)]
    elif '=' in condition:
        col, val = condition.split('=')
        return [r for r in rows if r[col.strip()] == val]
    else:
        raise ValueError("Noto‘g‘ri filter sintaksisi")

def apply_aggregation(rows: list[dict], agg: str) -> str:
    col, op = agg.split('=')
    col = col.strip()
    nums = [float(row[col]) for row in rows]

    match op:
        case "avg":
            return f"O‘rtacha: {sum(nums)/len(nums):.2f}"
        case "min":
            return f"Minimum: {min(nums)}"
        case "max":
            return f"Maksimum: {max(nums)}"
        case _:
            raise ValueError("Agregatsiya turi noto‘g‘ri")
