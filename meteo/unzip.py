import os
import zipfile

caminho = '../static/meteo'

    
for filename in os.listdir(caminho):
    if filename.endswith('.zip'):
        zip_path = os.path.join(caminho, filename)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if file.endswith('.svg'):
                    zip_ref.extract(file, caminho)
                    print(f"Arquivo {file} extraído com sucesso para {caminho}")

print("Processo de descompressão concluído.")
