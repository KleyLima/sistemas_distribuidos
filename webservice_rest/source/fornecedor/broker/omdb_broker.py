# -*- coding: utf-8 -*-

import requests


class OmdbBroker:
    


    @classmethod
    def get_infos(cls, nome_filme):
        """
        Busca pelo titulo do filme na API

        :param nome_filme: Nome do filme a ser buscado
        :return: JSON com as infos do Filme
        """
        
        data = requests.get(url + "&t=" + nomefilme)

        if response.status_code == 200:
            content = response.json()

            # TODO: Keep data fetching

