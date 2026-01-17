# =====================
# TEMPO
# =====================
TEMPO = {
    "HOY", "AYER", "MAÑANA", "AHORA", "ANTES", "DESPUES",
    "SIEMPRE", "NUNCA", "DIA", "SEMANA", "AÑO", "FIN-DE-SEMANA", "TIEMPO"
}

# =====================
# LUGAR
# =====================
LUGAR = {
    "CASA", "ESCUELA", "UNIVERSIDAD", "TRABAJO", "HOSPITAL",
    "CIUDAD", "PAIS", "MONTAÑA", "MAR", "CALLE"
}

# =====================
# SUJEITO
# =====================
SUJEITO = {
    "YO", "TU", "USTED", "EL", "ELLA", "NOSOTROS", "ELLOS",
    "PERSONA", "GENTE", "HOMBRE", "MUJER", "NIÑO",
    "FAMILIA", "VIAJERO"
}

# =====================
# AÇÃO (VERBOS)
# =====================
ACAO = {
    "IR", "VENIR", "LLEGAR", "SALIR",
    "COMER", "BEBER", "DORMIR",
    "TRABAJAR", "ESTUDIAR", "VIVIR",
    "GUSTAR", "QUERER", "NECESITAR",
    "TENER", "SER", "ESTAR",
    "HACER", "VER", "HABLAR", "PENSAR",
    "DESCANSAR"
}

# =====================
# OBJETOS / CONCEITOS
# =====================
OBJETO = {
    "MANZANA", "NUMERO", "TODO", "NADA", "ALGO",
    "MAS", "MENOS"
}

# =====================
# QUALIDADES / ESTADOS
# =====================
QUALIDADE = {
    "BUENO", "MALO", "GRANDE", "PEQUEÑO",
    "FELIZ", "TRISTE", "CANSADO", "ENFERMO",
    "RAPIDO", "LENTO", "MUCHO", "POCO"
}


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