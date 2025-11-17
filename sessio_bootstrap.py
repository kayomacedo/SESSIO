import os
import sys

def bootstrap():
    ROOT = os.path.dirname(os.path.abspath(__file__))  # diretorio atual = raiz
    if ROOT not in sys.path:
        sys.path.append(ROOT)

bootstrap()
