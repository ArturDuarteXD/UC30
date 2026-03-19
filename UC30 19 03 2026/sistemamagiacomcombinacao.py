def tipo_magia(fogo, agua):
    if fogo and agua:
        return "vapor"
    elif fogo:
        return "fogo"
    elif agua:
        return "agua"
    else:
        return "sem magiaa"