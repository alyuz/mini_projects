v = int(input())  # Valor da hora de trabalho
d = int(input())  # 0 a 7 - Dias da semana trabalhados
horasSemana = 0  # Horas totais da semana
qtdHorasExtrasDia = 0  # Quantidade de horas extras diárias

for i in range(1, d + 1):
    horasDia = 0  # Horas totais de cada dia
    periodos = int(input())
    for j in range(1, periodos + 1):
        horaInicio = int(input())
        horaFim = int(input())
        duracaoPeriodo = horaFim - horaInicio
        horasDia += duracaoPeriodo  # O tempo do período é adicionado às horas do dia

    if horasDia > 8:
        horasExtrasDia = horasDia - 8
        qtdHorasExtrasDia += horasExtrasDia  # Somando a quantidade de horas de todos os dias

    horasSemana += horasDia  # As horas do dia são adicionadas ao tempo total de horas da semana

horasExtrasSemana = 0
if horasSemana > 44:
    horasExtrasSemana = horasSemana - 44  # Calcular horas extras semanais


if qtdHorasExtrasDia > 0:
    if horasExtrasSemana > 0:
        totalExtraSemana = horasExtrasSemana - qtdHorasExtrasDia
        if totalExtraSemana > 0:
            valorHoraExtraDia = qtdHorasExtrasDia * ((v * 0.5))
            valorHoraExtraSemana = totalExtraSemana * ((v * 0.5))
            valorFinal = ((horasSemana * v) + valorHoraExtraSemana) + valorHoraExtraDia

            print(f"Horas trabalhadas: {horasSemana}")
            print(f"Horas extras: {horasExtrasSemana}")
            print(f"Valor devido: R$ {valorFinal:.2f}")

        else:
            valorHoraExtraDia = qtdHorasExtrasDia * ((v * 0.5))
            valorFinal = (horasSemana * v) + valorHoraExtraDia

            print(f"Horas trabalhadas: {horasSemana}")
            print(f"Horas extras: {qtdHorasExtrasDia}")
            print(f"Valor devido: R$ {valorFinal:.2f}")
    else:
        valorHoraExtraDia = qtdHorasExtrasDia * ((v * 0.5))
        valorFinal = (horasSemana * v) + valorHoraExtraDia

        print(f"Horas trabalhadas: {horasSemana}")
        print(f"Horas extras: {qtdHorasExtrasDia}")
        print(f"Valor devido: R$ {valorFinal:.2f}")

else:
    if horasExtrasSemana > 0:
        valorHoraExtraSemana = horasExtrasSemana * ((v * 0.5))
        valorFinal = (horasSemana * v) + valorHoraExtraSemana

        print(f"Horas trabalhadas: {horasSemana}")
        print(f"Horas extras: {horasExtrasSemana}")
        print(f"Valor devido: R$ {valorFinal:.2f}")

    else:
        valorFinal = horasSemana * v
        print(f"Horas trabalhadas: {horasSemana}")
        print(f"Horas extras: 0")
        print(f"Valor devido: R$ {valorFinal:.2f}")