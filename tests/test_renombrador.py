from pathlib import Path
from src.renombrador import renombrar

def test_renombrar_secuencial(tmp_path: Path):
    (tmp_path / "uno.txt").write_text("x")
    (tmp_path / "dos.txt").write_text("x")
    (tmp_path / "tres.txt").write_text("x")

    total = renombrar(tmp_path, prefijo="fich", start=5, simulate=False)
    assert total == 3
    assert (tmp_path / "fich_5.txt").exists()
    assert (tmp_path / "fich_6.txt").exists()
    assert (tmp_path / "fich_7.txt").exists()
