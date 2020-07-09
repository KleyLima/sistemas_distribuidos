# -*- coding: utf-8 -*-

from webservice_rest.source.fornecedor.broker.omdb_broker import OmdbBroker
from webservice_rest.source.fornecedor.broker.object.filme import Filme

class FilmesService:

    @classmethod
    def busca_varios(cls, search):
        """
        Realizar a busca de varios filmes, com base em uma string
        :param search: String para buscar o filme pelo titulo.
        """
        detail_film = []

        films = OmdbBroker().get_infos(nome_filme=search)
        films = OmdbBroker().unwrap(content=films)
        
        if films:
            # TODO: Iterar sobre a lista de resultados, buscando cada um com '&t=' na APi de filmes
            for film in films:
                detail = OmdbBroker('t').get_infos(film.get('Title'))
                detail = OmdbBroker('t').unwrap(content=detail)

                detail_film.append(Filme.mapper(detail))
                return detail_film


if __name__ == '__main__':
    na=FilmesService.busca_varios('Star Wars')
    [print(x) for x in na]
