# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

import cod_generator

def nuevo_libro():
    codigo = generar_codigo()
    titulo = input("Ingrese el nombre del libro:")
    autor = input("Ingrese el nombre del autor del libro:")
    cant_ej_ad = input("Ingrese la cantiad de ejemplares que se adquirieron:")

    libro_nuevo = {'cod': codigo,'autor': autor,'titulo': titulo,'cant_ej_ad': cant_ej_ad,'cant_ej_pr': 0} 


    #NO SE SI MOSTRAR LA INFO O NO DEL LIBRO
    print("Libro registrado con éxito:")
    print(f"Código: {codigo} - Autor: {autor} - Título: {titulo} - Cantidad de ejemplares adquiridos: {cant_ej_ad}") 
    return libro_nuevo

def generar_codigo():
    cod = cod_generator.generar()
    return cod
