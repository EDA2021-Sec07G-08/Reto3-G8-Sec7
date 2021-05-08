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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():

    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer):

    loadSentiments(analyzer, 'subsamples-small/sentiment_values.csv')
    loadContext(analyzer, 'subsamples-small/context_content_features-small.csv')
    loadUser(analyzer, 'subsamples-small/user_track_hashtag_timestamp-small.csv')
    loadGenres(analyzer)

    return analyzer

def loadSentiments(analyzer, sentimentsfile):

    sentimentsfile = cf.data_dir + sentimentsfile
    input_file = csv.DictReader(open(sentimentsfile, encoding="utf-8"), delimiter = ",")

    for sentiment in input_file:
        model.addSentiments(analyzer, sentiment)
    return analyzer

def loadContext(analyzer, contextfile):

    contextfile = cf.data_dir + contextfile
    input_file = csv.DictReader(open(contextfile, encoding="utf-8"), delimiter = ",")

    for context in input_file:
        model.addContext(analyzer, context)
        model.addTrack_id(analyzer,context)
        model.addDanceability(analyzer,context)
        model.addEnergy(analyzer,context)
        model.addInstrumentalness(analyzer, context)
        model.addLiveness(analyzer, context)
        model.addSpeechiness(analyzer, context)
        model.addValence(analyzer, context)
        model.addLoudness(analyzer, context)
        model.addTempo(analyzer, context)
        model.addAcousticness(analyzer, context)
    return analyzer

def loadUser(analyzer, userfile):

    userfile = cf.data_dir + userfile
    input_file = csv.DictReader(open(userfile, encoding='utf-8'), delimiter = ",")

    for user in input_file:
        model.addUser(analyzer, user)
    return analyzer

def loadGenres(analyzer):
    names = ['reggae', 'down_tempo', 'chill-out', 'hip-hop', 'jazz and funk', 'pop', 'r&b', 'rock', 'metal']
    tempos = [[60,90], [70,100], [90,120], [85,115], [120,125], [100,130], [60,80], [110,140], [100,160]]
    
    for i in range(len(names)):
        name = names[i]
        minTemp = tempos[i][0]
        maxTemp = tempos[i][1]
        model.addGenres(analyzer, name, minTemp, maxTemp)

def addGenre(analyzer, name, minTemp, maxTemp):
    return model.addGenre(analyzer, name, minTemp, maxTemp)
 
def Requerimiento1(analyzer, characteristic, min_range, max_range):
    return model.Requerimiento1(analyzer, characteristic, min_range, max_range)

def Requerimiento2 (analyzer,minDance,maxDance,minEnergy, maxEnergy): 
    return model.Requerimiento2(analyzer,minDance,maxDance,minEnergy, maxEnergy)

def Requerimiento3(analyzer, minIns, maxIns, minTemp, maxTemp):
    return model.Requerimiento3(analyzer, minIns, maxIns, minTemp, maxTemp)

def Requerimiento4(analyzer, str_generos):
    return model.Requerimiento4(analyzer, str_generos)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
