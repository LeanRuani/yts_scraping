#Enunciado:
#-Obtener todos los contenidos de la plataforma
#-Obtener la metadata de cada contenido: título, año, sinopsis, enlace web, géneros
#-Obtener los comentarios de cada contenido
#-Guardar la información obtenida en una base de datos, en archivo .json o .csv automáticamente
#*PLUS: Cantidad de likes
#*PLUS: Si es posible obtener más información/metadata por cada contenido

#Sitio a realizar el scraping: https://yts.mx/


import requests
from os import system
import pandas as pd
import json

def obtener_contenido():
    listado = pd.DataFrame()
    #hay 1971 paginas
    pagina = int(input("Ingrese el numero de paginas a recorrer entre el 2 al 1971: "))
    if  pagina >= 2 and pagina <= 1971:
        system('cls')
        for url in range(1, pagina):
            system('cls')
            print("Pagina {}".format(url))
            url = 'https://yts.mx/api/v2/list_movies.json?page={}'.format(url)
            yts = requests.get(url)
            peliculas = json.loads(yts.content)
            for number in range(0, 20):
                    listado = listado.append({
                        'id': peliculas['data']['movies'][number]['id'],
                        'titulo': peliculas['data']['movies'][number]['title_english'],
                    }, ignore_index=True)
        listado.to_json('detalle_pelicula.json', orient = 'records')
        system('cls')
        print("Listado de peliculas obtenido y guardado en archivo detalle_pelicula.json")
    else:
        system('cls')
        print("El numero de paginas a recorrer no es valido")

def obtener_detalle():
    id_pelicula = int(input("Ingrese el ID de la pelicula: "))
    url = 'https://yts.mx/api/v2/movie_details.json?movie_id={}'.format(id_pelicula)
    yts = requests.get(url)
    pelicula = json.loads(yts.content)
    listado_detalles = pd.DataFrame()
    if pelicula['data']['movie']['id'] != 0:
        listado_detalles = listado_detalles.append({
            'id': pelicula['data']['movie']['id'],
            'titulo': pelicula['data']['movie']['title_english'],
            'año': pelicula['data']['movie']['year'],
            'sinopsis': pelicula['data']['movie']['description_intro'],
            'url': pelicula['data']['movie']['url'],
            'generos': pelicula['data']['movie']['genres'],
            'mas_detalles': { 
                'like_count': pelicula['data']['movie']['like_count'],
                'download_count': pelicula['data']['movie']['download_count'],
                'rating': pelicula['data']['movie']['rating'],
                'language': pelicula['data']['movie']['language'],
                'torrents': pelicula['data']['movie']['torrents'],
                }
            }, ignore_index=True)
        listado_detalles.to_json('detalle_pelicula.json', orient = 'records')
        print("Detalle de la pelicula obtenido y guardado en archivo detalle_pelicula.json")
    else:
        print("El ID de la pelicula no es valido")

while True:
    system('cls')
    print ("1. Obtener todos los contenidos de la plataforma")
    print ("2. Metadata segun ID del contenido")
    print ("3. Salir")
    
    opcion = int (input("Opción: "))
    if opcion == 1:
       obtener_contenido()
       break
    elif opcion == 2:
        obtener_detalle()
        break
    elif opcion == 3:
        break
    else:
        system('cls')
        print ("Introduce un numero entre 1 y 3")
        print ("-------------------------------")
print ("Fin")