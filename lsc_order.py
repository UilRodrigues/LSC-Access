TEMPO = {"HOY", "AYER", "MAÑANA", "FIN-DE-SEMANA"}
LUGAR = {"MONTANHA", "MAR", "CIUDAD", "CASA"}
ACAO = {"IR", "DESCANSAR", "TRABAJAR"}
SUJEITO = {"VIAJERO", "FAMÍLIA", "PERSONA"}


def ordenar_lsc(glossas: list) -> list:
    tempo = []
    lugar = []
    acao = []
    sujeito = []
    outros = []

    for g in glossas:
        if g in TEMPO:
            tempo.append(g)
        elif g in LUGAR:
            lugar.append(g)
        elif g in ACAO:
            acao.append(g)
        elif g in SUJEITO:
            sujeito.append(g)
        else:
            outros.append(g)

    return tempo + lugar + acao + sujeito + outros