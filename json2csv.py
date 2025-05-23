import json
import csv
import sys
import os

def json_to_csv(json_filename):
    with open(json_filename, 'r') as f:
        data = json.load(f)
    
    root_keys = list(data.keys())

    root_key = root_keys[0]
    
    records = data[root_key]

    if not records:
        print("Нет данных для записи в CSV")
        return
    
    base_dir = os.path.dirname(os.path.abspath(json_filename))
    csv_filename = os.path.join(base_dir, f"{root_key}.csv")
    
    # Запись CSV
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    
    print(f"Файл {csv_filename} успешно создан")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py example.json")
        sys.exit(1)
    
    json_filename = sys.argv[1]
    try:
        json_to_csv(json_filename)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)