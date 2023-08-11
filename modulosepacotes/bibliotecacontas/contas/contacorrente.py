from typing import List, Dict
from modulosepacotes.bibliotecacontas.titulares.titular import Titular

# Eu utilizei no extrato um dicionário, mas poderia ser a classe Movimentacao abaixo
# class Movimentacao:
#     self._tipo: str # e pra entrada, s pra saída
#     self._valor: float 

class ContaCorrente:
    def __init__(self, titular: Titular, agencia: str, conta: str):
        self._titular: Titular = titular
        self._agencia: str = agencia
        self._conta: str = conta
        self._saldo: float = 0.0
        self._extrato: List[Dict[str, str]] = []

    @property
    def titular(self) -> Titular:
        return self._titular

    @property
    def agencia(self) -> str:
        return self._agencia
    
    @property
    def conta(self) -> str:
        return self._conta
    
    @property
    def saldo(self) -> float:
        return self._saldo

    def _adicionar_extrato(self, tipo: str, valor: float):
        valor_formatado = '{:.2f}'.format(valor)
        self._extrato.append({'key': tipo.upper(), 'value': valor_formatado})
        # if tipo.upper() == 'E':
        #     self._extrato.append({'key': 'E', 'value': valor_formatado})
        # else:            
        #     self._extrato.append({'key': tipo.upper(), 'value': valor_formatado})

    def _msg_resposta(self, sucesso: bool, nome_operacao: str) -> None:
        if sucesso:
            print(f'Operação realizada com sucesso. Operação: {nome_operacao}')
        else:
            print(f'Falha ao realizar operação. Operação: {nome_operacao}')

    def _saidas(self, valor: float, nome_operacao: str) -> bool:
        if self._saldo >= valor:
            self._saldo -= valor
            self._adicionar_extrato(tipo='s', valor=valor)
            self._msg_resposta(sucesso=True, nome_operacao=nome_operacao)
            return True
        else:
            self._msg_resposta(sucesso=False, nome_operacao=nome_operacao)
            return False

    def deposito(self, valor: float) -> None:
        # retornar somatório do saldo pra ver que foi depositado
        # booleano pra saber se deu certo
        # print da confirmação. sem retornar nada ou retornar o booleano, ou o saldo, etc
        # log da data, do valor, do saldo, etc
        nome_operacao = 'Deposito'
        if valor > 0.0:
            self._saldo += valor
            self._adicionar_extrato(tipo='e', valor=valor)
            self._msg_resposta(sucesso=True, nome_operacao=nome_operacao)
        else:
            self._msg_resposta(sucesso=False, nome_operacao=nome_operacao)

    def pagamento(self, valor: float) -> None:
        self._saidas(valor=valor, nome_operacao='Pagamento')

    def saque(self, valor: float) -> None:
        self._saidas(valor=valor, nome_operacao='Saque')

    def transferencia(self, valor: float, conta_destino: ContaCorrente) -> None:
        nome_operacao = 'Transferencia'
        if self._saldo >= valor:
            self._saldo -= valor
            self._adicionar_extrato(tipo='s', valor=valor)
            conta_destino.deposito(valor)
            self._msg_resposta(sucesso=True, nome_operacao=nome_operacao)
        else:
            self._msg_resposta(sucesso=False, nome_operacao=nome_operacao)
    
    def transferencia_usando_saida(self, valor: float, conta_destino: ContaCorrente) -> None:
        # para funcionar, tivemos que refatorar a saída e retornar se teve sucesso ou não
        teve_sucesso = self._saidas(valor=valor, nome_operacao='Transferencia')
        if teve_sucesso:
            conta_destino.deposito(valor)

    def extrato(self):
        print(f'Agencia: {self._agencia}')
        print(f'Conta: {self._conta}')
        print(f'Titular: {self.titular.nome_titular}')
        print(f'CPF do titular: {self._titular.cpf}')
        print('Saldo: R$', '{:.2f}'.format(self._saldo), sep=' ')
        for mov in self._extrato:
            print(f'\t{mov["key"]}: R$ {mov["value"]}')
        