import json
import pandas as pd


def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


def write_data_to_excel(data, excel_file):
    rows = []

    for host, cves in data.items():
        for cve in cves:
            rows.append({'Host': host, 'CVE': cve})

    df = pd.DataFrame(rows)
    df.to_excel(excel_file, index=False)


def main():
    json_file = 'output.json'
    excel_file = 'output.xlsx'

    data = read_json(json_file)
    write_data_to_excel(data, excel_file)
    print(f'Data written to {excel_file}')


if __name__ == "__main__":
    main()