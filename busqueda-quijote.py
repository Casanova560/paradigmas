import re
from pathlib import Path

patrones = [
    (r"(?i)cap[ií]tulo\s+[IVXLC0-9]+", "cabeceras de capítulo"),
    (r"\b\w+\s+y\s+\w+\b", "la 'y' con palabras adyacentes"),
    (r"\bpr[aeiou]d", "pra|pre|pri|pro|pru + d"),
    (r"\b(\w)\w*\1\b", "palabras palindrómicas"),
    (r"[áéíóúÁÉÍÓÚ]", "vocales acentuadas"),
]

lines = Path("quijote.txt").read_text(encoding="utf-8").splitlines()
out_path = Path("busqueda-quijote.txt")

with open(out_path, "w", encoding="utf-8") as f:
    for i, (pat, desc) in enumerate(patrones, start=1):
        found = []
        for ln, line in enumerate(lines, start=1):
            for m in re.finditer(pat, line):
                found.append(f"Línea {ln}, Col {m.start()+1}: {m.group()}")
        unique = sorted(set(found))
        f.write(f"{i}. Expresión: {pat} | Resultados únicos: {len(unique)}\n")
        for u in unique:
            f.write(f"    {u}\n")

