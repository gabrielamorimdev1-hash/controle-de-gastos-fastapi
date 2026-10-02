def calculo_total_gasto(gastos):
    total = 0

    for gasto in gastos:
        total += gasto["valor"]
        
    return total