"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv 
import sys
lista=[]

with open('data.csv') as data:
    reader = csv.reader(data,delimiter='\t')
    lista = list(reader)

    #CREAMOS UNA LISTA CUYOS ELEMENTOS SEAN LAS COLUMNAS DEL CSV        
    columna1=[]
    columna2=[]
    columna3=[]
    columna4=[]
    columna5=[]
    columnas=[columna1,columna2,columna3,columna4,columna5]

    for fila in lista:
        for index, elemento in enumerate(fila):
            if index == 0:
                columna1.append(fila[index])
            elif index == 1:
                columna2.append(fila[index])        
            elif index == 2:
                columna3.append(fila[index])
            elif index == 3:
                columna4.append(fila[index])       
            elif index == 4:
                columna5.append(fila[index])


def pregunta_01():
    a = columna2
    for i in range(len(a)):
        a[i] = int(a[i])
    return sum(a)


def pregunta_02():
 
  a=columna1
  listaA=[]
  listaB=[]
  listaC=[]
  listaD=[]
  listaE=[]
  for i in a:
    if i=='A':
      listaA= a.count(i)
    elif i=='B':
      listaB=a.count(i)
    elif i=='C':
      listaC=a.count(i)
    elif i=='D':
      listaD=a.count(i)
    else:
      listaE=a.count(i)
  ayuda= [("A",listaA),("B",listaB),("C",listaC),("D",listaD),("E",listaE)]

  return ayuda


def pregunta_03():
  a=columna1
  b=columna2
  listaA=[]
  listaB=[]
  listaC=[]
  listaD=[]
  listaE=[]
  for tupla in zip(a, b): #obtenemos la tupla en cada iteración
    if tupla[0]=="A":
      listaA.append(tupla[1])
      A=sum(listaA)
    elif tupla[0]=="B":
      listaB.append(tupla[1])
      B=sum(listaB)
    elif tupla[0]=="C":
      listaC.append(tupla[1])
      C=sum(listaC)
    elif tupla[0]=="D":
      listaD.append(tupla[1])
      D=sum(listaD)
    else:
      listaE.append(tupla[1])
      E=sum(listaE)
        
  ayuda= [("A",A),("B",B),("C",C),("D",D),("E",E)]

  return ayuda


def pregunta_04():
  a=columna3
  lista=[]

  for j in range(0,len(a)):
    lista.append(a[j][5:7])


  lista1=[]
  lista2=[]
  lista3=[]
  lista4=[]
  lista5=[]
  lista6=[]
  lista7=[]
  lista8=[]
  lista9=[]
  lista10=[]
  lista11=[]
  lista12=[]
  for i in lista:
    if i=='01':
      lista1= lista.count(i)
    elif i=='02':
      lista2=lista.count(i)
    elif i=='03':
      lista3=lista.count(i)
    elif i=='04':
      lista4=lista.count(i)
    elif i=='05':
      lista5=lista.count(i)
    elif i=='06':
      lista6=lista.count(i)
    elif i=='07':
      lista7=lista.count(i)
    elif i=='08':
      lista8=lista.count(i)
    elif i=='09':
      lista9=lista.count(i)
    elif i=='10':
      lista10=lista.count(i)
    elif i=='11':
      lista11=lista.count(i)
    else:
      lista12=lista.count(i)
  ayuda= [("01",lista1),("02",lista2),("03",lista3),("04",lista4),("05",lista5),("06",lista6),("07",lista7),("08",lista8),("09",lista9),("10",lista10),("11",lista11),("12",lista12)]

  return ayuda


def pregunta_05():
  a=columna1
  b=columna2
  listaA=[]
  listaB=[]
  listaC=[]
  listaD=[]
  listaE=[]
  for tupla in zip(a, b): #obtenemos la tupla en cada iteración
    if tupla[0]=="A":
      listaA.append(tupla[1])
    elif tupla[0]=="B":
      listaB.append(tupla[1])
    elif tupla[0]=="C":
      listaC.append(tupla[1])
    elif tupla[0]=="D":
      listaD.append(tupla[1])
    else:
      listaE.append(tupla[1])
  ayuda= [("A",max(listaA),min(listaA)),("B",max(listaB),min(listaB)),("C",max(listaC),min(listaC)),("D",max(listaD),min(listaD)),("E",max(listaE),min(listaE))]

  return ayuda


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
