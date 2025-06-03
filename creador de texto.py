#importa la librería time
import time
#bienvenida
print("hola :3")
time.sleep(2)
#pregunta al usuario si quiere crear un archivo
crear_archivo = input("¿Quieres crear un archivo? (s/n): ")
#proceso si el usuario responde 's'
if crear_archivo.lower() == 's':
    nombre_archivo = input("Introduce el nombre del archivo: ")
    with open(nombre_archivo, 'w') as archivo:
        #crea el archivo y escribe el contenido
        contenido = input("Introduce el contenido del archivo: ")
        archivo.write(contenido)
        nombre_archivo += '.txt'
        #resultado
    print(f"Archivo '{nombre_archivo}' creado con éxito.")