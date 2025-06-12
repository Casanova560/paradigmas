import re
from pathlib import Path

texto = Path("Pi125MDP.txt").read_text(encoding="utf-8")
criterios = {
    1: (r"1415",                          "todas las ocurrencias de 1415"),
    2: (r"1415[13579]",                   "1415 seguido de un dígito impar"),
    3: (r"[02468]{3}",                    "tres dígitos pares seguidos"),
    4: (r"(?:[02468]{3}9)",               "tres dígitos pares seguidos de un 9"),
    5: (r"(?:[02468]{3}[13579])",         "tres dígitos pares seguidos de un dígito impar"),
    6: (r"(?:[02468]{3}[09])",            "tres dígitos pares seguidos de un 0 o un 9"),
    7: (r"[02468]{2}(?:[13579]{1,3})?",   "dos dígitos pares con 1–3 impares opcionales"),
    8: (r"[13579]{2}0",                   "dos dígitos impares seguidos de un 0"),
    9: (r"[13579](?:[02468]{2,})",        "un dígito impar seguido de al menos dos pares"),
    10:(r"11[13579]",                     "111,113,115,117 o 119"),
    11:(r"11[13579][02468]",              "111,113,115,117 o 119 seguidos de un dígito par"),
}

with open("busqueda-pi.txt", "w", encoding="utf-8") as salida:
    for i, (pat, desc) in criterios.items():
        cnt = len(re.findall(pat, texto))
        salida.write(f"{i}. Expresión: {pat} | Resultados: {cnt} – {desc}\n")




