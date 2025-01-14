﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import random as rd
from datetime import time
import time
import datetime
from DISClib.DataStructures import listiterator as it
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():

    analyzer = {'eventos': None,
                'sentiments': None,
                'context_content': None,
                'user_track' : None,
                'track_ids': None,
                'danceability' : None,
                'energy': None,
                'instrumentalness': None,
                'liveness': None,
                'speechiness': None,
                'valence': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'genres': None,
                'created_at' : None,
                'created_track': None}

    analyzer['eventos'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['sentiments'] = om.newMap(omaptype='RBT', comparefunction=compareIds)
    analyzer['context_content'] = om.newMap(omaptype='RBT', comparefunction=compareIds)
    analyzer['user_track'] = om.newMap(omaptype='RBT', comparefunction= compareIds)
    analyzer['track_ids'] = om.newMap(omaptype='RBT', comparefunction= compareIds)
    analyzer['danceability'] = om.newMap(omaptype='RBT', comparefunction= compareIds)
    analyzer['energy']= om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['instrumentalness'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['liveness'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['speechiness'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['valence'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['loudness'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['tempo'] = om.newMap(omaptype='RBT') 
    analyzer['acousticness'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['genres'] = om.newMap(omaptype= 'RBT', comparefunction= compareIds)
    analyzer['created_at']= om.newMap(omaptype= 'RBT', comparefunction= compareIds)
    analyzer['created_track'] = om.newMap(omaptype='RBT', comparefunction= compareIds)
    analyzer['context_created'] = om.newMap(omaptype='RBT', comparefunction= compareIds)
    return analyzer
    

# Funciones para agregar informacion al catalogo

def addSentiments(analyzer, sentiment):

    if sentiment['vader_avg'] is not None:
        om.put(analyzer['sentiments'], sentiment['hashtag'], sentiment['vader_avg'])

def addContext(analyzer, context):

    exist = om.contains(analyzer['context_content'], context['artist_id'])
    lt.addLast(analyzer['eventos'], context)
    if exist == False:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['context_content'], context['artist_id'], newl)
    else:
        key_value = om.get(analyzer['context_content'], context['artist_id'])
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addUser(analyzer, user):

    exist = om.contains(analyzer['user_track'], user['track_id'])
    if not exist:
        key = user['track_id']
        hashtag = user['hashtag'].lower()
        if om.contains(analyzer['sentiments'], hashtag):
            pareja = om.get(analyzer['sentiments'], hashtag)
            vader = me.getValue(pareja)
            lista_valor_track_id = lt.newList()
            lt.addFirst(lista_valor_track_id, vader)
            lt.addLast(lista_valor_track_id, hashtag)
            om.put(analyzer['user_track'], key, lista_valor_track_id)
    if exist:
        key = user['track_id']
        hashtag = user['hashtag'].lower()
        if om.contains(analyzer['sentiments'], hashtag):
            pareja_lista_valor_track = om.get(analyzer['user_track'], user['track_id'])
            lista_valor_track = me.getValue(pareja_lista_valor_track)
            count = 0
            for i in range(lt.size(lista_valor_track)):
                presencia = lt.isPresent(lista_valor_track, hashtag)
            if presencia == 0:
                lt.addLast(lista_valor_track, hashtag) 


            
    
def addTrack_id(analyzer,track) : 
    exist = om.contains(analyzer['track_ids'], track['track_id'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, track)
        om.put(analyzer['track_ids'], track['track_id'], newl)
    else:
        key_value = om.get(analyzer['track_ids'], track['track_id'])
        lista = me.getValue(key_value)
        lt.addLast(lista, track)

def addDanceability(analyzer,dance) : 
    exist = om.contains(analyzer['danceability'], dance['danceability'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, dance)
        om.put(analyzer['danceability'], dance['danceability'], newl)
    else:
        key_value = om.get(analyzer['danceability'], dance['danceability'])
        lista = me.getValue(key_value)
        lt.addLast(lista, dance)

def addEnergy(analyzer,energy) : 
    exist = om.contains(analyzer['energy'], energy['energy'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, energy)
        om.put(analyzer['energy'], energy['energy'], newl)
    else:
        key_value = om.get(analyzer['energy'], energy['energy'])
        lista = me.getValue(key_value)
        lt.addLast(lista, energy)

def addInstrumentalness(analyzer, context):
    exist = om.contains(analyzer['instrumentalness'], context['instrumentalness'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['instrumentalness'], context['instrumentalness'], newl)
    else:
        key_value = om.get(analyzer['instrumentalness'], context['instrumentalness'])
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addLiveness(analyzer, context):
    exist = om.contains(analyzer['liveness'], context['liveness'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['liveness'], context['liveness'], newl)
    else:
        key_value = om.get(analyzer['liveness'], context['liveness'])
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addSpeechiness(analyzer, context):
    exist = om.contains(analyzer['speechiness'], context['speechiness'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['speechiness'], context['speechiness'], newl)
    else:
        key_value = om.get(analyzer['speechiness'], context['speechiness'])
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addValence(analyzer, context):
    exist = om.contains(analyzer['valence'], context['valence'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['valence'], context['valence'], newl)
    else:
        key_value = om.get(analyzer['valence'], context['valence'])
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addLoudness(analyzer, context):
    exist = om.contains(analyzer['loudness'], context['loudness'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['loudness'], context['loudness'], newl)
    else:
        key_value = om.get(analyzer['loudness'], context['loudness'])
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addTempo(analyzer, context):
    exist = om.contains(analyzer['tempo'], float(context['tempo']))
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['tempo'], float(context['tempo']), newl)
    else:
        key_value = om.get(analyzer['tempo'], float(context['tempo']))
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addAcousticness(analyzer, context):
    exist = om.contains(analyzer['acousticness'], context['acousticness'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['acousticness'], context['acousticness'], newl)
    else:
        key_value = om.get(analyzer['acousticness'], context['acousticness'])
        lista = me.getValue(key_value)
        lt.addLast(lista, context)

def addGenres(analyzer, name, minTemp, maxTemp):
    exist = om.contains(analyzer['genres'], name)
    if not exist:
        tupla = minTemp, maxTemp
        om.put(analyzer['genres'], name, tupla)
        
def addCreated(analyzer,created_at):
    
    fecha = datetime.datetime.strptime(created_at['created_at'], '%Y-%m-%d %H:%M:%S')
    entry = fecha.time()
    
    exist = om.contains(analyzer['created_at'], entry)
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, created_at)
        om.put(analyzer['created_at'], entry, newl)
    else:
        key_value = om.get(analyzer['created_at'], entry)
        lista = me.getValue(key_value)
        lt.addLast(lista, created_at)

def addCreatedAtContext(analyzer, context):

    fecha = datetime.datetime.strptime(context['created_at'], '%Y-%m-%d %H:%M:%S')
    entry = fecha.time()

    exist = om.contains(analyzer['context_created'], entry)
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['context_created'], entry, newl)
    else:
        key_value = om.get(analyzer['context_created'], entry)
        lista = me.getValue(key_value)
        lt.addLast(lista, context)
    
    
# Funciones para creacion de datos


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):

    if id1 == id2:
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

# Funciones de ordenamiento

def requerimiento_4_print(max_events, lista):

    print('+++++++ Req No. 4 results... ++++++ \n')
    print('Total of reproductions: ' + str(max_events) + '\n')

    num = lt.size(lista)
    num += 1

    for i in range(1,num):
        listilla = lt.getElement(lista, i)
        print('====== ' + str(listilla[0]) + ' ====== \n')
        print('For ' + str(listilla[0]) + ' the tempo is between ' + str(listilla[1]) + ' and ' + str(listilla[2]) + ' BPM \n')
        print(str(listilla[0]) + ' reproductions: ' + str(listilla[3]) + ' with ' + str(listilla[4]) + ' different artists \n')
        print('-----' + str(listilla[0]) + '------ \n')

        i = 0

        while i < 10:
            listilla_artistas = listilla[5]
            print('Artist ' + str(i + 1) + ": " + str(lt.getElement(listilla_artistas, i)))
            i += 1

def Requerimiento1(analyzer, characteristic, min_range, max_range):
    keys_in_range = om.keys(analyzer[characteristic], min_range, max_range)
    mapa = om.newMap()
    events = 0
    for i in range(lt.size(keys_in_range)):
        key = lt.getElement(keys_in_range, i)
        exist = om.contains(mapa, key)
        if not exist:
            value = om.get(analyzer[characteristic], key)
            value = me.getValue(value)
            for i in range(lt.size(value)):
                dicc = lt.getElement(value, i)
                artist = dicc['artist_id']
                om.put(mapa, artist, value)
                events += 1
    
    return events, om.size(mapa)


def Requerimiento2( analyzer,minDance,maxDance,minEnergy, maxEnergy):
    keysDance = om.keys(analyzer['danceability'],minDance,maxDance)
    keysTracks = om.keySet(analyzer['track_ids'])
    listaR = lt.newList()
    listaA = lt.newList()
    mapa_tracks = mp.newMap()
    for i in range (0,lt.size(keysDance)):
        key = lt.getElement(keysDance,i)
        keyvalue = om.get(analyzer['danceability'], key)
        value = me.getValue(keyvalue)

        for j in range (0,lt.size(value)):
            value1= lt.getElement(value,j)

            if float(value1['energy']) > float(minEnergy) and float(value1["energy"]) < float(maxEnergy) : 
                lt.addLast(listaR,value1)
                mp.put(mapa_tracks,value1['track_id'],0)
    i = 1 
    while i <= 5 :
        x = rd.randint(0,lt.size(listaR))
        elemento = lt.getElement(listaR,x)
        lt.addLast(listaA,elemento)
        i += 1

    print('Total of unique tracks in events: ' + str(mp.size(mapa_tracks)) + '\n')
    print('--- Unique track_id ---')

    for i in range(lt.size(listaA)):
        pos = lt.getElement(listaA, i)
        track = pos['track_id']
        energyf = pos['energy']
        danceabilityf = pos['danceability']
        print('Track ' + str(i + 1) + ' :' +str(track) + ' with energy of ' + str(energyf) + ' and danceability of ' + str(danceabilityf))
        i += 1


def Requerimiento3(analyzer, minIns, maxIns, minTemp, maxTemp):
    keys_in_range = om.keys(analyzer['instrumentalness'], minIns, maxIns)
    mapa = analyzer['instrumentalness']
    map_respuesta = om.newMap()
    lista_tracks = lt.newList()
    for i in range(lt.size(keys_in_range)):
        key = lt.getElement(keys_in_range, i)
        valores = om.get(mapa, key)
        valores = me.getValue(valores)
        for i in range(lt.size(valores)):
            small = lt.getElement(valores, i)
            if small['tempo'] >= minTemp and small['tempo'] <= maxTemp:
                track_id = small['track_id']
                exist = om.contains(map_respuesta, track_id)
                if not exist:
                    tupla = small['instrumentalness'], small['tempo']
                    om.put(map_respuesta, track_id, tupla)
                    lt.addLast(lista_tracks, track_id)

    print('Total of unique tracks in events: '+ str(lt.size(lista_tracks)))
    i = 0
    while i < 5:
        rand = rd.randint(0, lt.size(lista_tracks))
        track = lt.getElement(lista_tracks, rand)
        tupla_f = om.get(map_respuesta, track)
        tupla_f = me.getValue(tupla_f)
        print('Track ' + str(i + 1) + ' :' +str(track) + ' with instrumentalness of ' + str(tupla_f[0]) + ' and tempo of ' + str(tupla_f[1]))
        i += 1

def Requerimiento4(analyzer, str_generos):

    generos_lower = str_generos.lower()
    lista_generos = generos_lower.split(',')
    final = lt.newList()
    for i in range(len(lista_generos)):
        lista_genero = lt.newList()
        mapa = analyzer['genres']
        busqueda_map = om.get(mapa, lista_generos[i])
        tupla = me.getValue(busqueda_map)
        name = me.getKey(busqueda_map)
        minTemp = int(tupla[0])
        maxTemp = int(tupla[1])
        keys_in_range = om.keys(analyzer['tempo'], minTemp, maxTemp)
        events_parciales = lt.size(keys_in_range)

        lt.addLast(lista_genero, events_parciales)

        mp_artistas = om.newMap()
        lt_artistas = lt.newList()

        for i in range(lt.size(keys_in_range)):
            key = float(lt.getElement(keys_in_range, i))
            mapa_tempo = analyzer['tempo']
            valores = om.get(mapa_tempo, key)
            valores = me.getValue(valores)

            for i in range(lt.size(valores)):
                valor = lt.getElement(valores, i)
                exist = om.contains(mp_artistas, valor['artist_id'])

                if not exist:
                    artist_id = valor['artist_id']
                    om.put(mp_artistas, artist_id, valor)
                    while lt.size(lt_artistas) <= 10:
                        lt.addLast(lt_artistas, artist_id)

        artistas_parciales = om.size(mp_artistas)

        lt_final_genero = [name, minTemp, maxTemp, events_parciales, artistas_parciales, lt_artistas]
        lt.addLast(final, lt_final_genero) 

    max_eventos = 0

    for i in range(lt.size(final)):
        listilla = lt.getElement(final, i)
        max_eventos += int(listilla[3])

    requerimiento_4_print(max_eventos, final)

def Requerimiento5(analyzer,minHora,maxHora):
    value = om.values(analyzer['created_at'],minHora,maxHora)
    print(value)
    iterador = it.newIterator(value)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        iterador2 = it.newIterator(elemento)
        while it.hasNext(iterador2):
            elemento2 = it.next(iterador2)
            print(elemento2)

def Requerimiento5maps(analyzer, minHora, maxHora):
    
    valores = om.keys(analyzer['context_created'], minHora, maxHora)
    generos = om.keySet(analyzer['genres'])

    respuesta = om.newMap()

    for i in range(lt.size(valores)):
        key_value = lt.getElement(valores, i)
        info_context_pareja = om.get(analyzer['context_created'], key_value)
        context = me.getValue(info_context_pareja)
        for i in range(lt.size(context)):
            info_context = lt.getElement(context, i)
        for i in range(lt.size(generos)):
            key_genero = lt.getElement(generos, i)
            info_genero_pareja = om.get(analyzer['genres'], key_genero)
            info_genero = me.getValue(info_genero_pareja)
            minTemp = float(info_genero[0])
            maxTemp = float(info_genero[1])
            if float(info_context['tempo']) >= minTemp and float(info_context['tempo']) <= maxTemp:

                contains = om.contains(respuesta, key_genero)
                if not contains:
                    track_id = info_context['track_id']

                    #extraccion info relevante

                    llave_valor_info_adicional = om.get(analyzer['user_track'], track_id)
                    info_adicional = me.getValue(llave_valor_info_adicional)
                    vader = lt.getElement(info_adicional, 1)
                    hashtags = lt.size(info_adicional) - 1

                    lista_genero = lt.newList()

                    track = {}

                    track['track_id'] = track_id
                    track['vader'] = vader
                    track['num_hashtags'] = hashtags

                    lt.addLast(lista_genero, track)

                    om.put(respuesta, key_genero, lista_genero)
                
                if contains:
                    track_id = info_context['track_id']

                    llave_valor_info_adicional = om.get(analyzer['user_track'], track_id)
                    info_adicional = me.getValue(llave_valor_info_adicional)
                    vader = lt.getElement(info_adicional, 1)
                    hashtags = lt.size(info_adicional) - 1

                    pareja_lista_genero = om.get(respuesta, key_genero)
                    lista_genero = me.getValue(pareja_lista_genero)

                    track = {}

                    track['track_id'] = track_id
                    track['vader'] = vader
                    track['num_hashtags'] = hashtags

                    lt.addLast(lista_genero, track)
    
    return respuesta





        

    