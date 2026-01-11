PALAVRAS_REMOVER = {
    "el", "la", "los", "las",
    "un", "una",
    "de", "del", "al",
    "con", "para", "en",
    "desde", "hacia", "por",
    "su", "sus"
}


def normalizar_texto(texto: str) -> str:
    return texto.lower()


def remover_palavras_fracas(texto: str) -> list:
    palavras = texto.split()
    return [p for p in palavras if p not in PALAVRAS_REMOVER]