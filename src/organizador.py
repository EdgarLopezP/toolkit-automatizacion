#!/usr/bin/env python3
"""
Organiza archivos en subcarpetas según su extensión:
- imagenes: .jpg, .png, .gif...
- documentos: .pdf, .docx, .txt...
- datos: .csv, .json, .xlsx...
- otros: el resto

Uso:
    python src/organizador.py /ruta/a/carpeta --dry-run
"""
import argparse, shutil
from pathlib import Path

EXT_MAP = {
    "imagenes": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "documentos": {".pdf", ".doc", ".docx", ".txt", ".md"},
    "datos": {".csv", ".json", ".xlsx"},
}

def clasificar_archivo(path: Path) -> str:
    ext = path.suffix.lower()
    for carpeta, extensiones in EXT_MAP.items():
        if ext in extensiones:
            return carpeta
    return "otros"

def organizar(origen: Path, dry_run: bool = False) -> int:
    movidos = 0
    for p in origen.iterdir():
        if not p.is_file():
            continue
        destino_dir = origen / clasificar_archivo(p)
        destino_dir.mkdir(exist_ok=True)
        destino = destino_dir / p.name
        if not dry_run:
            shutil.move(str(p), str(destino))
        movidos += 1
    return movidos

def main():
    parser = argparse.ArgumentParser(description="Organiza archivos por tipo en subcarpetas.")
    parser.add_argument("carpeta", type=Path, help="Ruta de la carpeta a organizar")
    parser.add_argument("--dry-run", action="store_true", help="Simula sin mover archivos")
    args = parser.parse_args()

    if not args.carpeta.is_dir():
        raise SystemExit("La ruta indicada no existe o no es una carpeta.")

    total = organizar(args.carpeta, args.dry_run)
    print(f"Procesados {total} archivos. {'(simulación)' if args.dry_run else ''}")

if __name__ == "__main__":
    main()
