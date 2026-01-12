def remover_palavras(frase, palavras_para_remover):
    frase = frase.lower()
    palavras = frase.split()

    palavras_para_remover = set(palavras_para_remover)

    palavras_filtradas = [
        palavra for palavra in palavras if palavra not in palavras_para_remover
    ]

    return " ".join(palavras_filtradas)







