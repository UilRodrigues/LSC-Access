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





# EXECUÇÃO


 

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


    