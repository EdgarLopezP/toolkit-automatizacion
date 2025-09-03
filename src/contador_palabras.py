#!/usr/bin/env python3
"""
Muestra las k palabras más frecuentes de un archivo .txt (ignora stopwords comunes).

Uso:
    python src/contador_palabras.py ./notas.txt --k 10
"""
import argparse
import re
from collections import Counter
from pathlib import Path

# Palabras muy comunes en español que no cuentan para el análisis
STOPWORDS = {
    "el","la","los","las","de","y","a","en","que","un","una","por","con",
    "se","no","es","al","lo","como","del","sus","su","para","más","o"
}

def top_palabras(archivo: Path, k: int = 5):
    """
    Devuelve las k palabras más frecuentes de un archivo de texto.
    """
    texto = archivo.read_text(encoding="utf-8", errors="ignore")
    # Extraemos solo palabras (letras y acentos) y pasamos todo a minúsculas
    tokens = re.findall(r"[a-zA-ZáéíóúñÁÉÍÓÚÑ]+", texto.lower())
    tokens_filtrados = [t for t in tokens if t not in STOPWORDS]
    return Counter(tokens_filtrados).most_common(k)

def main():
    parser = argparse.ArgumentParser(description="Top k palabras más frecuentes en un .txt")
    parser.add_argument("archivo", type=Path, help="Ruta del archivo de texto")
    parser.add_argument("--k", type=int, default=5, help="Número de palabras a mostrar (por defecto 5)")
    args = parser.parse_args()

    if not args.archivo.is_file():
        raise SystemExit("El archivo indicado no existe.")

    ranking = top_palabras(args.archivo, args.k)
    for palabra, freq in ranking:
        print(f"{palabra}: {freq}")

if __name__ == "__main__":
    main()
