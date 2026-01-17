#from removeTildes import remover_acentos
from wordsLower import remover_palavras
from text_processing import normalizar_texto, remover_palavras_fracas
from lsc_dictionary import LSC_DICTIONARY
from lsc_order import ordenar_lsc
from removeTildes import remover_acentos



def converter_para_glossa(palavras: list) -> list:
    glossas = []
    for p in palavras:
        glossas.append(LSC_DICTIONARY.get(p, p.upper()))
    return glossas

def texto_para_lsc(frase: str) -> str:
    frase = remover_acentos(frase)
    frase = normalizar_texto(frase)

    palavras = frase.split()
    palavras_filtradas = remover_palavras_fracas(palavras)

    glossas = converter_para_glossa(palavras_filtradas)
    glossas_ordenadas = ordenar_lsc(glossas)

    return " ".join(glossas_ordenadas)



