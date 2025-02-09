import os
import hashlib
from collections import defaultdict

def find_modified_by_hash(files):

    hash_map = defaultdict(list)
    
    for file in files:
        try:
            with open(file, "rb") as f:
                data = f.read()
        except Exception as e:
            print(f"Erro ao ler o(s) arquivos {file}: {e}")
            continue
        
        file_hash = hashlib.sha256(data).hexdigest()
        hash_map[file_hash].append(file)
    
    for hash_val, file_list in hash_map.items():
        if len(file_list) == 1:
            print(f"[UTILIZANDO O METODO HASH] Arquivo alterado: {file_list[0]}")
            return
    print("[UTILIZANDO O METODO HASH] Possivelmente não existe arquivos alterado.")

def find_modified_by_comparison(files):

    contents = {}  
    
    for file in files:
        try:
            with open(file, "rb") as f:
                contents[file] = f.read()
        except Exception as e:
            print(f"Erro ao ler o(s) arquivos {file}: {e}")
            continue

    count_content = defaultdict(int)
    for content in contents.values():
        count_content[content] += 1

    reference_content = max(count_content, key=count_content.get)

    for file, content in contents.items():
        if content != reference_content:
            print(f"[UTILIZANDO O METODO DE VERIFICAÇÃO DE BYTES] Arquivo alterado: {file}")
            return
    print("[UTILIZANDO O METODO DE VERIFICAÇÃO DE BYTESa] Nenhum arquivo alterado identificado.")

def main():

    pasta = "C:\\Users\\DARM\\Desktop\\WP-IFCE\\WP-AUDITORIA\\imgs" #Alterar o caminho da parta

    files = [os.path.join(pasta, f) for f in os.listdir(pasta) 
             if os.path.isfile(os.path.join(pasta, f))]
    
    if len(files) < 1:
        print(f"A pasta '{pasta}' menos que 1 arquivo. Não é possivel realizar comparação")
        return

    print("Verificação por hash:")
    find_modified_by_hash(files)

    print("\nVerificação por comparação por Byte:")
    find_modified_by_comparison(files)

if __name__ == "__main__":
    main()
