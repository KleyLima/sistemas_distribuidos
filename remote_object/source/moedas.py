# -*- coding: utf-8 -*-

import Pyro5.api

@Pyro5.api.expose
class Moedas:
    """ Classe que representa as moedas, seus valores e relação na sua distribuição dado um valor."""

    @classmethod
    def __init__(cls):
        """
        Método que inicializa os atributos da classe, define as moedas disponiveis para distribuição e um 
        gerador de moedas, util na recursividade da funcão de transformação.
        """
        cls.vlr = 0
        cls.moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
        cls.gen = (coin for coin in cls.moedas)
        cls.lst = []
        cls.pretty = []

    @classmethod
    def valor_moedas(cls):
        """
        Distribui o valor passado para conversão na configuração de moedas presente em cls.moedas, usa o cls.gen
        para iterar sobre os valores a cada chamada recursiva da função. Retorna um dicionário das moedas
        utilizadas na tela.
        """
        try:
            coin = next(cls.gen)
            qtd = cls.vlr // coin
            cls.lst.append((coin, int(qtd))) if qtd != 0 else None
            cls.vlr %= coin
            cls.vlr = round(cls.vlr, 2)
            cls.valor_moedas()
        except StopIteration:
            return cls.lst
        finally:
            return cls.lst if cls.lst else False

    @classmethod
    def check(cls, vlr):
        try:
            vlr = float(vlr)
            return vlr if vlr > 0 else False
        except ValueError:
            return False

    @classmethod
    def formater(cls):
        cls.pretty = [f"{qtd} Moedas de R${coin}" if qtd > 1 else f"{qtd} Moeda de R${coin}" for coin, qtd in cls.lst]

    @classmethod
    def make_it_happen(cls, vlr):
        cls.vlr = float(vlr)
        cls.valor_moedas()
        cls.formater()       
        [print(x) for x in cls.pretty] if cls.pretty else None
        return cls.pretty


if __name__ == '__main__':
    #Moedas(float(input("Digite o valor (Não esqueça das moedas)")) if len(argv) == 1 else argv[1]).make_it_happen()
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(Moedas)
    ns.register("example.greeting", uri)

    print("Ready.")
    daemon.requestLoop()
    print('Hello') 

