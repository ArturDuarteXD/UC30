def rank_jogador(pontos, derrotas):
    pontos_finais = pontos - (derrotas * 10)
    
    if pontos_finais < 0:
        return "banido"
    
    if pontos_finais < 100:
        return "bronze"
    elif pontos_finais < 300:
        return "prata"
    elif pontos_finais < 600:
        return "ouro"
    else:
        return "diamante"