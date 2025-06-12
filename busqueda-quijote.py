import re
from pathlib import Path

def buscar(p, d, L, out):
    c = 0
    out.write(f"{d}\n  Regex: {p}\n")
    for i, line in enumerate(L, 1):
        for m in re.finditer(p, line):
            c += 1
            out.write(f"    Línea {i}, Col {m.start()+1}: {m.group()}\n")
    out.write(f"  Total: {c}\n\n")

L = Path("quijote.txt").read_text(encoding="utf-8").splitlines()
out_path = Path("busqueda-quijote.txt")

with open(out_path, "w", encoding="utf-8"):
    pass

with open(out_path, "a", encoding="utf-8") as f:
    buscar(r"(?i)cap[ií]tulo\s+[IVXLC0-9]+", "1. Cabeceras de capítulo", L, f)
    buscar(r"\b\w+\s+y\s+\w+\b", "2. 'y' con palabras adyacentes", L, f)
    buscar(r"\bpr[aeiou]d", "3. pra|pre|pri|pro|pru + d", L, f)
    buscar(r"\b(\w)\w*\1\b", "4. Palabras palindrómicas", L, f)
    buscar(r"[áéíóúÁÉÍÓÚ]", "5. Vocales acentuadas", L, f)
