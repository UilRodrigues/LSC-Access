import unicodedata

def remover_acentos(texto: str) -> str:

    if not isinstance(texto, str):
        raise TypeError("El argumento debe ser una cadena de texto (str).")
    
    # Normaliza el texto a forma NFD (descompone caracteres con acento)
    texto_normalizado = unicodedata.normalize('NFD', texto)
    
    # Filtra caracteres que no sean marcas diacríticas (Mn)
    texto_sin_acentos = ''.join(
        c for c in texto_normalizado
        if unicodedata.category(c) != 'Mn'
    )
    
    return texto_sin_acentos

# Ejemplo de uso
texto_original = "Canción número veintidós: Árbol, corazón y pingüino."
#print("Original:", texto_original)
#print("Sin acentos:", remover_acentos(texto_original))