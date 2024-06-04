import fitz  # PyMuPDF
import re
import json
import ParsFunc,json_exl
import os
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
    print('Поместите файл pdf в папку и напишите его навзание')
    pdf_path = str(input("Название файла --->   "))
    output_file = 'output.json'

    print("начинаю работу")

    data = extract_data_from_pdf(pdf_path)
    write_data_to_json(data, output_file)
    ParsFunc.ParsRC()
    json_exl.main_json_exel()

    print('Готово файл с excel находиться в папке под именем result.xlsx')

    c=""

    while c != 'y' or c != 'yes' or c != "no" or c != "n":
        print ("Удалить файлы pdf и json которые остались во время выполнения процесса ?\n yes(y)/no(n)")
        c = str(input("--->"))
        if c == "yes" or c == "y":
            os.remove(pdf_path)
            os.remove('output.json')
            os.remove('current_cve.json')

            print ("""
                        ______              
           .d$$$******$$$$c.        
        .d$P"            "$$c      
       $$$$$.           .$$$*$.    
     .$$ 4$L*$$.     .$$Pd$  '$b   
     $F   *$. "$$e.e$$" 4$F   ^$b  
    d$     $$   z$$$e   $$     '$. 
    $P     `$L$$P` `"$$d$"      $$ 
    $$     e$$F       4$$b.     $$ 
    $b  .$$" $$      .$$ "4$b.  $$ 
    $$e$P"    $b     d$`    "$$c$F 
    '$P$$$$$$$$$$$$$$$$$$$$$$$$$$  
     "$c.      4$.  $$       .$$   
      ^$$.      $$ d$"      d$P    
        "$$c.   `$b$F    .d$P"     
          `4$$$c.$$$..e$$P"        
              `^^^^^^^`
            """)

        elif c == 'no' or c == 'n':
            print("""
                                ______              
                   .d$$$******$$$$c.        
                .d$P"            "$$c      
               $$$$$.           .$$$*$.    
             .$$ 4$L*$$.     .$$Pd$  '$b   
             $F   *$. "$$e.e$$" 4$F   ^$b  
            d$     $$   z$$$e   $$     '$. 
            $P     `$L$$P` `"$$d$"      $$ 
            $$     e$$F       4$$b.     $$ 
            $b  .$$" $$      .$$ "4$b.  $$ 
            $$e$P"    $b     d$`    "$$c$F 
            '$P$$$$$$$$$$$$$$$$$$$$$$$$$$  
             "$c.      4$.  $$       .$$   
              ^$$.      $$ d$"      d$P    
                "$$c.   `$b$F    .d$P"     
                  `4$$$c.$$$..e$$P"        
                      `^^^^^^^`
                    """)

        else:
            c = ""

if __name__ == "__main__":
    main()