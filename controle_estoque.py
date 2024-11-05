valorEstoque = 0
qtdVendas = 0

def venda(valor, qtd):
    return valor + (-qtd)

def compra(valor, qtd):
    return valor + qtd

modificacao = int(input()) # Quantidade que está sendo alterada (pode ser adicionando ou subtraindo)

while modificacao != 0:

    while modificacao < 0: # É venda
        resultadoVenda = venda(valorEstoque, -modificacao) # Faz a conta com base na função, a modificação tem que ser especificada como negativa
        if resultadoVenda < 0: 
            print(f"Quantidade indisponivel para a venda de {modificacao * -1} unidades.")
            break
        else:
            valorEstoque = resultadoVenda
            qtdVendas += 1  
            break

    while modificacao > 0: # É compra
        resultadoCompra = compra(valorEstoque, +modificacao)
        valorEstoque = resultadoCompra
        break

    modificacao = int(input()) 

print(f"Quantidade de vendas realizadas: {qtdVendas}")
print(f"Quantidade em estoque: {valorEstoque}")