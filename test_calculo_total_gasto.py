from calculo_Total_gasto import calculo_total_gasto


def test_calculo_total_gasto():
    gastos = [
        {"descricao": "internet", "valor": 100.0, "categoria": "casa"},
        {"descricao": "almoço", "valor": 25.0, "categoria": "trabalho"},
    ]

    total = calculo_total_gasto(gastos)

    assert total == 125.00