# -*- coding: utf-8 -*-

class Filme:
        
    @classmethod
    def __init__(cls, nome=None, ano=None, genero=None, linguagem=None, premios=None, poster=None, bilheteria=None, notas=None):
        cls.nome = nome
        cls.ano = ano
        cls.genero = genero
        cls.linguagem = linguagem
        cls.premios = premios
        cls.bilheteria = bilheteria
        cls.notas = notas

    @classmethod
    def mapper(cls, data):
        return [Filme(nome=filme.get('Title'), ano=filme.get('Year'), genero=filme.get('Genre'),
                linguagem=filme.get('Language'), premios=filme.get('Awards'), poster=filme.get('Poster'),
                bilheteria=filme.get('BoxOffice'), notas=filme.get('Ratings')) for filme in data.get('Search')
                ] if data.get('Search') else None

