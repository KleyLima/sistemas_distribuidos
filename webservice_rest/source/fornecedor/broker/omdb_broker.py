# -*- coding: utf-8 -*-

import requests


class OmdbBroker(object):
    url = "http://www.omdbapi.com/?apikey=7de8e4e9"

    def __init__(self, search_by, mode='s'):
        self.mode = mode
        self.response = None
        self.search_by = search_by

    def get_infos(self):
        """
        Busca pelo titulo do filme na API
        :return: JSON com as infos do Filme
        """

        response = requests.get(self.__class__.url + f"&{self.mode}=" + self.search_by)

        if response.status_code == 200:
            content = response.json()

            self.response = content

    def unwrap(self):
        if self.response and self.response.get('Response') == 'True':
            if self.mode == 's':
                self.response = self.response.get('Search')
