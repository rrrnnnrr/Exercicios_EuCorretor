def ladderLength(inicio, fim, dicionario):
    conjuntoPalavras = set(dicionario)

    if fim not in conjuntoPalavras:
        return 0

    comeco = {inicio}
    final = {fim}
    conjuntoPalavras.remove(fim)
    indice = 1

    while comeco and final:
        if len(comeco) > len(final):
            comeco, final = final, comeco

        proximoConjunto = set()
        for palavra in comeco:
            for i in range(len(palavra)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    novaPalavra = palavra[:i] + c + palavra[i+1:]

                    if novaPalavra in final:
                        return indice + 1

                    if novaPalavra in conjuntoPalavras:
                        proximoConjunto.add(novaPalavra)
                        conjuntoPalavras.remove(novaPalavra)

        comeco = proximoConjunto
        indice += 1

    return 0
