def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "combustível insuficiente"
    
    if clima != "bom":
        return "clima desfavorável"
    
    if not sistema_ok:
        return "falha no sistema"
    
    return "lançamento autorizado"