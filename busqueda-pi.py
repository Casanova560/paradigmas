import re
from pathlib import Path

texto = Path("Pi125MDP.txt").read_text(encoding="utf-8")
criterios = {
    1: (r"1415", "todas las ocurrencias de 1415"),
    2: (r"1415[13579]", "1415 + dígito impar"),
    3: (r"[02468]{3}", "tres pares consecutivos"),
    4: (r"999(?!9)", "‘999’ sin cuarto 9"),
    5: (r"\b(?:101|103|107|109|113|127|131|137|139)\b", "primos de 3 cifras (ejemplo)"),
    6: (r"(\d)(?!\1)\1", "palíndromo interno de 3 cifras"),
    7: (r"(?:(?<=0)12|(?<=1)23|(?<=2)34)", "secuencias ascendentes cortas"),
    8: (r"(?:(?<=3)21|(?<=4)32|(?<=5)43)", "secuencias descendentes cortas"),
    9: (r"(\d)\1{3}", "cuatro dígitos idénticos"),
    10: (r"(?<!\d)\d(?!\d)", "dígito aislado"),
    11: (r"[\r\n]+\d", "salto/retorno + dígito"),
}

with open("busqueda-pi.txt", "w", encoding="utf-8") as salida:
    for i, (pat, desc) in criterios.items():
        cuenta = len(re.findall(pat, texto))
        salida.write(f"{i}. Expresión: {pat} | Resultados: {cuenta} – {desc}\n")


