#!/usr/bin/env python3
"""
Renombra en lote los archivos de una carpeta con el patrón: <prefijo>_<n>.<ext>

Uso:
    python src/renombrador.py /ruta/a/carpeta --prefijo fotos --inicio 1 --dry-run
"""
import argparse
from pathlib import Path

def renombrar(carpeta: Path, prefijo: str, start: int = 1, simulate: bool = False) -> int:
    """
    Renombra todos los archivos de 'carpeta' con un prefijo y numeración incremental.
    """
    n = start
    cambios = 0
    for p in sorted(carpeta.iterdir()):
        if not p.is_file():
            continue
        nuevo = p.with_name(f"{prefijo}_{n}{p.suffix.lower()}")
        if not simulate:
            p.rename(nuevo)
        cambios += 1
        n += 1
    return cambios

def main():
    parser = argparse.ArgumentParser(description="Renombra archivos en lote con un prefijo.")
    parser.add_argument("carpeta", type=Path, help="Carpeta con archivos a renombrar")
    parser.add_argument("--prefijo", required=True, help="Prefijo del nuevo nombre")
    parser.add_argument("--inicio", type=int, default=1, help="Número inicial (por defecto 1)")
    parser.add_argument("--dry-run", action="store_true", help="Simula sin renombrar")
    args = parser.parse_args()

    if not args.carpeta.is_dir():
        raise SystemExit("La ruta indicada no existe o no es una carpeta.")

    total = renombrar(args.carpeta, args.prefijo, args.inicio, args.dry_run)
    print(f"Renombrados {total} archivos. {'(simulación)' if args.dry_run else ''}")

if __name__ == "__main__":
    main()
