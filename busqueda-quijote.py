import re
from pathlib import Path

texto = Path("quijote.txt").read_text(encoding="utf-8")
filtros = {
    1: (r"(?i)\bcap[ií]tulo\s+[IVXLC0-9]+\b", "cabeceras de capítulo"),
    2: (r"\b\w+\s+y\s+\w+\b", "‘y’ entre palabras"),
    3: (r"(?i)\bpr[aeiou]d\w*\b", "pra|pre|pri|pro|pru + d"),
    4: (r"\b(?:cra|cre|cri|cro|cru)\w*\b", "palabras que empiezan cra|…|cru"),
    5: (r"\b\w*(?:cho|cha|che|chi|chu)\b", "palabras que terminan en cho|…|chu"),
}

with open("busqueda-quijote.txt", "w", encoding="utf-8") as salida:
    for idx, (pat, desc) in filtros.items():
        cnt = len(list(re.finditer(pat, texto)))
        salida.write(f"{idx}. Expresión: {pat} | Resultados: {cnt} – {desc}\n")



