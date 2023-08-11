from datetime import date
import sys
import os

module_path = os.path.abspath('modulosepacotes')
sys.path.append(module_path)

from modulosepacotes.bibliotecacontas.titulares.titular import Titular


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

if __name__ == "__main__":
    run()