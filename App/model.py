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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():

    analyzer = {'eventos': None,
                'sentiments': None}

    analyzer['eventos'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['sentiments'] = om.newMap(omaptype='RBT', comparefunction=compareIds)
    analyzer['context_content'] = om.newMap(omaptype='RBT', comparefunction=compareIds)
    analyzer['user_track'] = om.newMap(omaptype='RBT', comparefunction= compareIds)

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
