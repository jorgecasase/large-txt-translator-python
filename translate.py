import time
from deep_translator import GoogleTranslator

INPUT_LANGUAGE = 'auto'  
OUTPUT_LANGUAGE = 'es'   

def translate_large_text(input_file, output_file, input_language=INPUT_LANGUAGE, target_language=OUTPUT_LANGUAGE):

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    chunk_size = 3000
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

    with open(output_file, 'w', encoding='utf-8') as file:
        for index, chunk in enumerate(chunks):
            translated = False
            attempts = 0

            while not translated and attempts < 5:
                try:
                    translated_text = GoogleTranslator(source=input_language, target=target_language).translate(chunk)
                    file.write(translated_text + "\n")
                    translated = True
                    print(f"Fragmento {index + 1}/{len(chunks)} traducido correctamente.")
                except Exception as e:
                    attempts += 1
                    print(f"Error traduciendo el fragmento {index + 1} (Intento {attempts}): {e}")
                    time.sleep(2)

            if not translated:
                print(f"Error persistente en el fragmento {index + 1}. Se omitirá.")
                file.write(f"[Error al traducir el fragmento {index + 1}]\n")

    print(f"La traducción completa se ha guardado en {output_file}")

input_path = "input.txt"
output_path = "output.txt"

translate_large_text(input_path, output_path)