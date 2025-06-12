import re
from pathlib import Path

patrones = [
    ("1415", "todas las ocurrencias de la secuencia 1415"),
    (r"1415[13579]", "1415 seguido de un dígito impar"),
    (r"[02468]{3}", "tres dígitos pares seguidos"),
    (r"999(?!9)", "999 sin cuarto 9"),
    (r"\b(?:101|103|107|109|113|127|131|137|139|149|151|157|163|167|173|179|181|191|193|197|199|211|223|227|229|233|239|241|251|257|263|269|271|277|281|283|293|307|311|313|317|331|337|347|349|353|359|367|373|379|383|389|397|401|409|419|421|431|433|439|443|449|457|461|463|467|479|487|491|499|503|509|521|523|541|547|557|563|569|571|577|587|593|599|601|607|613|617|619|631|641|643|647|653|659|661|673|677|683|691|701|709|719|727|733|739|743|751|757|761|769|773|787|797|809|811|821|823|827|829|839|853|857|859|863|877|881|883|887|907|911|919|929|937|941|947|953|967|971|977|983|991|997)\b", "números primos de 3 cifras"),
    (r"(\d)(\d)\1", "palíndromos de 3 dígitos"),
    (r"(?:123|234|345|456|567|678|789)", "secuencias ascendentes de 3 dígitos"),
    (r"(?:321|432|543|654|765|876|987)", "secuencias descendentes de 3 dígitos"),
    (r"(\d)\1{3}", "cuatro dígitos idénticos seguidos"),
    (r"(?<!\d)\d(?!\d)", "dígitos sueltos"),
    (r"[\s\n]+\d", "espacio o salto + dígito"),
]

texto = Path("Pi125MDP.txt").read_text(encoding="utf-8")
out_path = Path("busqueda-pi.txt")

with open(out_path, "w", encoding="utf-8") as f:
    for i, (pat, desc) in enumerate(patrones, start=1):
        cnt = len(re.findall(pat, texto))
        f.write(f"{i}. Expresión: {pat} | Resultados: {cnt} – {desc}\n")

