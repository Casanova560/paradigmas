import re
with open("quijote.txt", "r", encoding="utf-8") as f:
    quijote_text = f.read()
lines = quijote_text.splitlines()
results = []
regex1 = re.compile(r'CAP[IÍ]TULO\s+[IVXLCDM0-9]+', re.IGNORECASE)
matches1 = list(regex1.finditer(quijote_text))
results.append(f"1. Expresion: {regex1.pattern} | Resultados: {len(matches1)}")
regex2 = re.compile(r'\b(\w+)\s+y\s+(\w+)\b', re.IGNORECASE)
matches2 = list(regex2.finditer(quijote_text))
results.append(f"2. Expresion: {regex2.pattern} | Resultados: {len(matches2)}")
regex3 = re.compile(r'\b(?:pra|pre|pri|pro|pru)d', re.IGNORECASE)
matches3 = list(regex3.finditer(quijote_text))
results.append(f"3. Expresion: {regex3.pattern} | Resultados: {len(matches3)}")
regex4 = re.compile(r'\b(cra|cre|cri|cro|cru)\w*', re.IGNORECASE)
matches4 = set(m.group(0).lower() for m in regex4.finditer(quijote_text))
results.append(f"4. Expresion: {regex4.pattern} | Resultados únicos: {len(matches4)}")
regex5 = re.compile(r'\b\w*(cho|cha|che|chi|chu)\b', re.IGNORECASE)
matches5 = list(regex5.finditer(quijote_text))
results.append(f"5. Expresion: {regex5.pattern} | Resultados: {len(matches5)}")
with open("busqueda-quijote.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")

print("Analisis completo. Resultados guardados en archivo 'busqueda-quijote.txt'")

