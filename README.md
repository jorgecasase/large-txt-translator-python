# Large txt translator with python

<img src="https://github.com/jorgecasase/github-repos-img/blob/main/img/python.png" alt="python" height="100"/>

## Features

- Automatically detects the language of the input text or uses a specified input language.
- Translates text in chunks of up to 3000 characters.
- Retries translation for up to 5 attempts per chunk if an error occurs.
- Saves translated text incrementally to prevent data loss in case of interruptions.
- Allows customization of input and output languages.

## Requirements

- Python 3.6 or higher
- Installed Python packages:
  - `deep-translator`

## Installation

1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install deep-translator
   ```

## Usage

1. Place the text file to be translated in the same directory as the script, or provide the full path to the file.
2. Modify the following constants in the script to set your desired input and output languages:
   ```python
   INPUT_LANGUAGE = 'auto'  # Change 'auto' to a specific language code if needed
   OUTPUT_LANGUAGE = 'es'   # Set the target language (e.g., 'fr' for French, 'de' for German)
   ```
3. Run the script:
   ```bash
   python traduccion.py
   ```
4. The translated text will be saved in the specified output file (e.g., `hitler_spanish.txt`).

## Configuration

### Input and Output Files

- `input_path`: Path to the file you want to translate (default is `hitler.txt`).
- `output_path`: Path to save the translated file (default is `hitler_spanish.txt`).

### Language Selection

Modify these constants to set your desired input and output languages:
- `INPUT_LANGUAGE`: Language code of the input text (e.g., `'en'` for English, `'fr'` for French).
- `OUTPUT_LANGUAGE`: Language code for the translation output (e.g., `'es'` for Spanish).

### Chunk Size

The script processes text in chunks of 3000 characters to comply with Deep Translator limits. You can adjust this value by modifying:
```python
chunk_size = 3000
```

## Error Handling

- The script retries failed translations up to 5 times.
- If a chunk cannot be translated, it is logged in the output file with a placeholder.

## Example

### Input (`example.txt`):
```
This is an example text that will be translated into another language.
```

### Output (`example_oputput.txt`):
```
Este es un texto de ejemplo que se traducirá a otro idioma.
```
