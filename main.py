from fastapi import FastAPI
from schemas import GastoEntrada
from calculo_Total_gasto import calculo_total_gasto

app = FastAPI()

# banco de dados temporario
gastos = []

#rota para listar todos os gastos
@app.get("/gastos")
def get_gastos():
    return gastos

@app.post("/gastos")
def create_gasto(gasto: GastoEntrada):
    novo_gasto = {
    "descricao": gasto.descricao,
    "valor": gasto.valor,
    "categoria": gasto.categoria
    }

    gastos.append(novo_gasto)

    return novo_gasto

#rota para calcular o total de gastos

@app.get("/gastos/total")
def get_total_gastos():
    total = calculo_total_gasto(gastos)
    return {"total_gastos": total}