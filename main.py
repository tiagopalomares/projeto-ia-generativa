import os
import pytesseract # type: ignore
from PIL import Image # type: ignore

# Diretórios
input_dir = "inputs"
output_dir = "output"

# Certifique-se de que a pasta output existe
os.makedirs(output_dir, exist_ok=True)

# Listar imagens na pasta inputs
images = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

for image_name in images:
    img_path = os.path.join(input_dir, image_name)
    img = Image.open(img_path)
    
    # Extrair texto
    extracted_text = pytesseract.image_to_string(img, lang="por")  # Ajuste o idioma se necessário
    
    # Salvar saída
    output_file = os.path.join(output_dir, f"{image_name}.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)
    
    print(f"Texto extraído de {image_name} salvo em {output_file}")
