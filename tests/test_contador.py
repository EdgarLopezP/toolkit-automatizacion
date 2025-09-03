from pathlib import Path
from src.contador_palabras import top_palabras

def test_top_palabras_filtra_stopwords(tmp_path: Path):
    texto = "Python es genial. Python y datos, datos y código. Código limpio."
    f = tmp_path / "notas.txt"
    f.write_text(texto, encoding="utf-8")

    ranking = top_palabras(f, k=3)
    palabras = {p for p, _ in ranking}
    assert {"python", "datos", "código"} & palabras
    assert any(freq >= 2 for _, freq in ranking)
