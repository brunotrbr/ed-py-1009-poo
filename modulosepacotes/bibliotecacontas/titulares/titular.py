from datetime import date

class Titular:
    def __init__(self, nome: str, cpf: str, dt_nasc: date):
        self._nome: str = nome
        self._cpf: str = cpf
        self._dt_nasc: date = dt_nasc

    @property
    def nome_titular(self) -> str:
        return self._nome
    
    @nome_titular.setter
    def nome_titular(self, nome: str) -> None:
        self._nome = nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def data_nascimento(self) -> date:
        return self._dt_nasc