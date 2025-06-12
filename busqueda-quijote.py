import re
from pathlib import Path

texto = Path("quijote.txt").read_text(encoding="utf-8")
lineas = texto.splitlines()
filtros = {
    1: (r"(?i)\bcap[ií]tulo\s+[IVXLC0-9]+\b",          "cabeceras de capítulo"),
    2: (r"\b\w+\s+y\s+\w+\b",                          "‘y’ entre palabras"),
    3: (r"\bpr[aeiou]d\b",                             "pra|pre|pri|pro|pru + d"),
    4: (r"\b(?:cra|cre|cri|cro|cru)\w*\b",             "palabras que empiezan cra|cre|…|cru"),
    5: (r"\b\w*(?:cho|cha|che|chi|chu)\b",             "palabras que terminan en cho|cha|…|chu"),
}

with open("busqueda-quijote.txt", "w", encoding="utf-8") as salida:
    for idx, (pat, desc) in filtros.items():
        ocurrencias = []
        for n, ln in enumerate(lineas, 1):
            for m in re.finditer(pat, ln):
                ocurrencias.append(f"Línea {n}, Col {m.start()+1}: {m.group()}")
        unica = sorted(set(ocurrencias), key=lambda x: (int(x.split()[1].strip(',')), int(x.split()[3].rstrip(':'))))
        salida.write(f"{idx}. Expresión: {pat} | Resultados únicos: {len(unica)} – {desc}\n")
        for reg in unica:
            salida.write(f"    {reg}\n")


