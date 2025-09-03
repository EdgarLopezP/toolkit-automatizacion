import os
import sys

# Añade la raíz del proyecto al sys.path para poder hacer: from src.modulo import ...
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
