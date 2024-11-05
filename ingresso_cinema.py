diaSemana = int(input())
horaSessao = int(input())
minutoSessao = int(input())
estudaSimNao = str(input())
formaPgto = str(input())

precoInicial = float()
ingresso = float()
desconto = float()

# primeiro o programa verifica o dia da sessão, depois a hora da sessão, depois se a pessoa é estudante ou não,
# e por fim a forma de pagamento (se for estudante a forma de pagamento não é considerada)

if diaSemana == 1 : # no domingo não é necessário considerar horário pois o preço é o mesmo em qualquer um
    precoInicial = 30.00
    if estudaSimNao == "S" :
        ingresso = precoInicial / 2
    elif estudaSimNao == "N" :
        if formaPgto == "D" :
            ingresso = precoInicial
        elif formaPgto == "C" :
            desconto = (0.3 * precoInicial)
            ingresso = precoInicial - desconto
            
elif diaSemana == 2 :
    if horaSessao == 18 and minutoSessao >= 30 and minutoSessao <= 59 : #sessão noturna (entre 18:30 e 18:59)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao >= 19 and minutoSessao >= 0 and minutoSessao <= 59 : #sessão noturna (após as 19)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao == 18 and minutoSessao >= 0 and minutoSessao <= 29 : #sessão vespertina (entre 18:00 e 18:29)
        precoInicial = 15.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao < 18 : #sessão vespertina (antes das 18)
        precoInicial = 15.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
elif diaSemana == 3 :
    if horaSessao == 18 and minutoSessao >= 30 and minutoSessao <= 59 : #sessão noturna (entre 18:30 e 18:59)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao >= 19 and minutoSessao >= 0 and minutoSessao <= 59 : #sessão noturna (após as 19)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao == 18 and minutoSessao >= 0 and minutoSessao <= 29 : #sessão vespertina (entre 18:00 e 18:29)
        precoInicial = 15.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao < 18 : #sessão vespertina (antes das 18)
        precoInicial = 15.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto

elif diaSemana == 4 :
    if horaSessao == 18 and minutoSessao >= 30 and minutoSessao <= 59 : #sessão noturna (entre 18:30 e 18:59)
        precoInicial = 30.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao >= 19 and minutoSessao >= 0 and minutoSessao <= 59 : #sessão noturna (após as 19)
        precoInicial = 30.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao == 18 and minutoSessao >= 0 and minutoSessao <= 29 : #sessão vespertina (entre 18:00 e 18:29)
        precoInicial = 15.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao < 18 : #sessão vespertina (antes das 18)
        precoInicial = 15.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto

elif diaSemana == 5 :
    if horaSessao == 18 and minutoSessao >= 30 and minutoSessao <= 59 : #sessão noturna (entre 18:30 e 18:59)
        precoInicial = 30.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao >= 19 and minutoSessao >= 0 and minutoSessao <= 59 : #sessão noturna (após as 19)
        precoInicial = 30.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao == 18 and minutoSessao >= 0 and minutoSessao <= 29 : #sessão vespertina (entre 18:00 e 18:29)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao < 18 : #sessão vespertina (antes das 18)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
                
elif diaSemana == 6 :
    if horaSessao == 18 and minutoSessao >= 30 and minutoSessao <= 59 : #sessão noturna (entre 18:30 e 18:59)
        precoInicial = 40.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.3 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao >= 19 and minutoSessao >= 0 and minutoSessao <= 59 : #sessão noturna (após as 19)
        precoInicial = 40.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.3 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao == 18 and minutoSessao >= 0 and minutoSessao <= 29 : #sessão vespertina (entre 18:00 e 18:29)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao < 18 : #sessão vespertina (antes das 18)
        precoInicial = 20.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.5 * precoInicial)
                ingresso = precoInicial - desconto
                
elif diaSemana == 7 :
    if horaSessao == 18 and minutoSessao >= 30 and minutoSessao <= 59 : #sessão noturna (entre 18:30 e 18:59)
        precoInicial = 40.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.2 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao >= 19 and minutoSessao >= 0 and minutoSessao <= 59 : #sessão noturna (após as 19)
        precoInicial = 40.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.2 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao == 18 and minutoSessao >= 0 and minutoSessao <= 29 : #sessão vespertina (entre 18:00 e 18:29)
        precoInicial = 30.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.2 * precoInicial)
                ingresso = precoInicial - desconto
            
    elif horaSessao < 18 : #sessão vespertina (antes das 18)
        precoInicial = 30.00
        if estudaSimNao == "S" :
            ingresso = precoInicial / 2
        elif estudaSimNao == "N" :
            if formaPgto == "D" :
                ingresso = precoInicial
            elif formaPgto == "C" :
                desconto = (0.2 * precoInicial)
                ingresso = precoInicial - desconto

    
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))