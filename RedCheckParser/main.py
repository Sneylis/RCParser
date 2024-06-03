import fitz  # PyMuPDF
import re
import json

def extract_data_from_pdf(pdf_path):
    # Открываем PDF файл
    document = fitz.open(pdf_path)
    data = {}

    # Регулярное выражение для поиска хостов и CVE
    host_regex = re.compile(r'Хост:\s*([^\s]+)')
    cve_regex = re.compile(r'CVE-\d{4}-\d+')

    current_host = None

    # Проходим по каждой странице PDF
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text = page.get_text()



        # Ищем хосты и CVE
        for line in text.split('\n'):
            host_match = host_regex.search(line)
            if host_match:
                current_host = host_match.group(1)
                if current_host not in data:
                    data[current_host] = []


            cve_matches = cve_regex.findall(line)
            if current_host and cve_matches:
                data[current_host].extend(cve_matches)


    return data

def write_data_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    pdf_path = 'KKB2_10.1.6.0.pdf'
    output_file = 'output.json'

    data = extract_data_from_pdf(pdf_path)
    write_data_to_json(data, output_file)
    print(f'Data extracted and written to {output_file}')

if __name__ == "__main__":
    main()