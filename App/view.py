﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf
from datetime import time
import time
import datetime


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requerimiento 4")
    print("6- Requerimiento 5")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        analyzer = controller.initCatalog()
        analyzer = controller.loadData(analyzer)
        num_eventos = lt.size(analyzer['eventos'])
        print('Se han cargado '+ str(num_eventos) + ' eventos!')
        artistaslt = om.keySet(analyzer['context_content'])
        num_artistas = lt.size(artistaslt)
        print('Se han cargado ' + str(num_artistas) + ' artistas!') 
        pistaslt = om.keySet(analyzer['user_track'])
        num_pistas = lt.size(pistaslt)
        print('Se han cargado ' + str(num_pistas) + ' pistas!')
        for i in range(0, 5):
            print(lt.getElement(analyzer['eventos'], i))
        j = 0
        while j <= 4:
            print(lt.getElement(analyzer['eventos'], int(num_eventos) - j))
            j += 1
    elif int(inputs[0]) == 2:
        characteristic = input('Ingrese la caracteristica de contenido: ')
        min_range = input('Ingrese el rango minimo: ')
        max_range = input('Ingrese el rango maximo: ')
        ans = controller.Requerimiento1(analyzer, characteristic, min_range, max_range)
        print('Total of reproductions: ' + str(ans[0]) + ' Total of unique artists: ' + str(ans[1]))

    elif int(inputs[0]) == 3:
        minEnerg = input('Digite la cantidad minima del Energy ')
        maxEnerg = input('Digite la cantidad máxima del Energy ')
        minDancing = input('Digite la cantidad minima del Danceability ')
        maxDancing = input('Digite la cantidad minima del Danceability ') 
        print ('Energy is betweeen '+minEnerg+' and '+maxEnerg)
        print ('Energy is betweeen '+minDancing+' and '+maxDancing)
        controller.Requerimiento2(analyzer,minDancing,maxDancing,minEnerg,maxEnerg)
    elif int(inputs[0]) == 4:
        minIns = input('Ingrese la cantidad minima de Instrumentalness: ')
        maxIns = input('Ingrese la cantidad maxima de Instrumentalness: ')
        minTemp = input('Ingrese la cantidad minima de Tempo: ')
        maxTemp = input('Ingrese la cantidad maxima de Tempo: ')
        controller.Requerimiento3(analyzer, minIns, maxIns, minTemp, maxTemp)
    elif int(inputs[0]) == 5:
        eleccion = input('¿Desea ingresar un nuevo genero musical (1) o hacer una busqueda por genero (2)?')
        if eleccion == '1':
            nombre = input('Ingrese el nombre del genero musical: ')
            minTemp = input('Ingrese el valor minimo del tempo: ')
            maxTemp = input('Ingrese el valor maximo del tempo: ')
            controller.addGenre(analyzer, nombre, minTemp, maxTemp)
        else:
            str_generos = input('Ingrese los generos que desea conocer separados por coma: ')
            controller.Requerimiento4(analyzer, str_generos)
    elif int(inputs[0]) == 6:
        minHor = input('Ingrese la hora mínima: ')
        maxHor = input('Ingrese la hora maxima: ')

        minHor = minHor.split(":")
        minHor= datetime.time(int(minHor[0]),int(minHor[1]))
        maxHor = maxHor.split(":")
        maxHor= datetime.time(int(maxHor[0]),int(maxHor[1]))
        

        print(controller.Requerimiento5maps(analyzer, minHor, maxHor))

    else:
        sys.exit(0)
sys.exit(0)
