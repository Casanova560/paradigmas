import re
from pathlib import Path

def buscar(patron, desc, lines, out):
    count = 0
    out.write_text(f"{desc}\n  Regex: {patron}\n", encoding="utf-8", append=True)
    for i, line in enumerate(lines, 1):
        for m in re.finditer(patron, line):
            count += 1
            out.write_text(f"    Línea {i}, Col {m.start()+1}: {m.group()}\n", encoding="utf-8", append=True)
    out.write_text(f"  Total: {count}\n\n", encoding="utf-8", append=True)

if __name__ == '__main__':
    lines = Path("quijote.txt").read_text(encoding="utf-8").splitlines()
    out = Path("busqueda-quijote.txt")
    out.write_text("", encoding="utf-8")
    buscar(r"(?i)cap[ií]tulo\s+[IVXLC0-9]+", "1. Cabeceras de capítulo", lines, out)
    buscar(r"\b\w+\s+y\s+\w+\b", "2. 'y' con palabras adyacentes", lines, out)
    buscar(r"\bpr[aeiou]d", "3. pra|pre|pri|pro|pru + d", lines, out)
    buscar(r"\b(\w)\w*\1\b", "4. Palabras palindrómicas", lines, out)
    buscar(r"[áéíóúÁÉÍÓÚ]", "5. Vocales acentuadas", lines, out)