# -*- coding: utf-8 -*- 


import requests
import json
from colorama import Fore, Style


class Imdb:

    def getFilme(self, nomefilme):
        
        uri = "http://www.omdbapi.com/?apikey=7de8e4e9"
        response = requests.get(uri + "&t=" + nomefilme)
        if response.status_code == 200:
            content = response.json()
            data = {}
            data['nome_filme'] = content['Title']
            data['ano_filme'] = content['Year']
            data['genero'] = content['Genre']
            data['language'] = content['Language']
            data['oscar'] = content['Awards']
            data['poster'] = content['Poster']
            data['bilheteria'] = content['BoxOffice']
            data['notas'] = content['Ratings']

            
        return data

    
    def getMedia(self, filme):

        filme = filme

        for chave in filme:
            if chave == 'notas':
                soma = 0
                for dici in filme.get(chave):
                    if dici.get('Source') == 'Internet Movie Database':
                        nota = dici.get('Value')[:-3]
                        nota = float(nota) * 10
                        soma = soma + int(nota)
                    elif dici.get('Source') == 'Rotten Tomatoes':
                        nota = dici.get('Value')[:-1]
                        nota = int(nota)
                        soma = soma + nota
                    elif dici.get('Source') == 'Metacritic':
                        nota = dici.get('Value')[:-4]
                        nota = int(nota)
                        soma = soma + nota
            
        return soma / 3



    def critica(self, media):
        
        if media <= 30:
            return f'{Fore.RED}Pessimo - {media:.2f}{Style.RESET_ALL}'
        elif media > 31 and media <= 50:
            return f'{Fore.MAGENTA}Ruim - {media:.2f}{Style.RESET_ALL}'
        elif media > 51 and media <= 70:
            return f'{Fore.YELLOW}Mediano - {media:.2f}{Style.RESET_ALL}'
        elif media > 71 and media <= 85:
            return f'{Fore.BLUE}Bom - {media:.2f}{Style.RESET_ALL}'
        else:
            return f'{Fore.GREEN}Muito bom - {media:.2f}{Style.RESET_ALL}'



if __name__ == '__main__':
    
    imdb = Imdb()

    nomefilme = input("Digite o nome do filme: ")
    filme = imdb.getFilme(nomefilme)

    for chave, valor in filme.items():
        print(chave + ':' +  valor) if chave != 'notas' else [print(site.get('Source') + ':' + site.get('Value')) for site in valor]
        

    print()
    print(imdb.critica(imdb.getMedia(filme)))

    
    

    