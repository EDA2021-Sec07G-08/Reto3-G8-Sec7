"""
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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

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
        pass

    else:
        sys.exit(0)
sys.exit(0)
