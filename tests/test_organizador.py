from pathlib import Path
from src.organizador import clasificar_archivo, organizar

def test_clasificar_archivo_basico(tmp_path: Path):
    img = tmp_path / "foto.jpg"; img.write_bytes(b"x")
    doc = tmp_path / "informe.pdf"; doc.write_bytes(b"x")
    dat = tmp_path / "datos.csv"; dat.write_bytes(b"x")
    otro = tmp_path / "script.sh"; otro.write_text("#!/bin/sh\necho hi\n")

    assert clasificar_archivo(img) == "imagenes"
    assert clasificar_archivo(doc) == "documentos"
    assert clasificar_archivo(dat) == "datos"
    assert clasificar_archivo(otro) == "otros"

def test_organizar_mueve_archivos(tmp_path: Path):
    a = tmp_path / "a.jpg"; a.write_bytes(b"x")
    b = tmp_path / "b.pdf"; b.write_bytes(b"x")
    c = tmp_path / "c.csv"; c.write_bytes(b"x")

    movidos = organizar(tmp_path, dry_run=False)
    assert movidos == 3
    assert (tmp_path / "imagenes" / "a.jpg").exists()
    assert (tmp_path / "documentos" / "b.pdf").exists()
    assert (tmp_path / "datos" / "c.csv").exists()
