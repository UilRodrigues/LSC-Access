def remover_palavras_fracas(palavras: list) -> list:
    palavras_fracas = {
        "el", "la", "los", "las", "un", "una", "unos", "unas",
        "de", "del", "al", "y", "o", "en", "con", "para", "por",
        "que", "es", "son", "ser", "estar"
    }

    return [p for p in palavras if p not in palavras_fracas]


def normalizar_texto(texto: str) -> str:
    return texto.lower()

