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
    frase = normalizar_texto(frase)
    palavras_filtradas = remover_palavras_fracas(frase)
    glossas = converter_para_glossa(palavras_filtradas)
    glossas_ordenadas = ordenar_lsc(glossas)
    return " ".join(glossas_ordenadas)

frase = "A pesar de que, en el ámbito de la programación y del análisis de datos, aún se subestime la importancia de la correcta codificación, es decir, del uso adecuado de caracteres con acento, como á, é, í, ó y ú, así como de la ñ, resulta evidente que, sin una atención previa a estos detalles, los resultados pueden ser incorrectos o incluso inconsistentes, ya que, por ejemplo, al comparar cadenas o al procesar texto con múltiples preposiciones y conectivos, se pueden generar errores difíciles de detectar."
resultado = texto_para_lsc(frase)

print(resultado)


 

# Dividir por un separador específico (ej. O, un, de, para, que, ...)
#a_phrase = "El viajero fue desde la montaña hacia el mar para descansar con su familia en un hotel junto a la playa durante el fin de semana"
#partes = a_phrase.split()
#new_string = partes
#my_list = []
#my_list.append(new_string)




# Usando lower()
#texto_minusculo_lower = a_phrase.lower()
#print(f"lower(): {texto_minusculo_lower}") # Saída: 

#palavrasParaRemover = ["el", "a","la", "un", "en", "con"]

# Filtrando
#novo_array = [partes for partes in my_list if partes not in palavrasParaRemover]

#print(novo_array)  # Saída: 



#frase_test = "¿Qué te parece si mañana jugamos fútbol? Mi mamá le compró a mi hermana una nueva muñeca. Hoy iré a la playa en un camión."
#textoSemAcentos = remover_acentos(frase_test)


#frase = "El viajero fue desde la montaña hacia el mar con su familia"
#palavras_remover = ["el", "la", "un", "en", "con"]

#resultado = remover_palavras(frase, palavras_remover)

#print(resultado)


    