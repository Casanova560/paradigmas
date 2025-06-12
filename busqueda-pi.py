import re
from pathlib import Path

def contar(p, d, t):
    m = re.findall(p, t)
    return f"{d}\n  Regex: {p}\n  Count: {len(m)}\n\n"

pi = Path("Pi125MDP.txt").read_text(encoding="utf-8")
out_path = Path("busqueda-pi.txt")

with open(out_path, "w", encoding="utf-8"):
    pass

with open(out_path, "a", encoding="utf-8") as f:
    f.write(contar("1415", "1. Secuencia '1415'", pi))
    f.write(contar(r"1415[13579]", "2. '1415' + impar", pi))
    f.write(contar(r"[02468]{3}", "3. Tres dígitos pares seguidos", pi))
    f.write(contar(r"999(?!9)", "4. '999' sin cuarto '9'", pi))
    primos = "|".join([
        "101","103","107","109","113","127","131","137","139","149","151","157","163","167","173","179",
        "181","191","193","197","199","211","223","227","229","233","239","241","251","257","263","269",
        "271","277","281","283","293","307","311","313","317","331","337","347","349","353","359","367",
        "373","379","383","389","397","401","409","419","421","431","433","439","443","449","457","461",
        "463","467","479","487","491","499","503","509","521","523","541","547","557","563","569","571",
        "577","587","593","599","601","607","613","617","619","631","641","643","647","653","659","661",
        "673","677","683","691","701","709","719","727","733","739","743","751","757","761","769","773",
        "787","797","809","811","821","823","827","829","839","853","857","859","863","877","881","883",
        "887","907","911","919","929","937","941","947","953","967","971","977","983","991","997"
    ])
    f.write(contar(fr"\b(?:{primos})\b", "5. Números primos de 3 cifras", pi))
    f.write(contar(r"(\d)(\d)\1", "6. Palíndromos de 3 dígitos", pi))
    f.write(contar(r"(?=(\d)(\d)(\d))(?=\1<\2<\3)", "7. Secuencias ascendentes de 3 dígitos", pi))
    f.write(contar(r"(?=(\d)(\d)(\d))(?=\1>\2>\3)", "8. Secuencias descendentes de 3 dígitos", pi))
    f.write(contar(r"(\d)\1{3}", "9. Cuatro dígitos idénticos seguidos", pi))
    f.write(contar(r"(?<!\d)(\d)(?!\d)", "10. Dígitos sueltos", pi))
    f.write(contar(r"[\s\n]+\d", "11. Espacio/salto + dígito", pi))
