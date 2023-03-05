# Importar el módulo os
import os

# Definir la ruta del directorio raíz
ruta = r"D:"

# Crear una lista vacía para almacenar los archivos duplicados
lista_duplicados = []

# Recorrer el directorio raíz y sus subcarpetas usando os.walk()
for carpeta, subcarpetas, archivos in os.walk(ruta):
  # Recorrer los archivos de cada carpeta
  for archivo in archivos:
    # Obtener la ruta completa del archivo usando os.path.join()
    ruta_archivo = os.path.join(carpeta, archivo)
    # Comprobar si el archivo ya está en la lista de duplicados
    if ruta_archivo in lista_duplicados:
      # Si es así, saltar al siguiente archivo
      continue
    # Si no, comprobar si hay otro archivo con el mismo nombre en otra carpeta
    else:
      # Recorrer las demás carpetas y subcarpetas usando otro bucle os.walk()
      for otra_carpeta, otras_subcarpetas, otros_archivos in os.walk(ruta):
        # Si la otra carpeta es la misma que la carpeta actual, saltar a la siguiente carpeta
        if otra_carpeta == carpeta:
          continue
        # Si no, recorrer los otros archivos de la otra carpeta
        else:
          for otro_archivo in otros_archivos:
            # Obtener la ruta completa del otro archivo usando os.path.join()
            otra_ruta_archivo = os.path.join(otra_carpeta, otro_archivo)
            # Comprobar si el otro archivo tiene el mismo nombre que el archivo actual
            if otro_archivo == archivo:
              # Contar el número de barras invertidas en cada ruta de carpeta
              num_barras_carpeta = carpeta.count("\\")
              num_barras_otra_carpeta = otra_carpeta.count("\\")
              # Comparar los números y quedarse con el mayor
              if num_barras_carpeta > num_barras_otra_carpeta:
                # Añadir solo el archivo de la carpeta más profunda a la lista de duplicados
                lista_duplicados.append(ruta_archivo)
              elif num_barras_otra_carpeta > num_barras_carpeta:
                # Añadir solo el otro archivo de la otra carpeta más profunda a la lista de duplicados
                lista_duplicados.append(otra_ruta_archivo)
              else:
                # Si tienen el mismo número de barras invertidas (misma profundidad), añadir ambos archivos a la lista de duplicados (opcional)
                lista_duplicados.append(ruta_archivo)
                lista_duplicados.append(otra_ruta_archivo)

# Abrir un archivo de texto para escribir los archivos duplicados con su ruta
with open("duplicados.txt", "w") as f:
  # Recorrer la lista de duplicados
  for dup in lista_duplicados:
    # Escribir la ruta en el archivo de texto con un salto de línea al final
    f.write(dup + "\n")

# Cerrar el archivo de texto
f.close()