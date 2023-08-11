from datetime import date


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