# -*- coding: utf-8 -*-

from webservice_rest.source.fornecedor.business.omdb_business import OmdbBusiness


class FilmesService:

    @classmethod
    def busca_varios(cls, search):
        """
        Realizar a busca de varios filmes, com base em uma string
        :param search: String para buscar o filme pelo titulo.
        """

        films = OmdbBusiness.search(search_by=search)
        films = OmdbBusiness.busca_detalhada(from_api=films)
        return films

    @classmethod
    def busca_one(cls, search):
        filmes = OmdbBusiness.busca_one(search_by=search)
        return filmes

if __name__ == '__main__':

    na = FilmesService()
    print(na.busca_one('Frozen'))
