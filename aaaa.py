import pandas as pd
import json

def xlsx_to_json(xlsx_file, json_file):
    # Read the Excel file
    df = pd.read_excel(xlsx_file)
    
    # Convert the DataFrame to a dictionary
    data_dict = df.to_dict(orient='records')
    
    # Write the dictionary to a JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=4)

# Example usage
xlsx_file = 'treinamento.xlsx'
json_file = 'treinamento.json'
xlsx_to_json(xlsx_file, json_file)