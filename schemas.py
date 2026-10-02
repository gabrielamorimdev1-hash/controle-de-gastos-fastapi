from pydantic import BaseModel

class GastoEntrada(BaseModel):
    descricao: str
    valor: float
    categoria: str