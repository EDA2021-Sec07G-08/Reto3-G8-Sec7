"""
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
                'acousticness': None}

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
    analyzer['tempo'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 
    analyzer['acousticness'] = om.newMap(omaptype='RBT', comparefunction= compareIds) 

    return analyzer
    

# Funciones para agregar informacion al catalogo

def addSentiments(analyzer, sentiment):

    om.put(analyzer['sentiments'], sentiment['hashtag'], sentiment)

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
        newl = lt.newList()
        lt.addLast(newl, user)
        om.put(analyzer['user_track'], user['track_id'], newl)
    else:
        key_value = om.get(analyzer['user_track'], user['track_id'])
        lista = me.getValue(key_value)
        lt.addLast(lista, user)
    
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
    exist = om.contains(analyzer['tempo'], context['tempo'])
    if not exist:
        newl = lt.newList()
        lt.addLast(newl, context)
        om.put(analyzer['tempo'], context['tempo'], newl)
    else:
        key_value = om.get(analyzer['tempo'], context['tempo'])
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

    return (mp.size(mapa_tracks), listaA)

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

def Requerimiento5 ( )