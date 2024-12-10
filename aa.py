import json
from PyPDF2 import PdfReader

def pdf_to_json(pdf_path, output_json_path):
    # Lê o PDF
    reader = PdfReader(pdf_path)
    pdf_data = {"pages": []}

    # Extrai texto de cada página
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        pdf_data["pages"].append({
            "page_number": i + 1,
            "content": page_text.strip() if page_text else ""
        })

    # Salva em um arquivo JSON
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(pdf_data, json_file, ensure_ascii=False, indent=4)

    print(f"PDF convertido para JSON e salvo em {output_json_path}")

# Exemplo de uso
pdf_to_json("qualificacacomatadoraspin.pdf", "qualificacacomatadoraspin.json")
