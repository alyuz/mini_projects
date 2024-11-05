d1 = int(input())
v1 = int(input())
t = int(input())
d2 = int(input())
v2 = int(input())

# Cálculo de tempo = distância / velocidade

tempo1 = d1 / v1
tempo2 = d2 / v2

# O resultado será dado em horas e por isso será convertido para dias dividindo-o por 24
dias1 = tempo1 / 24
dias2 = tempo2 / 24

# Soma o valor de dias a mais pelo espaço de tempo entre os lançamentos no resultado final para obtenção do tempo total da Blue Origin.
tempoTotal2 = dias2 + t

spaceX = tempoTotal2 > dias1 #se o tempo total da Blue Origin (2) for maior do que o da SpaceX (1) significa 
# que a SpaceX chegou primeiro e o resultado é True.
# Do contrário, caso o resultado seja menor ou igual ela não chegou primeiro e portanto o resultado é False.

# blueOrigin = tempoTotal2 < dias1 - Não será necessário pois o resultado é calculado de acordo 
# com a chegada da SpaceX sendo 1 para caso chegue primeiro e 0 para caso chegue depois (o que 
# significa que a Blue Origin chegou primeiro)

if spaceX == 1:
    print("True")
elif spaceX == 0:
    print("False")