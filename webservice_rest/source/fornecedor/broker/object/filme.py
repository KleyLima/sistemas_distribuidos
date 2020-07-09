# -*- coding: utf-8 -*-

class Filme:
    def __init__(self, nome=None, ano=None, genero=None, linguagem=None, premios=None, poster=None, bilheteria=None,
                 notas=None):
        self.nome = nome
        self.ano = ano
        self.genero = genero
        self.linguagem = linguagem
        self.premios = premios
        self.poster = poster
        self.bilheteria = bilheteria
        self.notas = notas

    def mapper(self, filme):
        return Filme(nome=filme.get('Title'), ano=filme.get('Year'), genero=filme.get('Genre'),
                     linguagem=filme.get('Language'), premios=filme.get('Awards'), poster=filme.get('Poster'),
                     bilheteria=filme.get('BoxOffice'), notas=filme.get('Ratings')) if filme else None
