import json

with open('Tubes_DIP_LogisticRegression.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        new_source = []
        for line in cell.get('source', []):
            # Fix 1: Comment out Colab specific lines
            if 'google.colab import files' in line:
                new_source.append('# ' + line)
            elif 'files.download' in line:
                new_source.append('# ' + line)
            elif 'google.colab import drive' in line:
                new_source.append('# ' + line)
            elif 'drive.mount' in line:
                new_source.append('# ' + line)
            elif 'to_csv(\'/content/drive/MyDrive' in line:
                new_source.append('# ' + line)
            # Fix 2: Handle NaN in TF-IDF
            elif "X = df['final_text']" in line and 'fillna' not in line:
                new_source.append("X = df['final_text'].fillna('')\n")
            # Fix 3: Remove multi_class='multinomial' from LogisticRegression
            elif "LogisticRegression(" in line and 'multi_class' in line:
                line = line.replace("multi_class='multinomial', ", "")
                line = line.replace("multi_class='multinomial'", "")
                new_source.append(line)
            else:
                new_source.append(line)
        cell['source'] = new_source
        
        # Clear existing outputs and execution counts so it runs fresh
        cell['outputs'] = []
        cell['execution_count'] = None

with open('Tubes_DIP_LogisticRegression.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook successfully fixed.")
