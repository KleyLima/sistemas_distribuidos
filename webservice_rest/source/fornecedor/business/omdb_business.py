# -*- coding: utf-8 -*-

from webservice_rest.source.fornecedor.broker.omdb_broker import OmdbBroker


class OmdbBusiness:

    @classmethod
    def search(cls, search_by, unit=False):
        return OmdbBusiness.busca_filmes(search_by=search_by) if not unit else OmdbBusiness.busca_filmes(search_by, 't')

    @classmethod
    def busca_filmes(cls, search_by, mode='s'):
        busca = OmdbBroker(search_by=search_by, mode=mode)
        busca.get_infos()
        busca.unwrap()
        return busca.response

    @classmethod
    def busca_one(cls, search_by, mode='t'):
        busca= OmdbBroker(search_by=search_by, mode=mode)
        busca.get_infos()
        return busca.response

    @classmethod
    def busca_detalhada(cls, from_api):
        return [OmdbBusiness.search(search_by=filme.get('Title'), unit=True) for filme in from_api]
