from datetime import date
import sys
import os

module_path = os.path.abspath('modulosepacotes')
sys.path.append(module_path)

from modulosepacotes.bibliotecacontas.titulares.titular import Titular
from modulosepacotes.bibliotecacontas.contas.contacorrente import ContaCorrente


def run():
    dt_nasc = date(year=1991, month=8, day=6)
    t1 = Titular('Pedro', 'Engenheiro de dados', dt_nasc)
    print(t1.nome_titular)
    print(t1.cpf)
    print(t1.data_nascimento)

    print(t1._nome)
    print(t1._cpf)
    print(t1._dt_nasc)

    t1.nome_titular = 'Marcos'
    print(t1.nome_titular)
    print(t1._nome)

    dt_nasc = date(year=1991, month=8, day=6)
    t1 = Titular('Pedro', 'Engenheiro de dados', dt_nasc)

    cc1 = ContaCorrente(t1, '001', 'c101')
    cc1.deposito(180.50) # nesse ponto eu estou informando que o depósito vai ser feito para a cc1
    print(cc1.saldo)
    cc1.saque(100)
    print(cc1.saldo)
    cc1.pagamento(80.0)
    print(cc1.saldo)

    cc1.extrato()

if __name__ == "__main__":
    run()