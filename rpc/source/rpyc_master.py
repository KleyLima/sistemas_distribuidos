# -*- coding: utf-8 -*-

from functools import reduce
import rpyc


def calculos(numbers):
    """
    Realiza a soma, média e multiplicação e elementos e uma lista.
    :param numbers: Lista de Inteiros
    :return: Tupla contendo (soma dos elementos, média de valores, multiplicação de todos elementos)
    """

    soma = sum(numbers)
    print("Soma Calculada")
    media = soma/len(numbers)
    print("Média Calculada")
    mult = reduce(lambda k, l: k*l, numbers)
    print("Multiplicação Calculada")

    return soma, media, mult


def connect():
    """
    Realiza a conexão com o slave na porta 18812
    """
    return rpyc.classic.connect("localhost")

def leitura_valores():
    """
    Realiza a leitura de valores do stdin e os retorna em uma lista.
    """
    return [int(x) for x in input('Insira a lista de valores: ').split()]

def realiza_imports(conn):
    """
    Realiza os imports necessários para execução da funcão no Slave.
    :param conn: objeto de conexão para enviar os comandos de import.
    """
    used = ["from functools import reduce", "import rpyc"]
    [conn.execute(use) for use in used]


if __name__ == '__main__':
    conn = connect()
    numbers = leitura_valores()
    realiza_imports(conn)
    funcao = conn.teleport(calculos)

    results = funcao(numbers)
    print(results)

